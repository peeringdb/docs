
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

## Mailing lists

We have changed the way in which PeeringDB will be announcing future enhancements, changes, maintenance windows, and other information. If you would like to be notified of certain events, or participate in certain discussions, please subscribe to one of the following email lists:

* [PeeringDB Announce](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce)
    All PeeringDB administrative information, such as upgrades,
    maintenances, outages, etc.

* [PeeringDB Governance](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-gov)
    Discussion list for PeeringDB governance issues This is a
    community-based effort, the community’s input will help guide the
    future of the PeeringDB (as it has always done).

* [PeeringDB Technical](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-tech)
    Discussion of the back end of PeeringDB & other technical topics

* [PeeringDB User-Discuss](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/user-discuss)
    All other list traffic.

Our goal is to give you all the information you want, and no more.  Please subscribe to any of these lists you feel are appropriate, or none. You will still be able to use the database even if you are not subscribed to any lists.

<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.5";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>

<p>
<div class="fb-like" data-href="https://www.facebook.com/peeringdb" data-layout="button_count" data-action="like" data-show-faces="true" data-share="true"></div>
</p>

<p>
<a href="https://twitter.com/PeeringDB" class="twitter-follow-button" data-show-count="false">Follow @PeeringDB</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
</p>


## Presentations

- [PeeringDB Version 2 Brazil](presentation/PeeringDB_Version_2-Brazil.pdf) - Matt Griswold / Greg Hankins
  Presented at
    - [IX (PTT) Fórum 9](http://ix.br/pttforum/9/index-en.html), São Paulo, BR - December 8, 2015 by Greg Hankins
- [PeeringDB Version 2 Introduction](presentation/PeeringDB_Version_2-Introduction.pdf) - Matt Griswold
  Presented at
    - [27th Euro-IX Forum](https://www.euro-ix.net/news-and-events/euro-ix-forum/), Berlin, DE - October 26, 2015 by Greg Hankins
    - [DENOG7](http://www.denog.de/meetings/denog7/?lang=en), Darmstadt, DE - October 30, 2015 by Arnold Nipper 


## How you can help

- Check your entries and make sure everything looks correct
- Port any scripts to the new API
- Send us feedback
- Improve these docs

## Reporting Issues

Strictly speaking we're really only looking for API bugs and missing or incorrect data right now. The web front end is crude and unpolished and mainly there to view the information without using the API. That said, any reports will be helpful when we get to that (which will be next).

You may view and report issues for version 2 at [GitHub](https://github.com/peeringdb/1to2/issues)

If you find incorrect data in version 1 (at www.peeringdb.com), please just email
support@peeringdb.com with what should be corrected.

Questions, comments and everything else should go to support@peeringdb.com

Thanks for the testing/feedback, we look forward to hearing from you!

