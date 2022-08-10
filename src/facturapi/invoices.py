"""Invoices API endpoint"""
from datetime import datetime
from typing import Union

from .enums import CancelationReason
from .http import BaseClient


class InvoicesClient(BaseClient):
    """Products API client"""

    endpoint = "invoices"

    def create(self, data: dict) -> dict:
        """Creates a new invoice

        Args:
            data (dict): Invoice data

        Returns:
            dict: Created invoice object
        """
        url = self._get_request_url()
        return self._execute_request("POST", url, json_data=data)

    def all(
        self,
        search: str = None,
        customer_id: str = None,
        start_date: datetime = None,
        end_date: datetime = None,
        page: int = None,
        limit: int = None,
    ) -> dict:
        """Returns a paginated list of all invoices in an organization
        or makes a search acording to parameters

        Args:
            search (str, optional): Text to search on the invoice. Defaults to None.
            customer_id (str, optional): Id of the customer. Useful to get invoices issued to a
            single customer. Defaults to None.
            start_date (datetime, optional): Lower limit of a date range. Defaults to None.
            end_date (datetime, optional): Upper limit of a date range. Defaults to None.
            page (int, optional): Result page to return, beginning with 1. Defaults to None.
            limit (int, optional): Number from 1 to 50 representing the maximum quantity of
            results to return. Used for pagination. Defaults to None.

        Returns:
            dict: _description_
        """
        params = {}
        if search:
            params.update({"q": search})

        if customer_id:
            params.update({"customer": customer_id})

        if start_date:
            params.update({"date[gt]": start_date.astimezone().isoformat()})

        if end_date:
            params.update({"date[lt]": end_date.astimezone().isoformat()})

        if page:
            params.update({"page": page})

        if limit:
            params.update({"limit": limit})

        url = self._get_request_url()
        return self._execute_request("GET", url, params)

    def retrieve(self, invoice_id: str) -> dict:
        """Retrieves a single invoice object

        Args:
            invoice_id (str): ID of the invoice to retrieve

        Returns:
            dict: Invoice object
        """
        url = self._get_request_url([invoice_id])
        return self._execute_request("GET", url)

    def cancel(
        self,
        invoice_id: str,
        reason: Union[CancelationReason, str],
        substitution: str = None,
    ) -> dict:
        """Cancels an invoice. The invoice will not be valid anymore and will
        change its status to canceled

        Args:
            invoice_id (str): Invoice ID to cancel
            reason (CancelationReason): Reason for cancellation
            substitution (str, optional): Substitute invoice id. Defaults to None.

        Returns:
            dict: Cancelled invoice object
        """
        params = {}
        if reason:
            params.update({"motive": reason.value})

        if substitution:
            params.update({"substitution": substitution})

        url = self._get_request_url([invoice_id])
        return self._execute_request("DELETE", url, query_params=params)
