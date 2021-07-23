# Advanced Search (Part 2)

We’ve published a couple of [recent](https://docs.peeringdb.com/blog/geographic_search/) [blogs](https://docs.peeringdb.com/blog/advanced_search_1/) about how we are improving search, following feedback on its importance in the [2020 user survey](https://docs.peeringdb.com/blog/peeringdb_2020_survey_2021_roadmap/). Here’s another one!

We introduced two significant improvements in the production release, 2.28.0. 

Our first improvement makes it easier to search based on a partial name. When an organization’s name has two parts, you can now search for just the first part and then select from all the organizations that share that name. Previously, search worked on exact matches. This change makes it easier for users to find the organizations they want.

<iframe width="560" height="315" src="https://www.youtube.com/embed/DMv2S_712bo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Our second improvement allows users to search for facilities within a given radius, using the [Advanced Search](https://www.peeringdb.com/advanced_search) interface. Users can search from a country and city, and select a radius in kilometres or miles. Of course, you can achieve the same results using the API or the web interface, which means you can integrate this feature into your own tools.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/FzOUKhJjRRg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


We hope you find these changes make PeeringDB even more useful to you. We prioritized these improvements because of the feedback we hear in 2020. We run out 2021 user survey in September but we’re open to feedback on how to improve PeeringDB at any time.

If you have an idea to improve PeeringDB you can share it on our [low traffic mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb). If you find a data quality issue, please let us know at <support@peeringdb.com>.

***

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
