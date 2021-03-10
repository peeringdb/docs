#API Keys
How often does one new feature deliver three important improvements? Adding support for API Keys in this week’s beta release does this. API Keys will help organizations improve the security of the data they publish while linking the tools to the org itself and not its people.
![[Key and Keyboard by Everardo Sanchez on Unsplash]](images/key-keyboard-coffee-everardo-sanchez-550x824.jpg)
API Keys allow organizations to have authenticated access directly associated with the org itself and not with individual users. Organizations will now have better control of their data and won’t need to tie automation to their users’ credentials, which will improve robust continuity of operations should individuals leave the organization.

Organizations previously faced a problem that if a user left, and their PeeringDB account was closed, any update processes that used the user’s account would end. Organizations can now tie automated processes to role accounts, ensuring continuity of operations even when people change.

And if you automate searches to find new peers, your scripts can now be updated to collect contact information as well as other details.

As more organizations use API Keys to automate more of their interactions with PeeringDB, we will get a better idea of who is using the API and who is not. This will allow us to engage with them so we can understand what they value. Of course, this does not mean that we’ll be abandoning users who want to focus on using the web interface. 

Aris Lambrianidis, a senior security engineer with White & Case LLP, says: “*The ability to leverage API keys means that programmatic workflows can work reliably using an authentication and authorization model independently of any credentials assigned to humans. Decoupling these access methods should significantly benefit the security and scalability of such operations.*” 

We have [published some documentation](https://github.com/peeringdb/peeringdb/blob/master/docs/api_keys.md) showing how to generate an API Key, and use that API Key to achieve tasks that will be common to many organizations using PeeringDB. We have also published sample code to help you develop your own automation. Additional examples that others can use are also welcome. Everyone benefits from sharing this kind of code as it means more accurate data quality. 

If you have an idea to improve PeeringDB you can share it on our [low traffic mailing lists](https://docs.peeringdb.com/#mailing-lists) or create an issue directly on [GitHub](https://github.com/peeringdb/peeringdb). If you find a data quality issue, please let us know at <support@peeringdb.com>.

***

PeeringDB is a freely available, user-maintained, database of networks, and the go-to location for interconnection data. The database facilitates the global interconnection of networks at Internet Exchange Points (IXPs), data centers, and other interconnection facilities, and is the first stop in making interconnection decisions.
