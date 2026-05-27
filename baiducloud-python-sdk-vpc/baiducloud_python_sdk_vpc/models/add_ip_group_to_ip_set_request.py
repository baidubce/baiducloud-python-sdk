"""
Request entity for AddIpGroupToIpSetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AddIpGroupToIpSetRequest(AbstractModel):
    """
    Request entity for AddIpGroupToIpSetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ip_group_id, ip_set_ids, client_token=None):
        """
        Initialize AddIpGroupToIpSetRequest request entity.

        :param ip_group_id: ip_group_id parameter
        :type ip_group_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip_set_ids: 关联的IP地址组ID，其ipVersion需与指定的IP地址族一致，单次最多指定5个
        :type ip_set_ids: List[str] (required)
        """
        super().__init__()
        self.ip_group_id = ip_group_id
        self.client_token = client_token
        self.ip_set_ids = ip_set_ids

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
        if self.ip_set_ids is not None:
            result['ipSetIds'] = self.ip_set_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddIpGroupToIpSetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipGroupId') is not None:
            self.ip_group_id = m.get('ipGroupId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ipSetIds') is not None:
            self.ip_set_ids = m.get('ipSetIds')
        return self
