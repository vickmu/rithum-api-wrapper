Order Client
============

The ``OrderClient`` class facilitates interactions with order-related endpoints of the ChannelAdvisor API. It provides methods to list orders, retrieve a specific order by ID, and create new orders.

Initialization
--------------

The client is initialized with an instance of ``ChannelAdvisorClient``:

.. code-block:: python

    from client import ChannelAdvisorClient
    from orders import OrderClient

    ca_client = ChannelAdvisorClient('your_access_token', 'your_default_profile_id')
    order_client = OrderClient(ca_client)

Usage
-----

Listing Orders
--------------

Retrieve a list of orders:

.. code-block:: python

    orders = order_client.list()
    print(orders.json())  # Assuming the response is a JSON object

Advanced Listing Orders W/Filtering & Pagination
------------------------------------------------

Requires a Filter object: 

Example getting a list of Shipped Amazon orders from a specific profile

.. code-block:: python

    order_client = factory.order_client

    order_filter = Filter()
    order_filter.add_filter(attribute="ShippingStatus", operator="eq", value="Shipped")
    order_filter.add_filter(attribute='CreatedDateUtc', operator='ge',value='2024-02-20', quote_value=False )
    
    #list() will combine the responses and return a list List[Dict[str, Any]]
    response = order_client.list(order_filter=order_filter, paginate=True, page_size=250)


Getting an Order by ID
----------------------

Retrieve a specific order by its ID, expanding items details:

.. code-block:: python

    order_id = 12345
    order = order_client.get_by_id(order_id)
    print(order.json())  # Assuming the response is a JSON object

Creating an Order
-----------------

Create a new order by providing order details as a dictionary:

.. code-block:: python

    new_order = {
        "buyerEmailAddress": "buyer@example.com",
        "orderItems": [
            {
                "sku": "SKU123",
                "lineItemID": "123",
                "quantity": 1,
                "price": 10.0
            }
        ],
        "totalPrice": 10.0
    }
    response = order_client.create(new_order)
    print(response.json())  # Assuming the response is successful

Updating an order private notes
-------------------------------

.. code-block:: python

    response = order_client.create_private_note(id=12341, note="hello world")
    print(response.json())  # Assuming the response is successful
