# Geographic Search

Where is it? This isn’t just the plaintive cry of someone wondering where the courier has left their package. Finding facilities in PeeringDB has been a big problem. The database did not associate partial and full names in searches, so if a facility owner had entered Montana but you were searching for MT, their facility might not be found. 

As new facilities are created in our database they will be linked to geographic coordinates. Changing the way we record authoritative data for locations in our database means that we will be able to introduce a number of helpful features over the next few months. Over time, we will improve the way existing address data is presented in the database.
![[Maps by Andrew Neel on Unsplash]](images/maps-andrew-neel-unsplash.jpg)
The number of facilities in PeeringDB grew by [about a sixth](images/pdb-infographic-2021.jpg) in 2020. As we add entries with new addresses in 2021 we will normalize the primary presentation of addresses and use them as a search key. We’ll add support for additional searches based on these addresses in the coming months and use this experience to help us clean up the data we already have.

In the future, we will be able to expand the way we provide searches. For instance, we’ll be able to provide a search for facilities with a distance radius of a chosen coordinate. Other innovative searches will be possible and we will prioritize their development based on user feedback.

Tom Paseka, Network Strategy at Cloudflare, says: “*Getting location naming right is hugely important. Having Düsseldorf and Dusseldorf return the same results makes local use of PeeringDB possible, giving more precise data across languages and improving data integrity. This is great!.*” 

If you have an idea to improve PeeringDB you can share it on our [low traffic mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb). If you find a data quality issue, please let us know at <support@peeringdb.com>.

---

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
