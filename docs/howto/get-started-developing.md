# HOWTO: Get Started with Developing for PeeringDB 

## Technology

We use Python with Django and MySQL. Django manages interaction with the database. We publish all [our code](https://github.com/peeringdb/peeringdb) on GitHub. 

We [have documented](/howto/run_development_container/) how to set up our development environment. 

## What to develop

PeeringDB users can request features and report bugs by creating [issues on GitHub](https://github.com/peeringdb/peeringdb/issues). Review open issues to either find a project you’d like to work on, or to see if there’s an existing issue for the feature you want.

If you want to develop a feature that has not been discussed on GitHub, you should either create an issue or contact us to discuss what you need. You can send a message to [productcom@lists.peeringdb.com](mailto:productcom@lists.peeringdb.com) or contact any of the members of the [Product Committee](/committee/product/).

If you want to develop code for an issue that has achieved consensus on GitHub, we suggest starting with issues labeled as "Good first issue". These are simple issues that will help you get a feel for PeeringDB.

## Style

Before you start developing code look at how similar functions have been implemented. Use the same design as existing functions and develop unit tests for your code. We aim for 80% unit test coverage. You also need to run [black](https://pypi.org/project/black/) on your code before submitting a pull request. We use black to ensure that all of our code has the same formatting. Reusing designs, developing unit tests, and using consistent formatting makes it easier for us to maintain the code over time.

We keep the feature parity between the web interface and the API. A feature added to one needs to be added to the other.

The implementation details documented in issues should be detailed enough to use as documentation for the web interface. Documentation is also needed for the API. The minimum we need for API documentation is an example of how to format the request and a pointer to the document section to update.

## Pull requests

It's good to let us know which issues you are working on when you start work. It's also helpful if you include the issues being fixed in your pull request. Please include "Fixes #issue" for each issue addressed in your pull request. We can then close those issues when we deploy your code.

## What happens next?

When you submit your pull request we will run continuous integration tests on the code. We'll also review it ourselves. We'll report on the output of the tests in comments on the pull request and let you know if you need to make any changes.

## Improving this HOWTO

Please let us know how we could improve this article. Send a mail to the [Outreach Committee](mailto:outreachcom@lists.peeringdb.com).
