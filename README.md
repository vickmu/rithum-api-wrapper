[![Documentation Status](https://readthedocs.org/projects/rithum-api-wrapper/badge/?version=latest)](https://rithum-api-wrapper.readthedocs.io/en/latest/?badge=latest)

# CA API Wrapper

The `ca_api_wrapper` is a Python package that simplifies interacting with the ChannelAdvisor API. It provides a straightforward, object-oriented approach to accessing ChannelAdvisor's features, such as managing products, orders, and exports, making it easier for developers to integrate ChannelAdvisor services into their applications.

## Features

- **Easy Authentication**: Simplify the process of authenticating with the ChannelAdvisor API.
- **Product Management**: Easily list, retrieve, and update product information.
- **Order Processing**: Fetch and update orders with minimal hassle.
- **Export Utilities**: Access export functionalities provided by ChannelAdvisor.
- **Error Handling**: Robust error handling to gracefully manage API exceptions.

## Installation

Install `ca_api_wrapper` using pip:

```bash
pip install ca_api_wrapper
```
### Quick start
Here's a quick example to get you started with the ca_api_wrapper:
```py

from ca_api_wrapper.api.client_registry import ClientsFactory

# User provides their own credentials
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-1234"
default_profile_id = 12345678
secondary_profile_id = 12345679 

factory = ClientsFactory(access_token, default_profile_id, secondary_profile_id)
product_client = factory.product_client

response = product_client.products.get_by_id(11111111)
```

