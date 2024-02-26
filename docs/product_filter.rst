Product Filter
==============

The ``ProductFilter`` class provides a flexible way to construct filters for querying products. It supports a variety of operators, logical operators, date functions, and math functions to create complex query conditions.

Usage
-----

Initialize the ``ProductFilter`` without any arguments:

.. code-block:: python

    from filters import ProductFilter

    filter = ProductFilter()

Adding Filters
--------------

To add a filter condition, use the ``add_filter`` method specifying the attribute to filter on, the operator, and the value:

.. code-block:: python

    filter.add_filter('price', 'gt', '100')  # price greater than 100

You can chain multiple conditions together, and they will be logically ANDed by default. To use a different logical operator, specify it as the fourth argument:

.. code-block:: python

    filter.add_filter('category', 'eq', 'Electronics', 'or')  # OR condition

Date and Math Functions
-----------------------

The class also supports filtering based on date and math functions:

.. code-block:: python

    filter.add_date_function_filter('year', 'createdDate', '2020')  # items created in 2020
    filter.add_math_function_filter('floor', 'price', '100')  # price rounded down equals 100

Getting the Filter String
-------------------------

Once all conditions are added, retrieve the final filter string with ``get_filter``:

.. code-block:: python

    final_filter = filter.get_filter()
    print(final_filter)

Supported Operators
-------------------

- Comparison: ``lt``, ``le``, ``gt``, ``ge``, ``eq``, ``ne``
- Logical: ``and``, ``or``

Supported Functions
-------------------

- Date: ``year``, ``month``, ``day``, ``hour``, ``minute``, ``second``
- Math: ``floor``, ``ceiling``

