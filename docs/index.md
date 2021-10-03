# About PeeringDB

## How can PeeringDB help me to interconnect?

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/QA2PvYbvDhg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Create and account and [register](https://www.peeringdb.com/register) in PeeringDB to get started.

## Acceptable use policy

By using this service, you agree to adhere to our [AUP](https://www.peeringdb.com/aup).

## Getting help

* Please log bugs and feature requests at [GitHub](https://github.com/peeringdb/peeringdb/issues).

* Several PeeringDB mailing lists are listed below.

* Questions, comments and everything else should go to <support@peeringdb.com>.

## Mailing lists

We have changed the way in which PeeringDB will be announcing future enhancements, changes, maintenance windows, and other information. If you would like to be notified of certain events, or participate in certain discussions, please subscribe to one of the following email lists:

* [PeeringDB Announce](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-announce)
    All PeeringDB administrative announcement information, such as upgrades, maintenances, outages, etc.

* [PeeringDB Governance](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-gov)
    Discussion list for PeeringDB governance issues.  This is a community-based effort, the community’s input will help guide the future of the PeeringDB as it has always done.

* [PeeringDB Technical](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-tech)
    Discussion about PeeringDB technical topics.

* [PeeringDB Translate](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/pdb-translate)
    Discussions about PeeringDB translations.

* [PeeringDB User-Discuss](http://lists.peeringdb.com/cgi-bin/mailman/listinfo/user-discuss)
    All other topics.

Our goal is to give you all the information you want, and no more.  Please subscribe to any of these lists you feel are appropriate, or none. You will still be able to use the database even if you are not subscribed to any lists.

## Quick start

PeeringDB is available at <https://www.peeringdb.com/> with self-describing API docs at <https://www.peeringdb.com/apidocs/>.  More thorough docs are at [API Specs](api_specs.md), but in a nutshell, just prepend the URL with `api/` to get that object in JSON.

For example:
<https://www.peeringdb.com/net/1>
becomes:
<https://www.peeringdb.com/api/net/1>

List all via API by taking the `id` off:
<https://www.peeringdb.com/api/net>

Local database replication is accomplished with this [command line tool](https://github.com/peeringdb/peeringdb-py), please see the [documentation](http://peeringdb.github.io/peeringdb-py/cli/#sync) for more information.

## Release notes

The [release notes](release_notes/index.md) list the GitHub issues and a summary of what has changed in PeeringDB software releases.

## Guides

- [es] [Guía corta para uso de peeringdb.com](guide/guia_PeeringDB.pdf) - Fabián Mejía
- [pt-BR] [Guia de cadastro de informações de ASNs no PeeringDB](guide/PeeringDB_Cadastro_de_ASN.pdf) - Julimar Lunguinho Mendes / Equipe de Engenharia
- [pt-BR] [Guia de cadastro de informações de Facilities no PeeringDB](guide/PeeringDB_Cadastro_de_Facilities.pdf) - Julimar Lunguinho Mendes / Equipe de Engenharia

## Tools

The [tools](tools.md) page features tools developed by PeeringDB users.

## Tutorials and workshops

High-level [HOWTOs](howtos.md) provide a beginner detailed instructions on how to get started using PeeringDB.

- [The How-to Guide](presentation/20210506-Teraco_Tech_Day.pdf) at [Teraco Virtual Tech Day with PeeringDB](https://www.teraco.co.za/events/virtual-tech-days/?fbclid=IwAR310Y84fDzXnZOcfXWxnogcgkDTrWaTwfM4u0U8c5wkFPd5ihNaHuNWjzk) - May 6, 2021 - Ben Ryall
- [PeeringDB Tutorial, learning the GUI and the API](presentation/20200220-1-2-GUI-API-APRICOT2020-Arnold-Nipper.pdf) at [APRICOT 2020](https://2020.apricot.net/program/schedule/#/day/9), Melbourne, AU - February 20, 2020 - Arnold Nipper
- [How is PeeringDB organised?](presentation/20191110-1-GUI-DENOG11-Arnold-Nipper.pdf) and [The PeeringDB API](presentation/20191110-2-API-DENOG11-Arnold-Nipper.pdf) at [DENOG11](https://www.denog.de/de/meetings/denog11/workshops.html), Hamburg, DE - November 10, 2019 - Arnold Nipper
- [PeeringDB Workshop](presentation/20190820_PeeringDB_Workshop_1-2_AfPIF_2019.pdf) at [AfPIF-10](https://www.afpif.org/afpif-10/), Balaclava, MV - August 20, 2019 - Arnold Nipper ([video](https://livestream.com/internetsociety/afpif2019/videos/195303661) starts at 14:00)
- [Part 1: Intro](presentation/20190227-peeringdb-workshop-1-intro.pdf), [Part 2: Main](presentation/20190227-peeringdb-workshop-2-main.pdf), [Part 3: API](presentation/20190227-peeringdb-workshop-3-api.pdf) at [APRICOT 2019](https://2019.apricot.net/program/schedule/#/day/10/peeringdb-tutorial), Daejeon, KR - February 27, 2018 - Arnold Nipper ([video](https://www.youtube.com/watch?v=cygDlOqs9tI))

## Presentations

The [presentations](presentations.md) page has a complete list of PeeringDB presentations that were given at events around the world.

## Open source

#### Source code audit

PeeringDB commissioned a full audit of PeeringDB's source code in 2018. [Computest](https://www.computest.nl/) (the auditor) prepared a __Third Pary Memo__, this memo provides a high level overview of the outcome of the source code audit. The report is available [here](gov/misc/2018-05-16_Computest_Source_Code_Audit_TPM.pdf).

## Beta development

* The [PeeringDB beta server](https://beta.peeringdb.com/) runs the latest beta software version, with full access over HTTP and the API.  Note that changes made to the beta database are local to the beta server only, and are not reflected on the production servers.

* The [latest changes to PeeringDB](https://beta.peeringdb.com/changes) automagically redirects to the list of issues on PeeringDB's GitHub repository that document all of the changes in the current beta version.

## Historical data

* MySQL dumps from July, 29 2010 to March 14, 2016 are archived by CAIDA at <http://data.caida.org/datasets/peeringdb-v1/>.

## How you can help

* Check your entries and make sure everything looks correct

* Port any scripts to the new API

* Send us feedback

* Improve these docs

* Add or improve a [translation](translation/)

Thanks for your feedback, we look forward to hearing from you!
