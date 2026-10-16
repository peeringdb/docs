
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

Zensical has no `gh-deploy` command; publishing the built `site/` directory to
GitHub Pages is handled separately.

To get your changes pushed to the live site, just create a pull request, if you're unfamiliar with how to do that, GitHub has [documentation](https://help.github.com/articles/creating-a-pull-request/).



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

The site look comes from `peeringdb_theme/`, a standalone Zensical theme derived from
the MkDocs 1.4.3 `mkdocs` theme (see `THIRD-PARTY-NOTICES.md`). `main.html` holds the
PeeringDB customisations (footer, no previous/next links). Search reads the
`search.json` index that Zensical generates (`peeringdb_theme/js/search.js`).
