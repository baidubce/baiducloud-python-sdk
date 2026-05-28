"""
Request entity for UpgradeZoneRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_dns.models.billing import Billing


class UpgradeZoneRequest(AbstractModel):
    """
    Request entity for UpgradeZoneRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, action, names, billing, client_token=None):
        """
        Initialize UpgradeZoneRequest request entity.

        :param action: action parameter
        :type action: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param names: 域名的名称。
        :type names: List[str] (required)

        :param billing: billing parameter
        :type billing: Billing (required)
        """
        super().__init__()
        self.action = action
        self.client_token = client_token
        self.names = names
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
        :rtype: UpgradeZoneRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('names') is not None:
            self.names = m.get('names')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        return self
