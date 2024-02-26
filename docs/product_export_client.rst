Product Export Client
=====================

The ``ProductExportClient`` class is designed to handle the export of product data from the ChannelAdvisor platform. It offers methods to initiate data export based on filters and attributes, retrieve export data by token, and manage the export process.

Initialization
--------------

The client is initialized with an instance of ``ChannelAdvisorClient``:

.. code-block:: python

    from .client import ChannelAdvisorClient
    from .exports import ProductExportClient

    client = ChannelAdvisorClient('your_access_token', 'your_default_profile_id')
    export_client = ProductExportClient(client)

This instance provides access to the necessary authentication details and profile ID.

Methods
-------

.. automethod:: ca_api_wrapper.api.exports.ProductExportClient.__init__

get_products
~~~~~~~~~~~~

Retrieve products based on specified filters and attributes:

.. automethod:: ca_api_wrapper.api.exports.ProductExportClient.get_products

get_export_by_token
~~~~~~~~~~~~~~~~~~~

Retrieve export data using a previously acquired token:

.. automethod:: ca_api_wrapper.api.exports.ProductExportClient.get_export_by_token

Private Methods
---------------

Note: These methods are intended for internal use within the class and are not part of the public API.

_generate_export_token
~~~~~~~~~~~~~~~~~~~~~~

Generates an export token based on the provided filters and attributes.

.. automethod:: ca_api_wrapper.api.exports.ProductExportClient._generate_export_token

_get_products_export_data
~~~~~~~~~~~~~~~~~~~~~~~~~

Attempts to retrieve product export data using a token, with retry logic.

.. automethod:: ca_api_wrapper.api.exports.ProductExportClient._get_products_export_data

_get_product_export
~~~~~~~~~~~~~~~~~~~

Performs the actual API call to retrieve product export data.

.. automethod:: ca_api_wrapper.api.exports.ProductExportClient._get_product_export

_download_export_convert_to_df
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Downloads and converts the export data into a pandas DataFrame.

.. automethod:: ca_api_wrapper.api.exports.ProductExportClient._download_export_convert_to_df

_assign_column_name_to_column_value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assigns meaningful names to DataFrame columns based on export data.

.. automethod:: ca_api_wrapper.api.exports.ProductExportClient._assign_column_name_to_column_value

