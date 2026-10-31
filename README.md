# dimpap / dev notes

A personal site for projects, programming notes, and research.
Built with Jekyll and Markdown, hosted at <https://dimpap99.github.io/>.
No frontend build tool, database, or JavaScript is needed.

## Run it locally

Install Ruby 3.3 and Bundler, then run from this directory:

```bash
bundle install
bundle exec jekyll serve --drafts --unpublished
```

Open <http://127.0.0.1:4000>. This preview includes drafts and hidden project
write-ups. Those flags are for your local preview. The normal GitHub Pages build
does not publish them. Restart the server after changing `_config.yml`.

For a preview of exactly what will go live:

```bash
bundle exec jekyll serve
```

## Write a note

```bash
python3 scripts/content.py post "What I learned building a graph tool"
```

This creates `_drafts/what-i-learned-building-a-graph-tool.md` from
`templates/post.md`, plus an image directory. Edit the Markdown, fill in the
one-sentence `description`, and add optional `tags: [graphs, python]`.

When it is ready:

```bash
python3 scripts/content.py publish what-i-learned-building-a-graph-tool
```

The helper moves the draft into `_posts/YYYY-MM-DD-slug.md` using today's date.
Use `--date 2026-10-31` to choose a publication date. It never pushes to GitHub
or replaces an existing file. Future-dated posts stay hidden until a build runs
on or after that date. GitHub Pages does not schedule a rebuild for you.

## Add a project

```bash
python3 scripts/content.py project "My old ray tracer"
```

Edit `_projects/my-old-ray-tracer.md`. The front matter controls its listing:

```yaml
title: "My old ray tracer"
description: "A short explanation of what it does and why it was interesting."
year: 2020
stack: [C++, OpenGL]
status: "archived"
repo_url: "https://github.com/DimPap99/your-repository"
demo_url: ""
published: false
```

The body is the write-up: the idea, how it works, what you learned. The fields
above are examples. Replace them with your actual project details. `year` is
the year you built the project, and projects appear newest first. Empty source
and demo links are automatically omitted. Set `published: true` when ready.

## Images and files

Keep images in `assets/images/<post-or-project-slug>/`. For example:

```liquid
![A screenshot of the finished tool]({{ '/assets/images/my-tool/screenshot.png' | relative_url }})
```

Use descriptive alt text, reasonably sized images, and filenames without spaces.
For code, link the GitHub repository. For large downloads, link a GitHub Release
instead of adding build artifacts to this blog. PDFs can go in `assets/files/`
and be linked with the same `relative_url` pattern.

## Publish to GitHub Pages

This repository is already configured to publish from **main / (root)**. A push
to `main` triggers the Pages build. To publish your finished content:

```bash
git status
git add <the-files-you-want-to-publish>
git commit -m "Add a project write-up"
git push origin main
```

Review the file list before committing. Only add the source files. `_site/` is
generated and ignored. If hosting needs configuring again, go to the repository's
**Settings → Pages → Build and deployment**, choose **Deploy from a branch**,
then **main** and **/(root)**. Build results appear in the **Actions** tab.

You can also write entirely on GitHub:

1. Copy `templates/post.md` into a new file at `_posts/YYYY-MM-DD-your-title.md`,
   or copy `templates/project.md` into `_projects/your-project.md`.
2. Replace the `@@...@@` placeholders, fill in the metadata, and write the body.
   For a project, set `published: true` when ready.
3. Use **Add file → Upload files** for images under `assets/images/your-slug/`.
4. Commit to `main`, or open a pull request if you prefer to review it first.

Files under `_drafts/` stay out of the rendered site, but **they are still readable
in a public GitHub repository**. Keep private or unpublished research outside the
repository until you are ready to share its source.

See [GitHub's guide to adding Jekyll content](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll)
and the [publishing source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Personalize

| File | What to edit |
| --- | --- |
| `_config.yml` | Site title, name, description, URL, GitHub username, contact text |
| `_data/profile.yml` | Homepage intro, current position, research areas, education |
| `about.html` | The longer personal introduction |
| `css/site.css` | Colors (variables at the top), typography, responsive layout |
| `_posts/` | Published notes |
| `_projects/` | Project write-ups |
| `_drafts/` | Unpublished notes and the original formatting example |
| `templates/` | Starting points used by the content helper |

The site introduction is saved as a draft. No sample posts or projects appear
on the public site. Add your own content when ready. The RSS feed, sitemap,
syntax highlighting, page metadata, and old `/archive.html` redirect are automatic.

## Check before publishing

```bash
bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
python3 -m unittest discover -s tests
```
