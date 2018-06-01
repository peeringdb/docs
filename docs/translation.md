## Contributing to translations

### Adding a new locale

If you wish to add a new locale, create a new ticket at <https://github.com/peeringdb/peeringdb/issues> stating your intent and one of the operators / developers will generate the necessary files for your locale and add them to the repository.

Once they are created and ready, PeeringDB will open a ticket and assign it to you for progress and so multiple people can coordinate progress.


### Getting the files

We prefer that you use git, fork the repo, and submit a pull request when done. If you don't want to use git, you may either download them from the appropriate directory at <https://github.com/peeringdb/peeringdb/tree/master/locale> or end an email to <productcom@lists.peeringdb.com> and we'll email you the files.


### Git

#### Fork the repository

If you're unfamiliar with forking, check out docs at <https://help.github.com/articles/fork-a-repo/>.

To fork the repo:

- click the fork button on <https://github.com/peeringdb/peeringdb>
- select your GitHub username


#### Clone the forked repository

```sh
git clone git@github.com:$GITHUB_USERNAME/peeringdb.git
cd peeringdb
```


### Find the files

Locale files are kept in the `locale/` directory.

There are 2 `.po` files for each language:

- `django.po` : server side translation strings
- `djangojs.po` - client side translation strings (JavaScript prompts etc.)


### Make your changes to the files

Use your favorite gettext translation editor to make changes to the files. Once you are happy with your changes, submit a pull request at <https://github.com/peeringdb/peeringdb/pulls>.


### Submit your changes

If you used git, please submit a pull request at <https://github.com/peeringdb/peeringdb/pulls>, if not, please send the files to <productcom@lists.peeringdb.com>


### Gettext translation editors

- [Poedit](https://poedit.net/)


### Thanks to the translators!

#### pt

- Robert Philips (NTT Communications)
- Ligio Gomes (NTT Communications)
