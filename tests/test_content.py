import importlib.util
import json
from datetime import date
from pathlib import Path
import shutil
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("content", REPO / "scripts/content.py")
content = importlib.util.module_from_spec(spec)
spec.loader.exec_module(content)


class ContentWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(REPO / "templates", self.root / "templates")

    def test_new_note_stays_in_drafts_and_escapes_title(self):
        title = 'Graphs: "a small experiment"'
        path, images = content.create("post", title, self.root)
        self.assertEqual(path.parent.name, "_drafts")
        self.assertFalse((self.root / "_posts").exists())
        self.assertEqual(json.loads(path.read_text().splitlines()[1][7:]), title)
        self.assertTrue(images.is_dir())
        self.assertNotIn("@@", path.read_text())

    def test_duplicate_creation_preserves_existing_work(self):
        path, _ = content.create("post", "My note", self.root)
        path.write_text("Work I do not want to lose")
        with self.assertRaises(FileExistsError):
            content.create("post", "My note", self.root)
        self.assertEqual(path.read_text(), "Work I do not want to lose")

    def test_publishing_moves_markdown_without_changing_it(self):
        draft, _ = content.create("post", "My note", self.root)
        original = draft.read_text()
        published = content.publish("my-note", date(2026, 10, 31), self.root)
        self.assertEqual(published.name, "2026-10-31-my-note.md")
        self.assertEqual(published.read_text(), original)
        self.assertFalse(draft.exists())

    def test_publishing_refuses_conflicting_slug_and_keeps_draft(self):
        draft, _ = content.create("post", "My note", self.root)
        posts = self.root / "_posts"
        posts.mkdir()
        existing = posts / "2025-01-01-my-note.md"
        existing.write_text("An existing published post")
        with self.assertRaises(ValueError):
            content.publish("my-note", date(2026, 10, 31), self.root)
        self.assertTrue(draft.is_file())
        self.assertEqual(existing.read_text(), "An existing published post")

    def test_cannot_create_duplicate_of_published_note(self):
        content.create("post", "My note", self.root)
        content.publish("my-note", date(2026, 10, 31), self.root)
        with self.assertRaises(ValueError):
            content.create("post", "My note", self.root)

    def test_path_traversal_is_rejected(self):
        for slug in ("../outside", "/tmp/note", "nested/note", "note.md"):
            with self.subTest(slug=slug), self.assertRaises(ValueError):
                content.publish(slug, date(2026, 10, 31), self.root)

    def test_project_starts_hidden(self):
        path, _ = content.create("project", "An old build", self.root)
        self.assertEqual(path.parent.name, "_projects")
        self.assertIn("published: false", path.read_text())
        self.assertNotIn("@@", path.read_text())

    def test_invalid_titles_do_not_create_files(self):
        for title in ("", "   ", "!!!", "Title\npublished: true"):
            with self.subTest(title=title), self.assertRaises(ValueError):
                content.create("post", title, self.root)
        self.assertFalse((self.root / "_drafts").exists())


if __name__ == "__main__":
    unittest.main()
