
# PeeringDB Documentation

As viewable at https://docs.peeringdb.com/

*NOTE* Please do not put issues here anymore, new issues should be created at <https://github.com/peeringdb/peeringdb/issues>

### Modifying these docs

To work on and change these documents, you'll need git, python, and pip.

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

Install [MkDocs](http://www.mkdocs.org/) and other requirements
```sh
cd ~/src/docs
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --upgrade poetry
poetry install
```

Start mkdocs
```sh
cd ~/src/docs
source venv/bin/activate
mkdocs serve
```

or, if you'd like to specify the port, use -a $ADDRESS:$PORT, for example:

```sh
cd ~/src/docs
source venv/bin/activate
mkdocs serve -a 0.0.0.0:7889
```

You should now see a message similar to:
    Serving on <http://127.0.0.1:8000>

Point your browser at that URL, and you'll get real time updates to the generated documentation as you edit.

Markdown has its own formatting syntax, to get started look [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for an excellent cheatsheet.


### Updating the site

Once you are happy with your changes, commit and push, then run
```sh
cd ~/src/docs
git commit -a
git push
```

If you want to be able to view your changes at `$GITHUB_USER.github.io/docs`, just run:
```sh
cd ~/src/docs
source venv/bin/activate
mkdocs gh-deploy
```

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
source venv/bin/activate
poetry install
```
