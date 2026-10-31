#!/usr/bin/env python3
"""Create Markdown content without dependencies; keep new work unpublished."""

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]


def slugify(title):
    ascii_title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_title.lower()).strip("-")
    if not slug:
        raise ValueError("Use a title with at least one ASCII letter or number.")
    return slug


def create(kind, title, root=ROOT):
    title = title.strip()
    if not title or any(character in title for character in "\r\n"):
        raise ValueError("The title must be one nonempty line.")
    slug = slugify(title)
    directory = "_drafts" if kind == "post" else "_projects"
    destination = root / directory / f"{slug}.md"
    if kind == "post" and any((root / "_posts").glob(f"????-??-??-{slug}.md")):
        raise ValueError(f"A published post already uses the slug '{slug}'. Choose another title.")
    template = (root / "templates" / f"{kind}.md").read_text(encoding="utf-8")
    asset_path = f"/assets/images/{slug}"
    text = (template.replace("@@TITLE@@", json.dumps(title, ensure_ascii=False))
            .replace("@@YEAR@@", str(date.today().year))
            .replace("@@ASSET_PATH@@", asset_path))
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents accidentally replacing an existing write-up.
    with destination.open("x", encoding="utf-8") as output:
        output.write(text)
    image_directory = root / asset_path.lstrip("/")
    image_directory.mkdir(parents=True, exist_ok=True)
    return destination, image_directory


def publish(slug, publication_date, root=ROOT):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("Use the draft's filename without .md, for example: my-first-note")
    source = root / "_drafts" / f"{slug}.md"
    if not source.is_file():
        raise ValueError(f"No draft found at _drafts/{slug}.md")
    if any((root / "_posts").glob(f"????-??-??-{slug}.md")):
        raise ValueError(f"A published post already uses the slug '{slug}'.")
    destination = root / "_posts" / f"{publication_date.isoformat()}-{slug}.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as output:
        output.write(source.read_text(encoding="utf-8"))
    source.unlink()
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for kind in ("post", "project"):
        command = commands.add_parser(kind, help=f"Create an unpublished {kind} from a template")
        command.add_argument("title", help="Put multi-word titles in quotes")
    publication = commands.add_parser("publish", help="Move a finished draft into _posts locally")
    publication.add_argument("slug", help="The draft's filename without .md")
    publication.add_argument("--date", type=date.fromisoformat, default=date.today(), metavar="YYYY-MM-DD")
    args = parser.parse_args()
    try:
        if args.command == "publish":
            destination = publish(args.slug, args.date)
            print(f"Ready: {destination.relative_to(ROOT)}")
            print("This changes local files only. Commit and push when you want it live.")
        else:
            destination, image_directory = create(args.command, args.title)
            print(f"Created: {destination.relative_to(ROOT)}")
            print(f"Images:  {image_directory.relative_to(ROOT)}/")
            if args.command == "post":
                print(f"When ready: python3 scripts/content.py publish {destination.stem}")
            else:
                print("When ready: set published: true in the file's front matter.")
    except (ValueError, FileExistsError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
