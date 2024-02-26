Channel Advisor Client
======================

The ``ChannelAdvisorClient`` class provides the core functionality for making requests to the ChannelAdvisor API.

Initialization
--------------

The client is initialized with your API credentials and optionally a base URL:

- ``access_token``: Your ChannelAdvisor API access token.
- ``default_profile_id``: The default profile ID for API requests.
- ``secondary_profile_id`` (optional): A secondary profile ID, if applicable.
- ``base_url`` (optional): The base URL for the ChannelAdvisor API. Defaults to "https://api.channeladvisor.com".

.. code-block:: python

    from client import ChannelAdvisorClient

    client = ChannelAdvisorClient(
        access_token="your_access_token",
        default_profile_id="your_default_profile_id",
        secondary_profile_id="your_secondary_profile_id"
    )

Making Requests
---------------

Use the ``make_request`` method to make API requests:

.. .. automethod:: api.client.ChannelAdvisorClient.make_request

This method constructs a request to the specified API endpoint, handling authentication, headers, and other request parameters.
