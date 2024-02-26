Product Client
==============

The ``ProductClient`` class is designed to interact with product-related endpoints of the ChannelAdvisor API. It simplifies the process of listing products, fetching products by SKU or UPC, and managing product attributes.

Initialization
--------------

The client is initialized with an instance of ``ChannelAdvisorClient``:

.. code-block:: python

    from client import ChannelAdvisorClient
    from products import ProductClient

    ca_client = ChannelAdvisorClient('your_access_token', 'your_default_profile_id')
    product_client = ProductClient(ca_client)

Usage
-----

Products Endpoint
-----------------

.. code-block:: python

    # List all products
    products = product_client.products.list()
    print(products.json())

    # Get a product by SKU
    sku = "SKU123"
    product = product_client.products.get_by_sku(sku)
    print(product.json())

    # Get a product by UPC
    upc = "0123456789012"
    product = product_client.products.get_by_upc(upc)
    print(product.json())

Attributes Endpoint
-------------------

.. code-block:: python

    # Get attributes for a product by ID
    product_id = 12345
    attributes = product
