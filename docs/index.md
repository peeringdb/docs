# PeeringDB

## Introduction

### Goals
!!! info
    These docs were meant to go away with beta, but since we haven't made official 2.0 docs yet, they're still around and (hopefully) have been updated to be current.

!!! danger "Attention"
    The MySQL interface is gone.

    Local database replication is accomplished with this [command line tool](https://github.com/peeringdb/peeringdb-py), please see the [documentation](http://peeringdb.github.io/peeringdb-py/cli/#sync) for more information.

    The last available MySQL dump is now available at <https://peeringdb.com/v1/final_export.sql>

### Changes from version 1

- All fields are validated (email, IP address, etc), fields not validated are either discarded or put into a notes field.
- Network connections to Internet Exchanges have changed to "links" with multiple IP addresses on them
- Numerous small schema changes
- All objects are structured under an Organization with granular access controls

## Quick start

If you want to poke around on your own, it's located at <https://peeringdb.com/> with self describing API docs at <https://peeringdb.com/apidocs/>

More thorough docs are at [API Specs](api_specs.md), but in a nutshell, just prepend the URL with `api/` to get that object in JSON.

For example:
<https://peeringdb.com/net/1>
becomes
<https://peeringdb.com/api/net/1>

List all via API by taking the `id` off:

<https://peeringdb.com/api/net>

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

- [PeeringDB 2.0](presentation/20161103-ITNOG2-Nipper-peeringdb.pdf) at [ITNOG2](http://www.itnog.it/itnog2/), Bologna, IT - November 3, 2016 - Arnold Nipper
- [PeeringDB Product Committee Charter Survey](presentation/20160919-epf11-Loos-peeringdb.pdf) at [EPF 11](https://www.peering-forum.eu/), Sofia, BG - September 20, 2016 - Eric Loos
- [PeeringDB 2.0](presentation/20160916-npd16-Wollny-peeringdb.pdf) at [NPD 16](http://www.neutralpeeringdays.net/), The Hague, NL - September 16, 2016 - Walt Wollny
- [PeeringDB 2.0](presentation/2016-08-30_afpif2016-Nipper-peeringdb.pdf) at [AfPIF 2016](https://www.internetsociety.org/afpif-2016/), Dar es Salaam, TZ - August 30, 2016 - Arnold Nipper
- [PeeringDB 2.0 for IXPs](presentation/2016-08-29_afix2016-Nipper-peeringdb.pdf) at [AFIX 2016](http://www.af-ix.net/?q=resources/2016/08/afix-2016-meeting-agenda), Dar es Salaam, TZ - August 29, 2016 - Arnold Nipper
- [PeeringDB 2.0](presentation/2016-06-07_PeeringDB-2.0_ENOG11.pdf) at [ENOG 11](https://www.enog.org/meetings/enog-11/), Moscow, RU - June 7, 2016 - Arnold Nipper
- [PeeringDB 2.0](presentation/2016-05-25_81-ripe-72-peeringdb.pdf) at [RIPE 72](https://ripe72.ripe.net/), Copenhagen, DK - May 25, 2016 - Greg Hankins
- [PeeringDB 2.0](presentation/2016-05-12_chi-nog-06-peeringdb.pdf) at [CHI-NOG 06](http://chinog.org/meetings/chi-nog-06/), Chicago, US - May 12, 2016 - Matt Griswold
- [PeeringDB 2.0 e o Cenário Brasileiro](presentation/2016-05-12_PeeringDB-2.0_GTER_41.pdf) and [IX.br Guia de cadastro de informações de ASNs no PeeringDB](presentation/2016-05-12_IX.br_PeeringDB_Guide.pdf) at [GTER 41](http://gtergts.nic.br/), Uberlândia, BR - May 12, 2016 - Eduardo Ascenço Reis
- [PeeringDB 2.0 for IXPs](presentation/2016-04-26_PeeringDB_28th_Euro-IX_Forum.pdf) at [28th Euro-IX Forum](https://www.euro-ix.net/), Luxembourg, LU - April 26, 2016 - Greg Hankins / Arnold Nipper
- [RIPE SEE 5](https://www.ripe.net/participate/meetings/regional-meetings/see-5), Tirana, AL - April 19, 2016 - Arnold Nipper
- [PeeringDB 2.0](presentation/2016-04-21_PeeringDB_UKNOF34.pdf) at [UKNOF34](https://indico.uknof.org.uk/conferenceDisplay.py?confId=36), Manchester, UK - April 21, 2016 - Greg Hankins
- [PeeringDB Update](presentation/2016-04-13_PeeringTrack-PDB-Update-GPF11.pdf) at [GPF 11](https://www.peeringforum.com/), Los Angeles, US - April 13, 2016 - Aaron Hughes
- [NetNod](http://www.netnod.se/netnod-spring-meeting-2016), Stockholm, SE - March 17, 2016 - Job Snijders
- [DKNOG6](http://www.dknog.dk/events/dknog6/), Copenhagen, DK - March 10, 2016 - Job Snijders
- [PeeringDB Update](presentation/PeeringTrack-PDB-Update-20160205.pdf) - Aaron Hughes
  Presented at
    - [APRICOT 2016](https://2016.apricot.net/), Auckland, NZ - February 23, 2016 by Aaron Hughes
    - [NANOG 66](http://nanog.org/meetings/nanog66/home), San Diego, CA, US - February 10, 2016 by Aaron Hughes
- [PeeringDB Version 2 Coding Introduction](presentation/PeeringDB_Version_2-Coding_Introduction.pdf) at [NANOG 66](http://nanog.org/meetings/nanog66/home), San Diego, CA, US - February 8, 2016 - Matt Griswold
- [PeeringDB Version 2 Brazil](presentation/PeeringDB_Version_2-Brazil.pdf) - Matt Griswold / Greg Hankins
  Presented at
    - [IX (PTT) Fórum 9](http://ix.br/pttforum/9/index-en.html), São Paulo, BR - December 8, 2015 by Greg Hankins
- [PeeringDB Version 2 Introduction](presentation/PeeringDB_Version_2-Introduction.pdf) - Matt Griswold
  Presented at
    - [27th Euro-IX Forum](https://www.euro-ix.net/news-and-events/euro-ix-forum/), Berlin, DE - October 26, 2015 by Greg Hankins
    - [DENOG7](http://www.denog.de/meetings/denog7/?lang=en), Darmstadt, DE - October 30, 2015 by Arnold Nipper 

## Tools

* [django-peeringdb](http://peeringdb.github.io/django-peeringdb/) is a Django library with a local PeeringDB database sync.  It defines the database schema to create a local database copy.  The library is easy to integrate into a common framework for local tools and custom interfaces, and also supports multiple database engines (MySQL, Postgres, SQLite).

* [peeringdb-py](http://peeringdb.github.io/peeringdb-py/) is a Python client for PeeringDB.  It features functions to get objects and display them in JSON or YAML format, and provides a whois-like display of records.  The client also has an integrated local database sync, and provides a Python library for integration with custom tools.  [Some examples](https://github.com/grizz/pdb-examples) are available too.

* [Pinder](http://github.com/dotwaffle/pinder) is a tool that facilitates peering.  If peering is desired between two networks, and you're happy to just configure sessions without a commercial agreement, Pinder acts as the middle man.  You can submit the request via either a basic web UI or an API, and the other network is notified or can periodically check their outstanding requests.  If both network agree to peer, they are notified to configure a session.  Once both networks indicate that sessions are configured and established, the request is then deleted. [A brief slide deck](http://accel.waffle.sexy/pinder.pdf) explains the functionality in more detail.

## How you can help

- Check your entries and make sure everything looks correct
- Port any scripts to the new API
- Send us feedback
- Improve these docs

## Reporting issues

You may view and report issues for PeeringDB 2.0 at [GitHub](https://github.com/peeringdb/peeringdb/issues).

Questions, comments and everything else should go to <support@peeringdb.com>.

Thanks for the testing/feedback, we look forward to hearing from you!
