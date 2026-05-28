"""
Request entity for RenewZoneRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_dns.models.billing_for_renew import BillingForRenew


class RenewZoneRequest(AbstractModel):
    """
    Request entity for RenewZoneRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, action, billing, client_token=None):
        """
        Initialize RenewZoneRequest request entity.

        :param name: name parameter
        :type name: str (required)

        :param action: action parameter
        :type action: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param billing: billing parameter
        :type billing: BillingForRenew (required)
        """
        super().__init__()
        self.name = name
        self.action = action
        self.client_token = client_token
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
        :rtype: RenewZoneRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('billing') is not None:
            self.billing = BillingForRenew().from_dict(m.get('billing'))
        return self
