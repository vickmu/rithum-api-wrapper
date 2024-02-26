Clients Factory
===============

The ``ClientsFactory`` class is a factory for creating client objects to interact with various parts of the ChannelAdvisor API, including products, orders, and exports.

Initialization
--------------

To initialize a ``ClientsFactory`` instance, provide the following parameters:

- ``access_token``: Your ChannelAdvisor API access token.
- ``default_profile_id``: The default profile ID for API requests.
- ``secondary_profile_id`` (optional): A secondary profile ID, if applicable.
- ``base_url`` (optional): The base URL for the ChannelAdvisor API. Defaults to "https://api.channeladvisor.com".

.. code-block:: python

    from client_registry import ClientsFactory

    factory = ClientsFactory(
        access_token="your_access_token",
        default_profile_id="your_default_profile_id",
        secondary_profile_id="your_secondary_profile_id"
    )

Accessing Clients
-----------------

.. autoattribute:: ca_api_wrapper.api.client_registry.ClientsFactory.product_client
.. autoattribute:: ca_api_wrapper.api.client_registry.ClientsFactory.order_client
.. autoattribute:: ca_api_wrapper.api.client_registry.ClientsFactory.export_client

Each property returns an instance of the respective client, ready to interact with the ChannelAdvisor API.
