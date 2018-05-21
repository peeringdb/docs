## Contributing to translations

### Fork the repository

If you're unfamiliar with forking, check out docs at <https://help.github.com/articles/fork-a-repo/>

- click the fork button on <https://github.com/peeringdb/peeringdb>
- select your GitHub username


### Clone the repository

```sh
git clone git@github.com:$GITHUB_USERNAME/peeringdb.git
cd peeringdb
```


### Find the files

Locale files are kept in the `locale/` directory.

There are 2 `.po` files for each language:

- `django.po` : server side translation strings
- `djongojs.po` - client side translation strings (JavaScript prompts etc.)


#### Adding a new locale

If you wish to add a new locale, create a new ticket at https://github.com/peeringdb/peeringdb/issues stating your intent and one of the operators / developers will generate the necessary files for your locale and add them to the repository.


### Make your changes to the files

Use your favorite gettext translation editor to make changes to the files. Once you are happy with your changes, submit a pull request at <https://github.com/peeringdb/peeringdb/pulls>.


## Gettext translation editors

- [Poedit](https://poedit.net/)
