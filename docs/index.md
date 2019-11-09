# About PeeringDB

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
    Discussion about PeeringDB atechnical topics.

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

## Guides

- [es] [Guía corta para uso de peeringdb.com](guide/guia_PeeringDB.pdf) - Fabián Mejía
- [pt-BR] [Guia de cadastro de informações de ASNs no PeeringDB](guide/PeeringDB_Cadastro_de_ASN.pdf) - Julimar Lunguinho Mendes / Equipe de Engenharia
- [pt-BR] [Guia de cadastro de informações de Facilities no PeeringDB](guide/PeeringDB_Cadastro_de_Facilities.pdf) - Julimar Lunguinho Mendes / Equipe de Engenharia

## Tutorials

- [PeeringDB Workshop](presentation/20190820_PeeringDB_Workshop_1-2_AfPIF_2019.pdf) at [AfPIF-10](https://www.afpif.org/afpif-10/), Balaclava, MV - August 20, 2019 - Arnold Nipper ([video](https://livestream.com/internetsociety/afpif2019/videos/195303661) starts at 14:00)
- PeeringDB Tutorial Workshop [Part 1: Intro](presentation/20190227-peeringdb-workshop-1-intro.pdf), [Part 2: Main](presentation/20190227-peeringdb-workshop-2-main.pdf), [Part 3: API](presentation/20190227-peeringdb-workshop-3-api.pdf) at [APRICOT 2019](https://2019.apricot.net/program/schedule/#/day/10/peeringdb-tutorial), Daejeon, KR - February 27, 2018 - Arnold Nipper ([video](https://www.youtube.com/watch?v=cygDlOqs9tI))

## Presentations

#### 2019

- [PeeringDB Update](presentation/20191107-PeeringAsia3-Arnold-Nipper-V2.pdf) at [Peering Asia 3.0](http://peeringasia.com/), Kuala Lumpur, MY - November 7, 2019 - Arnold Nipper
- [PeeringDB Update](presentation/20191105-ATNOG2019-2-Stefan_Funke.pdf) at [ATNOG 2019/2](https://atnog.at/), Vienna, AT - November 5, 2019 - Stefan Funke
- [Introduction to PeeringDB](presentation/20191105-JBIX-Peering-Forum-Arnold-Nipper-V2.pdf) at [JBIX Peering Forum 2019](http://pf.jbix.my/), Kuala Lumpur, MY - November 5, 2019 - Arnold Nipper
- [Cadastro para participantes do IX.br](presentation/ix-forum-florianopolis-peeringdb.20191025.pdf) at [IX Fórum Regional](https://regional.forum.ix.br/38-SC/), Florianópolis, BR - October 25, 2019 - Julimar Lunguinho Mendes
- [OAuth for IXP Operators](presentation/euroix-201910-euroix35-oauth-for-ixps.pdf) at the [35th Euro-IX Forum](https://www.euro-ix.net/en/events/fora/35th-euro-ix-forum/), Zaandam, NL - October 21, 2019 - Barry O'Donovan
- [The PeeringDB API](presentation/20191021-API-EuroIX35-Arnold-Nipper.pdf) at the [35th Euro-IX Forum](https://www.euro-ix.net/en/events/fora/35th-euro-ix-forum/), Zaandam, NL - October 21, 2019 - Arnold Nipper
- [Introduction to PeeringDB](presentation/20191001-RONOG6-Arnold-Nipper.pdf) at [RONOG 6](https://www.ronog.ro/), Bucharest, RO - October 1, 2019 - Arnold Nipper
- [PeeringDB Update](presentation/PeeringDBUpdate_EPF2019.pdf) at [EPF14](https://www.peering-forum.eu/agenda?year=2019), Tallinn, EE - September 18, 2019 - Filiz Yilmaz
- [Cadastro para participantes do IX.br](presentation/ix-forum-natal-peeringdb.20190906.pdf) at [IX Fórum Regional](https://regional.forum.ix.br/36-RN/), Natal, BR - September 6, 2019 - Julimar Lunguinho Mendes
- [Introduction to PeeringDB](presentation/20190828-SAFNOG5-Arnold-Nipper.pdf) at [SAFNOG-5](http://www.safnog.org/), Johannesburg, ZA - August 28, 2019 - Arnold Nipper
- [Introduction to PeeringDB](presentation/20190822-AfPIF2019-Arnold-Nipper.pdf) at [AfPIF-10](https://www.afpif.org/afpif-10/), Balaclava, MV - August 22, 2019 - Arnold Nipper
- [Introducción a PeeringDB](presentation/20190814-MexNOG2-peeringdb-intro-Spanish.pdf) at [MexNOG 2019](http://www.mexnog.org.mx/), Mexico City, MX - August 14, 2019 - Diego Dominguez
- [Introduction to PeeringDB](presentation/20190716-ATNOG2019-1-Arnold-Nipper.pdf) at [ATNOG 2019/1](https://atnog.at/), Salzburg, AT - July 16, 2019 - Arnold Nipper
- [Introduction to PeeringDB](presentation/20190701-INNOG2-Arnold-Nipper.pdf) at [INNOG 2](https://www.innog.net/innog-2/program/conference/), New Delhi, IN - July 1, 2019 - Arnold Nipper ([video](https://www.youtube.com/watch?v=BsSkPIQEtz8))
- [Cadastro para participantes do IX.br](presentation/ix-forum-saopaulo-peeringdb.20190610.pdf) at [IX Fórum Regional](https://regional.forum.ix.br/31-SP/), São Paulo, BR - June 10, 2019 - Julimar Lunguinho Mendes
- [News from PeeringDB](presentation/20190603-ENOG16-Arnold-Nipper.pdf) at [ENOG 16](https://www.enog.org/enog-16/), Tbilisi, GE - June 3, 2019 - Arnold Nipper
- [PeeringDB Update](presentation/20190527-NONOG3-Arnold-Nipper.pdf) at [NONOG-3](https://www.nonog.net/nonog-3/), Oslo, NO - May 27, 2019 - Arnold Nipper
- [PeeringDB Update](presentation/20190514-SINOG6-Arnold-Nipper.pdf) at [SINOG 6.0](https://www.sinog.si/sinog/sinog6/en/), Ljubljana, SI - May 14, 2019 - Arnold Nipper
- [Introduction to PeeringDB](presentation/20190507-BKNIX-Peeringforum-Arnold-Nipper.pdf) at [BKNIX Peering Forum and ThaiNOG Day 2019](https://peeringforum.bknix.co.th/2019/), Bangkok, TH - May 7, 2019 - Arnold Nipper
- [Use in Latin America](presentation/LAC-Peering-Forum-2019-Punta_Cana-PeeringDB.20190506.pdf) at [Peering Forum LAC](http://peeringforum.lat/), Punta Cana, DR - May 6, 2019 - Julimar Lunguinho Mendes and Carlos Martinez Cagnazzo
- [Cadastro para participantes do IX.br](presentation/ix-forum-campogrande-peeringdb.20190416.pdf) at [IX Fórum Regional](https://regional.forum.ix.br/29-MS/), Campo Grande, BR - April 26, 2019 - Julimar Lunguinho Mendes
- [Introduction to PeeringDB](presentation/20190419-TelecomDay-Arnold-Nipper.pdf) at [Telecom Day](http://telecomday.ru/en/programm/), St. Petersburg, RU - April 19, 2019 - Arnold Nipper
- [PeeringDB Update](presentation/20190417-SEE8-Arnold-Nipper.pdf) at [SEE 8](https://www.ripe.net/participate/meetings/regional-meetings/see/see-8), Sarajevo, BH - April 17, 2019 - Arnold Nipper
- [PeeringDB Update](presentation/20190405-PeeringDB-Update-Curso-IPv6.pdf) at [Curso Avançado de IPv6](https://cursoseventos.nic.br/curso/curso-avancado-ipv6/), São Paulo, BR - April 5, 2019 - Julimar Lunguinho Mendes
- [PeeringDB Update](presentation/20190404-BCIX-1-Roundtable-Stefan-Funke.pdf) at [BCIX Round Table April 2019](https://www.facebook.com/events/2386787348000284/), Berlin, DE - April 4, 2019 - Stefan Funke
- [PeeringDB Update](presentation/20190403-MENOG19-Arnold-Nipper-V2.pdf) at [MENOG 19](https://www.menog.org/meetings/menog-19/), Beirut, LB - April 3, 2019 - Arnold Nipper
- [PeeringDB Update](presentation/20190315-DKNOG9-Arnold-Nipper-V2.pdf) at [DKNOG9](https://events.dknog.dk/event/4/contributions/), Copenhagen, DK - March 15, 2019 - Arnold Nipper
- [PeeringDB Update](presentation/20190312-PeeringDays2019-Arnold-Nipper.pdf) at [Peering Days 2019](https://peeringdays.eu/programme/), Zagreb, CR - March 12, 2019 - Arnold Nipper
- [PeeringDB Update](presentation/20190306-PhNOG2019-Arnold-Nipper-V2.pdf) at [PhNOG 2019](http://phnog.com/phnog-2019-cebu-details/), Cebu, PH - March 8, 2019 - Arnold Nipper
- [PeeringDB Update](presentation/20190301-HKNOG70-Arnold-Nipper-V2.pdf) at [HKNOG 7.0](https://hknog.net/hknog-7-0/), Hong Kong, HK - March 1, 2019 - Arnold Nipper

#### 2018

- [PeeringDB Update](presentation/20181123-MSK-IX-Peering-Forum-2018-Stanic.pdf) at [MSK-IX Peering Forum 2018](https://peering-forum.ru/en/), Moscow, RU - November 23, 2018 - Rebecca Stanić
- [PeeringDB Update](presentation/20181121-DENOG10-Nipper.pdf) at [DENOG10](https://www.denog.de/de/meetings/denog10/denog10.html), Darmstadt, DE - November 21, 2018 - Arnold Nipper
- [PeeringDB Update](presentation/20181109-ITNOG4-Nipper.pdf) at [ITNOG4](https://www.itnog.it/itnog4/), Bologna, IT - November 9, 2018 - Arnold Nipper
- [Introduction to PeeringDB API](presentation/20181104-EuroIX33-Lightning-Introduction-to-PeeringDB-API-Nipper.pdf) at the [33rd Euro-IX Forum](https://www.euro-ix.net/), Venice, IT - November 6, 2018 - Arnold Nipper
- [PeeringDB Introduction](presentation/20181031-ngNOG-PeeringDB.pdf) at [ngNOG 2018](https://nog.ng/), Lagos, NG - October 31, 2018 - Ben Ryall
- [PeeringDB Update](presentation/20181030-SwiNOG34-Nipper.pdf) at [SwiNOG #34](https://www.swinog.ch/meetings/swinog34/), Berne, CH - October 30, 2018 - Arnold Nipper
- [PeeringDB Update and Japanese Localization Experience](presentation/20181025-PeeringAsia20-Nipper.pdf) at [Peering Asia 2.0](https://www.peeringasia.com/), Hong Kong, HK - October 25, 2018 - Arnold Nipper and Masataka Mawatari
- [PeeringDB Update](presentation/20180924-SAFNOG-4-Nipper.pdf) at [SAFNOG-4/EANOG/tzNOG](http://www.safnog.org/), Dar es Salaam, TZ - September 25, 2018 - Arnold Nipper
- [PeeringDB Update](presentation/20180918-EPF13-Stanic.pdf) at [EPF 13](https://www.peering-forum.eu/), Athens, GR - September 18, 2018 - Rebecca Stanić
- [Cadastro para participantes do IX.br](presentation/Ix-forum-natal-peeringdb.20180914.pdf) at [IX (PTT) Fórum Regional](https://regional.forum.ix.br/24-RN/), Natal, BR - September 14, 2018 - Julimar Lunguinho Mendes
- [PeeringDB Frontend Translation Project](presentation/20180907_apnic46_peeringdb_i18n_mawatari.pdf) at [APNIC 46](https://conference.apnic.net/46/), Noumea, NC - September 12, 2018 - Masataka Mawatari
- [PeeringDB Update](presentation/20180821-AfPIF2018-Nipper.pdf) at [AfPIF2018](https://www.afpif.org/afpif2018/), Cape Town, ZA - August 23, 2018 - Arnold Nipper
- [PeeringDB for IXes](presentation/20180820-AF-IX@AfPIF2018-Nipper.pdf) at [AFIX](https://www.af-ix.net/), Cape Town, ZA - August 20, 2018 - Arnold Nipper
- [Introduction to PeeringDB API](presentation/20180810-SANOG32-Lightning-Introduction-to-PeeringDB-API-Nipper.pdf) at [SANOG 32](http://www.sanog.org/sanog32/), Dhaka, BD - August 10, 2018 - Arnold Nipper
- [PeeringDB Update](presentation/20180809-SANOG32-Update-Nipper.pdf) at [SANOG 32](http://www.sanog.org/sanog32/), Dhaka, BD - August 9, 2018 - Arnold Nipper
- [PeeringDB: What is it, how to and benefits](presentation/20180622-NEPF-Gilmore.pdf) at [New England Peering Forum 2018](http://nepeeringforum.org/), Cambridge, MA, US - June 22, 2018 - Patrick W. Gilmore
- [PeeringDB Update](presentation/20180619-SEE7-Lightning-Nipper.pdf) at [SEE 7](https://www.ripe.net/participate/meetings/regional-meetings/see/see-7), Timișoara, R0 - June 18, 2018 - Arnold Nipper
- [PeeringDB Update](presentation/20180605-ENOG15-Nipper-V2.pdf) at [ENOG 15](https://www.enog.org/enog-15/programme/agenda/), Moscow, RU - June 5, 2018 - Arnold Nipper
- [PeeringDB Update](presentation/20180524-SwiNOG-33-Lightning-Nipper-V2.pdf) at [SwiNOG 33](http://www.swinog.ch/meetings/swinog33/index.asp), Berne, CH - May 24, 2018 - Arnold Nipper
- [PeeringDB Update e cadastro de Facilities](presentation/gter45-peeringdb.20180515.pdf) at [GTER 45](http://gtergts.nic.br/), Florianópolis, BR - May 22, 2018 - Julimar Lunguinho Mendes ([video](https://www.youtube.com/watch?v=WgACfvJ-HFY))
- [PeeringDB Update](presentation/20180516-RIPE76-Lightning-Nipper-V2.pdf) at [RIPE 76 Connect Working Group](https://ripe76.ripe.net/programme/meeting-plan/connect-wg/), Marseille, FR - May 16, 2018 - Arnold Nipper ([video](https://ripe76.ripe.net/archives/video/49))
- [PeeringDB Update](presentation/20180508-AIS2018-Nipper-v2.pdf) at [African Internet Summit 2018](https://internetsummitafrica.org/), Dakar, SN - May 8, 2018 - Arnold Nipper
- [PeeringDB Update](presentation/20180309-DKNOG8-Lightning-Nipper.pdf) at [DKNOG8](https://dknog8.dknog.dk/), Copenhagen, DK - March 9, 2018 - Arnold Nipper
- [PeeringDB Update](presentation/20180307-CEE-Peering-Days-Lightning-Nipper.pdf) at [CEE Peering Days 2018](https://2018.peeringdays.eu/programme.php), Berlin, DE - March 7, 2018 - Arnold Nipper
- [Introduction to PeeringDB](presentation/20180226-Apricot2018-Nipper.pdf) at [APRICOT 2018](https://2018.apricot.net/program/schedule/#/day/8/peering-and-interconnection-ii-global), Kathmandu, NP - February 26, 2018 - Arnold Nipper
- [PeeringDB Update](presentation/20180224-17th-APIX-Nipper.pdf) at [APIX Meeting #17](http://apix.asia/?page_id=75), Kathmandu, NP - February 24, 2018 - Arnold Nipper
- [PeeringDB Introduction](presentation/20180208-Capacity-India-and-SAARC-Nipper.pdf) at [Capacity India & SAARC 2018](http://www.capacityconferences.com/India-Connect-Agenda), New Delhi, IN - February 8, 2018 - Arnold Nipper

#### 2017

- [PeeringDB Update](presentation/20171114-alnof-sanghani.pdf) at [NIX.cz Member Meering](https://www.nix.cz/), Prague, CZ - November 23, 2017 - Bijal Sanghani
- [PeeringDB Update](presentation/20171123-DENOG9-nipper.pdf) at [DENOG9](http://www.denog.de/de/meetings/denog9/agenda.html), Darmstadt, DE - November 23, 2017 - Arnold Nipper
- [PeeringDB Update](presentation/20171114-alnof-sanghani.pdf) at [ALNOF](https://alnof.namex.it/), Tirana, AL - November 14, 2017 - Bijal Sanghani
- [PeeringDB Update](presentation/20171101-Peering-Asia-nipper.pdf) at [Peering Asia 1.0](http://peeringasia.com/), Kyoto, JP - November 1, 2017 - Arnold Nipper
- [PeeringDB Update](presentation/20170926-topix-meeting-sanghani.pdf) at [TOP-IX Meeting](https://www.top-ix.org/en/2017/07/31/104342/), Torino, IT - September 26, 2017 - Bijal Sanghani
- [PeeringDB Update](presentation/20170915-Neutral-Peering-Day-2017-nipper.pdf) at [NPD 17](https://neutralpeeringdays.net/#Program), The Hague, NL - September 15, 2017 - Arnold Nipper
- [PeeringDB Update](presentation/20170906-SAFNOG-3-nipper.pdf) at [SAFNOG-3](http://www.safnog.org/safnog-3-with-iweek-in-durban), Durban, ZA - September 6, 2017 - Arnold Nipper
- [PeeringDB Update](presentation/20170824-AfPIF2017-nipper.pdf) at [AfPIF 2017](http://www.internetsociety.org/afpif/2017/), Abidjan, CI - August 24, 2017 - Arnold Nipper
- [PeeringDB Update](presentation/20170710-SANOG30-nipper.pdf) at [SANOG 30](http://www.sanog.org/sanog30/program.html) Peering Forum, Gurgaon, IN - July 10, 2017 - Arnold Nipper
- [More benefits from PeeringDB](presentation/20170622-decix-technical-meeting-nipper-v2.pdf) at [DE-CIX Technical Meeting](https://www.de-cix.net/en/news-events/events/de-cix-technical-meeting), Frankfurt, DE - June 22, 2017 - Arnold Nipper
- [PeeringDB Update](presentation/20170605-nanog-70-hughes-peeringdb.pdf) at [NANOG 70](https://www.nanog.org/meetings/nanog70/home), Bellevue, WA, US - June 5, 2017 - Aaron Hughes
- [PeeringDB Update](presentation/20170602-bosnog-mcmanus.pdf) at [BOSNOG Meeting & IX Peering Forum](https://www.meetup.com/BOSNOG-The-Boston-Network-Operators-Group/events/239045101/), Cambridge, MA, US - June 2, 2017 - Stephen McManus
- [Orientações no preenchimento de participantes do IX.br](presentation/gter43-peeringdb.20170522.pdf) at [GTER 43](http://gtergts.nic.br/), Foz do Iguaçu, BR - May 25, 2017 - Julimar Lunguinho Mendes
- [PeeringDB Update](presentation/20170523-ENOG13-Nipper.pdf) at [ENOG 13.0](https://www.enog.org/enog-13/), Saint Petersburg, RU - May 23, 2017 - Arnold Nipper
- [PeeringDB Update](presentation/20170426-gpf-12.0-hughes-peeringdb.pdf) at [Global Peering Forum 12.0](https://www.peeringforum.com/gpf-12-0-peeringdb-update/), New York, NY, US - April 26, 2017 - Aaron Huges
- [PeeringDB](presentation/20170406-ESNOG19-Nipper.pdf) at [GORE/ESNOG Reunion 19](http://www.esnog.net/2017/01/goreesnog-reunion-19-csuccatnix-barcelona/), Barcelona, ES - April 6, 2017 - Arnold Nipper
- [PeeringDB](presentation/20170323-CEE-Peeringdays-Nipper.pdf) at [CEE Peering Days 2017](https://2017.peeringdays.eu/programme.php), Ljubljana, SL - March 23, 2017 - Arnold Nipper
- [PeeringDB 2.0](presentation/20170228-Apricot2017-Nipper.pdf) at [APRICOT 2017](https://2017.apricot.net/), Ho Chi Minh City, VN - February 28, 2017 - Arnold Nipper

#### 2016

- [PeeringDB](presentation/2016-11-23-kikeautumn16-2.pdf) at [19 KIKE Conference](http://kikeevents.com/en/category/19-kike-conference/), Serock, PL - November 23, 2016 - Robert Jakub
- [PeeringDB 2.0](presentation/20161103-ITNOG2-Nipper-peeringdb.pdf) at [ITNOG2](http://www.itnog.it/itnog2/), Bologna, IT - November 3, 2016 - Arnold Nipper
- [PeeringDB Product Committee Charter Survey](presentation/20160919-epf11-Loos-peeringdb.pdf) at [EPF 11](https://www.peering-forum.eu/), Sofia, BG - September 20, 2016 - Eric Loos
- [PeeringDB 2.0](presentation/20160916-npd16-Wollny-peeringdb.pdf) at [NPD 16](http://www.neutralpeeringdays.net/), The Hague, NL - September 16, 2016 - Walt Wollny
- [PeeringDB 2.0](presentation/2016-08-30_afpif2016-Nipper-peeringdb.pdf) at [AfPIF 2016](https://www.internetsociety.org/afpif-2016/), Dar es Salaam, TZ - August 30, 2016 - Arnold Nipper
- [PeeringDB 2.0 for IXPs](presentation/2016-08-29_afix2016-Nipper-peeringdb.pdf) at [AFIX 2016](http://www.af-ix.net/?q=resources/2016/08/afix-2016-meeting-agenda), Dar es Salaam, TZ - August 29, 2016 - Arnold Nipper
- [PeeringDB 2.0](presentation/2016-06-07_PeeringDB-2.0_ENOG11.pdf) at [ENOG 11](https://www.enog.org/meetings/enog-11/), Moscow, RU - June 7, 2016 - Arnold Nipper
- [PeeringDB 2.0](presentation/2016-05-25_81-ripe-72-peeringdb.pdf) at [RIPE 72](https://ripe72.ripe.net/), Copenhagen, DK - May 25, 2016 - Greg Hankins
- [PeeringDB 2.0](presentation/2016-05-12_chi-nog-06-peeringdb.pdf) at [CHI-NOG 06](http://chinog.org/meetings/chi-nog-06/), Chicago, IL, US - May 12, 2016 - Matt Griswold
- [PeeringDB 2.0 e o Cenário Brasileiro](presentation/2016-05-12_PeeringDB-2.0_GTER_41.pdf) and [IX.br Guia de cadastro de informações de ASNs no PeeringDB](presentation/2016-05-12_IX.br_PeeringDB_Guide.pdf) at [GTER 41](http://gtergts.nic.br/), Uberlândia, BR - May 12, 2016 - Eduardo Ascenço Reis
- [PeeringDB 2.0 for IXPs](presentation/2016-04-26_PeeringDB_28th_Euro-IX_Forum.pdf) at [28th Euro-IX Forum](https://www.euro-ix.net/), Luxembourg, LU - April 26, 2016 - Greg Hankins / Arnold Nipper
- [RIPE SEE 5](https://www.ripe.net/participate/meetings/regional-meetings/see-5), Tirana, AL - April 19, 2016 - Arnold Nipper
- [PeeringDB 2.0](presentation/2016-04-21_PeeringDB_UKNOF34.pdf) at [UKNOF34](https://indico.uknof.org.uk/conferenceDisplay.py?confId=36), Manchester, UK - April 21, 2016 - Greg Hankins
- [PeeringDB Update](presentation/2016-04-13_PeeringTrack-PDB-Update-GPF11.pdf) at [GPF 11](https://www.peeringforum.com/), Los Angeles, CA, US - April 13, 2016 - Aaron Hughes
- [NetNod](http://www.netnod.se/netnod-spring-meeting-2016), Stockholm, SE - March 17, 2016 - Job Snijders
- [DKNOG6](http://www.dknog.dk/events/dknog6/), Copenhagen, DK - March 10, 2016 - Job Snijders
- [PeeringDB Update](presentation/PeeringTrack-PDB-Update-20160205.pdf) - Aaron Hughes
    - [APRICOT 2016](https://2016.apricot.net/), Auckland, NZ - February 23, 2016 - Aaron Hughes
    - [NANOG 66](http://nanog.org/meetings/nanog66/home), San Diego, CA, US - February 10, 2016 - Aaron Hughes
- [PeeringDB Version 2 Coding Introduction](presentation/PeeringDB_Version_2-Coding_Introduction.pdf) at [NANOG 66](http://nanog.org/meetings/nanog66/home), San Diego, CA, US - February 8, 2016 - Matt Griswold

#### 2015

- [PeeringDB Version 2 Brazil](presentation/PeeringDB_Version_2-Brazil.pdf) - Matt Griswold / Greg Hankins
    - [IX (PTT) Fórum 9](http://ix.br/pttforum/9/index-en.html), São Paulo, BR - December 8, 2015 - Greg Hankins
- [PeeringDB Version 2 Introduction](presentation/PeeringDB_Version_2-Introduction.pdf) - Matt Griswold
    - [27th Euro-IX Forum](https://www.euro-ix.net/news-and-events/euro-ix-forum/), Berlin, DE - October 26, 2015 - Greg Hankins
    - [DENOG7](http://www.denog.de/meetings/denog7/?lang=en), Darmstadt, DE - October 30, 2015 - Arnold Nipper 

## Tools

This section lists tools for using PeeringDB, and tools that use PeeringDB.

* [django-peeringdb](http://peeringdb.github.io/django-peeringdb/) is a Django library with a local PeeringDB database sync.  It defines the database schema to create a local database copy.  The library is easy to integrate into a common framework for local tools and custom interfaces, and also supports multiple database engines (MySQL, Postgres, SQLite).

* The [Isolario project](https://www.isolario.it/index.php) improve knowledge about the AS-level ecosystem of the Internet by increasing the amount of Autonomous Systems (ASes) from which BGP data is collected. Isolario offers network operators services based on the real-time analysis of inter-domain routing from different points of view in return for full routing tables.

* [Ixgen](https://github.com/ipcjk/ixgen/blob/master/Readme.md) is yet another open source, multiplatform peering configuration generator that is based on the PeeringDB API.  It can also run its own server for faster results.  Ixgen is configured using an INI- or JSON-style format, and produces custom template-driven or fixed JSON-style configurations,

* [peeringdb-py](http://peeringdb.github.io/peeringdb-py/) is a Python client for PeeringDB.  It features functions to get objects and display them in JSON or YAML format, and provides a whois-like display of records.  The client also has an integrated local database sync, and provides a Python library for integration with custom tools.  [Some examples](https://github.com/grizz/pdb-examples) are available too.

* [Pinder](http://github.com/dotwaffle/pinder) is a tool that facilitates peering.  If peering is desired between two networks, and you're happy to just configure sessions without a commercial agreement, Pinder acts as the middle man.  You can submit the request via either a basic web UI or an API, and the other network is notified or can periodically check their outstanding requests.  If both network agree to peer, they are notified to configure a session.  Once both networks indicate that sessions are configured and established, the request is then deleted. [A brief slide deck](http://accel.waffle.sexy/pinder.pdf) explains the functionality in more detail.

* [Search in PeeringDB](https://chrome.google.com/webstore/detail/search-in-peeringdb/aogffgldgfjelpadabfbcngmndbceiad?fbclid=IwAR1F_kOMgFe1lHC-lPVaTEQzNSGmqUhlmIzPPVFDrHH6FhvytQJFW1NRvOE) is a Chrome extension to search for ASNs, networks, and IXs in PeeringDB using the context menu.
* [TraceMON](https://labs.ripe.net/Members/massimo_candela/tracemon-traceroute-visualisation-network-debugging-tool) is a tool for visualizing a network topology generated by traceroutes that provides one-click access to IXP and network information.  It also displays PeeringDB information and allows the user to update their record.  RIPE Atlas users can access it by selecting a [traceroute measurement](https://atlas.ripe.net/measurements/?search=&status=&af=&kind=2%2C4&age=#!tab-public) and clicking on the TraceMON tab.

## Open source

#### Source code audit

PeeringDB commissioned a full audit of PeeringDB's source code in 2018. [Computest](https://www.computest.nl/) (the auditor) prepared a __Third Pary Memo__, this memo provides a high level overview of the outcome of the source code audit. The report is available [here](gov/misc/2018-05-16_Computest_Source_Code_Audit_TPM.pdf).

## Beta development

* The [PeeringDB beta server](https://beta.peeringdb.com/) is running the latest beta software version, with full access over HTTP and the API.  Note that changes made to the beta database are local to the beta server only, and are not reflected on the production servers.

* The [latest changes to PeeringDB](https://beta.peeringdb.com/changes) automagically redirects to the list of issues on PeeringDB's GitHub repository that document all of the changes in the current beta version.

## Historical data

* The PeeringDB 1.0 MySQL interface is gone.  The last available MySQL dump is archived at <https://www.peeringdb.com/v1/final_export.sql>.
* MySQL dumps from July, 29 2010 to March 14, 2016 are archived by CAIDA at <http://data.caida.org/datasets/peeringdb-v1/>.

## How you can help

* Check your entries and make sure everything looks correct

* Port any scripts to the new API

* Send us feedback

* Improve these docs

* Add or improve a [translation](translation/)

Thanks for your feedback, we look forward to hearing from you!
