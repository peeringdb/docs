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

We have a [separate document](https://github.com/peeringdb/peeringdb-py/blob/master/docs/local_server.md) describing how to install `peeringdb-py`, run the server setup, and make local queries using the API. 

Because the server now has an automatic synchronization process, you no longer need to create a cron job to synchronize data.
