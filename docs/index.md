# About PeeringDB

## How can PeeringDB help me to interconnect?

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/QA2PvYbvDhg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Getting started

New to PeeringDB? [Register an account](https://www.peeringdb.com/register), then follow the HOWTO for your role:

* [Network Operator](howto/get-started-operator.md)
* [Exchange Operator](howto/get-started-exchange.md)
* [Facility or Campus Operator](howto/get-started-facility.md)
* [Carrier Operator](howto/get-started-carrier.md)

See all [HOWTOs](howtos.md) for more guides, our [glossary](glossary.md) of PeeringDB terms, and [guides in other languages](#guides-in-other-languages) below.

## Policies

* By using this service, you agree to adhere to PeeringDB's [Acceptable Use Policy](https://www.peeringdb.com/aup).
* The [Admin Committee Guidelines and Criteria for Approving Networks, IXPs, and Facilities](committee/admin/approval-guidelines/) documents PeeringDB’s registration approval process.

## Getting help

* Please log bugs and feature requests at [GitHub](https://github.com/peeringdb/peeringdb/issues).
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

## Quick API start

PeeringDB is available at <https://www.peeringdb.com/> with self-describing API docs at <https://www.peeringdb.com/apidocs/>.  More thorough docs are at [API Specs](api_specs.md), but in a nutshell, just prepend the URL with `api/` to get that object in JSON.

For example:
<https://www.peeringdb.com/net/1>
becomes:
<https://www.peeringdb.com/api/net/1>

List all via API by taking the `id` off:
<https://www.peeringdb.com/api/net>

Local database replication is accomplished with this [command line tool](https://github.com/peeringdb/peeringdb-py), please see the [documentation](http://peeringdb.github.io/peeringdb-py/cli/#sync) for more information.

## Guides in other languages

- [en] [PeeringDB information registration guide and facility presence for NNI's](guide/IX.br - Guide for registering information in PeeringDB-English-Version - 2023.pdf) - Julimar Lunguinho Mendes
- [es] [Guía corta para uso de peeringdb.com](guide/guia_PeeringDB.pdf) - Fabián Mejía
- [es] [Guía de registro de información en PeeringDB y presencia en facilities para NNI's](guide/IX.br - Guia para el registro de informacion en el PeeringDB-Version-Espanol - 2023.pdf) - Julimar Lunguinho Mendes
- [pt-BR] [Guia de cadastro de Carrier no PeeringDB](guide/IX.br - Guia de cadastro de Carrier no PeeringDB-Versao-Portugues - 2025.pdf) - Julimar Lunguinho Mendes
- [pt-BR] [Guia de cadastro de informações no PeeringDB e presença em facility para NNI's](guide/IX.br - Guia de cadastro de informacoes no PeeringDB-Versao-Portugues - 2023.pdf) - Julimar Lunguinho Mendes

## Learn more

* [Release notes and schedule](release_notes/index.md) — upcoming releases, and a summary of what has changed in PeeringDB software releases.
* [Tools](tools.md) — tools developed by PeeringDB users.
* [Presentations](presentations.md) — tutorials, workshops, and presentations given at events around the world.
* [Beta server](https://beta.peeringdb.com/) — runs the latest beta software, with full access over HTTP and the API. Changes made there are local to the beta server only. The [latest changes](https://beta.peeringdb.com/changes) redirects to the GitHub issues documenting them.
* [Source code audit](gov/misc/2018-05-16_Computest_Source_Code_Audit_TPM.pdf) — a Third Party Memo from a full audit of PeeringDB's source code, commissioned in 2018.
* Historical data — MySQL dumps from July 29, 2010 to March 14, 2016 are archived by CAIDA at <http://data.caida.org/datasets/peeringdb-v1/>.

## How you can help

* Check your entries and make sure everything looks correct

* Port any scripts to the new API

* Send us feedback

* Improve these docs

* Add or improve a [translation](translation/)

Thanks for your feedback, we look forward to hearing from you!
