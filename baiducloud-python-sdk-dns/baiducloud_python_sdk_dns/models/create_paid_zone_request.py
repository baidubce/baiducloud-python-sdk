"""
Request entity for CreatePaidZoneRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_dns.models.billing import Billing


class CreatePaidZoneRequest(AbstractModel):
    """
    Request entity for CreatePaidZoneRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, names, product_version, billing, client_token=None):
        """
        Initialize CreatePaidZoneRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param names: 域名的名称。
        :type names: List[str] (required)

        :param product_version: 购买的产品版本，包含：普惠版（“discount”）、企业版（“flagship”）。
        :type product_version: str (required)

        :param billing: billing parameter
        :type billing: Billing (required)
        """
        super().__init__()
        self.client_token = client_token
        self.names = names
        self.product_version = product_version
        self.billing = billing

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.names is not None:
            result['names'] = self.names
        if self.product_version is not None:
            result['productVersion'] = self.product_version
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreatePaidZoneRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('names') is not None:
            self.names = m.get('names')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        return self
