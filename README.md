
# PeeringDB Documentation

As viewable at https://docs.peeringdb.com/

*NOTE* Please do not put issues here anymore, new issues should be created at <https://github.com/peeringdb/peeringdb/issues>

### Modifying these docs

To work on and change these documents, you'll need git and Python 3.11 or newer.

- CentOS
    ```sh
    sudo yum install python-pip
    ```

Fork the repo
- click the Fork button on <https://github.com/peeringdb/docs>
- select your GitHub username

Clone the repo
```sh
cd ~/src # Adjust here and below as appropriate.
git clone git@github.com:$GITHUB_USERNAME/docs.git
```

Install [Zensical](https://zensical.org/) and other requirements
```sh
cd ~/src/docs
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade uv
uv sync
```

Start the preview server
```sh
cd ~/src/docs
source .venv/bin/activate
zensical serve
```

or, if you'd like to specify the address and port, use -a $ADDRESS:$PORT, for example:

```sh
cd ~/src/docs
source .venv/bin/activate
zensical serve -a 0.0.0.0:7889
```

You should now see a message similar to:
    Serving /home/you/src/docs/site on <http://localhost:8000>

Point your browser at that URL, and you'll get real time updates to the generated documentation as you edit.

Markdown has its own formatting syntax, to get started look [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for an excellent cheatsheet.


### Blog posts

Add the post under `docs/blog/`, starting with its publish date as front matter,
and link it from `docs/blogs.md`:

```markdown
---
date: 2026-10-12
---
# Post title
```

The blog RSS feed (`/feed.xml`) is built from these dates, not from git history.

### Updating the site

Once you are happy with your changes, commit and push, then run
```sh
cd ~/src/docs
git commit -a
git push
```

To build the static site into `site/`, run:
```sh
cd ~/src/docs
source .venv/bin/activate
zensical build --clean
```

To get your changes pushed to the live site, just create a pull request, if you're unfamiliar with how to do that, GitHub has [documentation](https://help.github.com/articles/creating-a-pull-request/).

### Previews and publishing

Every pull request gets a preview site. Once the build finishes, a comment on the
PR links to `https://pr-<number>.<project>.pages.dev`, and each new push to the PR
updates it. Previews leave out PDFs and audio files to stay small, so links to those
don't work in a preview. Previews are not indexed by search engines.

Merging to `master` publishes the site: GitHub Actions builds it and pushes it to
the `gh-pages` branch, which GitHub Pages serves at docs.peeringdb.com. Nobody needs
to run a deploy by hand.

How it works (`.github/workflows/`):

- `pr-preview-build.yml` builds the PR with `zensical build --strict` and no access
  to secrets, so it is safe for pull requests from forks. A failing build fails this
  check.
- `pr-preview-deploy.yml` runs from `master` after a successful build, uploads the
  built files to Cloudflare Pages and comments the URL. It never runs code from the PR.
- `deploy.yml` builds and publishes on every push to `master`, one `gh-pages` commit
  per deploy. It can also be started by hand from the Actions tab.

One-time setup for repo admins:

- Settings → Pages: source "Deploy from a branch", branch `gh-pages` (as before).
- Settings → Actions → General → "Approval for running fork pull request workflows":
  choose "Require approval for all external contributors". GitHub's default only
  asks for first-time contributors, and a preview publishes whatever a fork's build
  produces under PeeringDB's Cloudflare project.
- Cloudflare: create the Pages project once, with
  `npx wrangler pages project create <project> --production-branch=master`, and an
  API token with the "Cloudflare Pages: Edit" permission.
- Settings → Secrets and variables → Actions: secret `CLOUDFLARE_API_TOKEN`, and
  variables `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_PAGES_PROJECT`. Until the
  variables are set, previews are skipped and everything else still works.

To roll back the live site, revert the change on `master`; the deploy workflow
publishes the reverted site within a few minutes. In an emergency, push an older
deploy straight back (`git push --force origin <older-sha>:gh-pages`), and still
revert on `master` so the next merge doesn't publish the change again.



### Updating your fork

The first time you want to do it, you need to add a remote with
```sh
cd ~/src/docs
git remote add upstream git@github.com:peeringdb/docs.git
```

After that, to sync to the upstream repo and install requirements/updates
```sh
cd ~/src/docs
git fetch upstream
git merge upstream/master
source .venv/bin/activate
uv sync
```

`zensical` is intentionally not pinned in `pyproject.toml`. To move the lock file to
the newest Zensical release, run `uv sync --upgrade-package zensical` and commit the
updated `uv.lock`.

### Theme

The site uses Zensical's built-in theme. PeeringDB branding lives in `mkdocs.yml`
(logo, favicon, palette, footer social links) and `docs/stylesheets/peeringdb.css`
(colours). `overrides/main.html` adds the blog RSS feed to every page's `<head>`.
Search is Zensical's built-in search.
