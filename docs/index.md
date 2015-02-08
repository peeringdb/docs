
# PeeringDB 2.0

## Introduction

### Goals
This stage is an introduction to the new RESTful API and RFC on the new schema and interface. Changes are automatically synced from version 1 every hour.

!!! danger "Attention"
    The MySQL interface **WILL** be going away

We do not have a specific time frame for moving away from the legacy interface, and will make sure everyone has ample chance to migrate to the JSON interface.

### Timeline
The next phase will be getting people switched over to the new API and making any changes deemed necessary. Once we've accomplished that, we intend on having the write interface ready to go and can make the switch.

### Changes from version 1

- All fields are validated (email, IP address, etc), fields not validated are either discarded or put into a notes field.
- Network connections to Internet Exchanges have changed to "links" with multiple IP addresses on them
- Numerous small schema changes
- All objects are structured under an Organization with granular access controls

## Quick start

If you want to poke around on your own, it's **readonly** at <https://beta.peeringdb.com/> with self describing API docs at <https://beta.peeringdb.com/apidocs/>

More thorough docs are at [API Specs](api_specs.md), but in a nutshell, just prepend the URL with `api/` to get that object in JSON.

For example:
<https://beta.peeringdb.com/net/1>
becomes
<https://beta.peeringdb.com/api/net/1>

List all via API by taking the `id` off:

<https://beta.peeringdb.com/api/net>

## Mailing list

There has been a mailing list created for PeeringDB users, which is where all future API and schema change discussions will take please.  You may subscribe by sending an email to user-discuss+subscribe@peeringdb.com if interested.

## How you can help

- Check your entries and make sure everything looks correct
- Port any scripts to the new API
- Send us feedback
- Improve these docs

## Reporting Issues

Strictly speaking we're really only looking for API bugs and missing or incorrect data right now. The web front end is crude and unpolished and mainly there to view the information without using the API. That said, any reports will be helpful when we get to that (which will be next).

You may view and report issues at [GitHub](https://github.com/peeringdb/1to2/issues)

Questions, comments and everything else should go to support@peeringdb.com

Thanks for the testing/feedback, we look forward to hearing from you!

