# HOWTO: Install peeringdb-py

You can install `peeringdb-py` on a wide selection of operating systems. Users have installed it on several Linux distributions, macOS, and Windows Subsystem for Linux.

It will give you a local version of PeeringDB’s SQL database. Unlike the PeeringDB API, the SQL data structure might change without notice. Please do not build tools that make SQL queries. We suggest using our library to make [API calls](https://docs.peeringdb.com/api_specs/) on your local cache. We maintain the library and commit to maintaining the API functionality, even if the underlying database structure changes.

Please let us know if you find a query that is only possible with SQL and not via the API. Either create an issue in [GitHub](https://github.com/peeringdb/peeringdb/issues), or send a mail describing the problems to [support@peeringdb.com](mailto:support@peeringdb.com).

## PeeringDB credentials

You only need a PeeringDB account if you want to synchronize the contact information to your peeringdb-py cache. If you want to synchronize the whole database, including the contact data, you will need an API Key.

If you are installing peeringdb-py for organizational use you should use an organizational API Key. You can use an API Key tied to a user account for personal use. We have a [HOWTO guide for API Keys](/howto/api_keys/).

## Software requirements

You must ensure these these packages are installed to install and use `peeringdb-py`:
- git
- pip
- python
- virtualenv

You will also need to have a database installed. The configuration defaults to using SQLite.

## Database

`peeringdb-py`’s defaults to an SQLite3 database. You can choose to use a different database. If you want to do this you must adjust the database engine statement in the `config.yaml`, which is placed in your `.peeringdb/config.yaml`, which sits in your home directory. Whichever database you choose, it must use UTF-8 as the character set.

## Installation instructions for `peeringdb-py`

### Create a directory for `peeringdb-py` and go there
 
`mkdir ~/peeringdb-py && cd ~/peeringdb-py`

### Create a virtual environment 

`virtualenv --python=python3 pdbvenv`

### Activate the virtual environment

`source pdbvenv/bin/activate`

### Install `peeringdb-py`
Run `pip` to install the local cache and Django. 

```
sh
pip install --upgrade pip setuptools
pip install peeringdb django-peeringdb

# check for which version of django suits you
# when in doubt use the LTS version from https://www.djangoproject.com/download/
pip install "django>=3.2,<3.3"
```

### Create a `peeringdb-py` configuration file

`peeringdb config set -n`

### Edit your configuration

edit `[HOME]/.peeringdb/config.yaml`.  Make sure you adjust the directory name. Replace [HOME] with the relevant file path. Replace [CENSORED] with your own API Key, if you are authenticating. Remove [CENSORED] if you choose to remain anonymous. Anonymous users cannot see some contact information.

```
orm:
  backend: django_peeringdb
  database:
    engine: sqlite3
    host: ''
    name: [HOME]/peeringdb-py/peeringdb.sqlite3
    password: ''
    port: 0
    user: ''
  migrate: true
  secret_key: ''
sync:
  api_key: [CENSORED]
  only: []
  password: ''
  strip_tz: 1
  timeout: 0
  url: https://www.peeringdb.com/api
  user: ''
```

### Check that the software is installed

This will confirm that `peeringdb-py` is running by showing you the software version:
`peeringdb --version`	

You will see something like:
`peeringdb 1.2.1.1`

This will confirm that Django is running by showing you the software version:
`django-admin --version`

You will see something like:
`2.2.28`

This will show that you have django-peeringdb installed and what version it is.
`pip freeze | grep django-peeringdb`

You will see something like this:
`django-peeringdb==2.14.1`

### Synchronize your new local cache

This will synchronize your local cache with the server and tell you how long it took.
`time peeringdb sync`

You will see something like this:
```
real    14m47.515s
user    14m27.077s
sys     0m1.939s
```

If you wait and then synchronize again you'll get the changes since your initial sync. The process does not pull the full database, making it a very efficient update process. You will see a faster synchronization for updates than the initial pull.

`time peeringdb sync`

The times you see will look something like this:
```
real    0m3.110s
user    0m1.074s
sys     0m0.088s
```

### Fetch private data

The initial sync will happen from the public cache, which does not contain data that isn't available to unauthenticated requests, such as network contacts that are set to `Users` visibility. In order to fetch this data you can pass the `--fetch-private` argument.

Note that you will need to have valid authentication set up for this (preferably with an API key), for example:

```
peeringdb sync --fetch-private
```

### Automatically refreshing data

You can schedule automatic database updates by creating an entry in your crontab. We recommend synchronizing every hour. You should not synchronize on the hour but offset at a random minute in the hour. This distributes users across the hour and reduces the burden on the server. 

This will open your default editor and allow you to create a scheduled task.

`crontab -e`

Place this entry in your crontab and save the file, changing [HOME] to the relevant file path.

`00 * * * * sleep $[RANDOM\%300] ; cd [HOME]/peeringdb-py ; touch peeringdb.sync.log ; date >> peeringdb.sync.log ; ./pdbvenv/bin/peeringdb sync >> peeringdb.sync.log 2>&1`

Confirm what is scheduled:

`crontab -l` 

### Upgrade `peeringdb-py` to the latest version

```
sh
pip install --upgrade peeringdb django-peeringdb
```

## Example usage

The SQL data structure might change without notice. Please do not build tools that make SQL queries. We suggest using our library to make API calls on your local cache. We maintain the library and commit to maintaining the API functionality, even if the underlying database structure changes.
