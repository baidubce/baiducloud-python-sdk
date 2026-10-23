"""
Request entity for DeleteL3AccessGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteL3AccessGroupRequest(AbstractModel):
    """
    Request entity for DeleteL3AccessGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, access_group_name, zone_name):
        """
        Initialize DeleteL3AccessGroupRequest request entity.

        :param access_group_name: 要删除的权限组名称
        :type access_group_name: str (required)

        :param zone_name: 权限组所属的可用区
        :type zone_name: str (required)
        """
        super().__init__()
        self.access_group_name = access_group_name
        self.zone_name = zone_name

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
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteL3AccessGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self
