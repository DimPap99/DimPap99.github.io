#!/usr/bin/env python3
"""Check generated local links, assets, and anchors using the standard library."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.links = []
        self.ids = set()
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for attribute in ("href", "src"):
            if attrs.get(attribute):
                self.links.append(attrs[attribute])


def check(directory, baseurl=""):
    directory = directory.resolve()
    pages = {path: Page(path) for path in directory.rglob("*.html")}
    errors = []
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            url_path = unquote(url.path)
            if baseurl and url_path.startswith("/"):
                if not url_path.startswith(baseurl + "/") and url_path != baseurl:
                    errors.append(f"{path.relative_to(directory)}: missing baseurl in {link}")
                    continue
                url_path = url_path[len(baseurl):]
            target = (directory / url_path.lstrip("/") if url_path.startswith("/")
                      else path.parent / url_path) if url_path else path
            target = target.resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{path.relative_to(directory)}: missing target {link}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{path.relative_to(directory)}: missing anchor {link}")
    return pages, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path("_site"))
    parser.add_argument("--baseurl", default="", help="Use with a build made with --baseurl")
    args = parser.parse_args()
    if not args.directory.is_dir():
        parser.error("Build the site first: bundle exec jekyll build")
    pages, errors = check(args.directory, args.baseurl.rstrip("/"))
    if not pages:
        errors.append("No generated HTML pages found.")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Checked {len(pages)} HTML pages: all local links, assets, and anchors resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
