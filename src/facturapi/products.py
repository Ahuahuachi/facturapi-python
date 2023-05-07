"""Products API endpoint"""
from typing import List, Union

from .constants import Taxability
from .http import BaseClient
from .models import Product, build_product


class ProductsClient(BaseClient):
    """Products API client"""

    endpoint = "products"

    def create(  # pylint: disable=too-many-arguments
        self,
        description: str,
        product_key: str,
        price: Union[int, float],
        tax_included: bool = True,
        taxes: List[dict] = None,
        unit_key: str = "H87",
        **kwargs,
    ) -> Product:
        """Creates a new product or service in your Facturapi catalog

        Args:
            description (str): Description of the good or service as it will appear on the
                invoice.\n
            product_key (str): Product/service key, from the SAT catalog.\n
            price (Union[int, float]): Price per unit of the good or service.\n
            tax_included (bool, optional): True if all applicable taxes are included in the price.
                False if price does not include taxes. Defaults to True.\n
            taxes (List[dict]): List of taxes to apply to the product. If None, default taxes will
                apply. If empty list (`[]`) product is tax exempt.
                Default:
                ```
                [{
                    "rate": 0.16,
                    "type": "IVA",
                    "factor": "Tasa",
                    "withholding": False
                }]
                ```\n
            unit_key (str, optional): Unit of measure key, from the SAT catalog. Defaults to "H87".
            **kwargs:
                taxability (Union[Taxability, str], optional): Represents whether the good or
                    service is subject to tax or not. Defaults to None.\n
                unit_name (str, optional): Word that represents the unit of measurement of you
                    product. Must be related to the unit key unit_key. Defaults to None.\n
                sku (str, optional): Identifier for internal use designated by the company.
                    Defaults to None.\n

        Returns:
            Product: Created product
        """
        data = {
            "description": description,
            "product_key": product_key,
            "price": price,
            "tax_included": tax_included,
            "unit_key": unit_key,
            **{k: v for k, v in kwargs.items() if k in ["unit_name", "sku"]},
        }

        if taxes is not None:
            data.update({"taxes": taxes})

        taxability = kwargs.get("taxability")
        if isinstance(taxability, Taxability):
            taxability = taxability.value
        if taxability:
            data.update({"taxability": taxability})

        url = self._get_request_url()
        response = self._execute_request("POST", url, json_data=data).json()
        return build_product(response)

    def all(self, search: str = None, page: int = None, limit: int = None) -> dict:
        """Returns a paginated list of all products of an organization or search by parameters
        recieved

        Args:
            search (str, optional): String to search in product description or SKU.
            Defaults to None.
            page (int, optional): Page of the result list. Defaults to None.
            limit (int, optional): Number of maximum quantity of results. Defaults to None.

        Returns:
            dict: Response data
        """
        params = {}
        if search:
            params.update({"q": search})
        if page:
            params.update({"page": page})
        if limit:
            params.update({"limit": limit})

        url = self._get_request_url()
        return self._execute_request("GET", url, params).json()

    def retrieve(self, product_id: str) -> dict:
        """Returns a single product object

        Args:
            product_def retrieve(self, product_id (str): Product ID

        Returns:
            dict: _description_
        """
        url = self._get_request_url([product_id])
        return self._execute_request("GET", url).json()

    def update(self, product_id: str, data: dict) -> dict:
        """Updates an existing product information

        Args:
            product_id (str): ID of the product to update
            data (dict): Product's new data to

        Returns:
            dict: Updated product object
        """
        url = self._get_request_url([product_id])
        return self._execute_request("PUT", url, json_data=data).json()

    def delete(self, product_id: str) -> dict:
        """Deletes the product from your organization

        Args:
            product_id (str): ID of the product to delete

        Returns:
            dict: Deleted product object
        """
        url = self._get_request_url([product_id])
        return self._execute_request("DELETE", url).json()
