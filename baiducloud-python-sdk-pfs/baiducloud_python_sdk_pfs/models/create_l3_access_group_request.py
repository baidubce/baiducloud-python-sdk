"""
Request entity for CreateL3AccessGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateL3AccessGroupRequest(AbstractModel):
    """
    Request entity for CreateL3AccessGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, access_group_name, zone_name, description=None, source_zone_name=None, source_access_group_name=None
    ):
        """
        Initialize CreateL3AccessGroupRequest request entity.

        :param access_group_name: 权限组名称。字母开头，可含字母/数字/`.`/`_`/`-`，1~65 字节
        :type access_group_name: str (required)

        :param zone_name: 可用区名称
        :type zone_name: str (required)

        :param description: 描述
        :type description: str (optional)

        :param source_zone_name: 复制源可用区，与 sourceAccessGroupName 成对使用
        :type source_zone_name: str (optional)

        :param source_access_group_name: 复制源权限组名，与 sourceZoneName 成对使用
        :type source_access_group_name: str (optional)
        """
        super().__init__()
        self.access_group_name = access_group_name
        self.zone_name = zone_name
        self.description = description
        self.source_zone_name = source_zone_name
        self.source_access_group_name = source_access_group_name

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
        if self.description is not None:
            result['description'] = self.description
        if self.source_zone_name is not None:
            result['sourceZoneName'] = self.source_zone_name
        if self.source_access_group_name is not None:
            result['sourceAccessGroupName'] = self.source_access_group_name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateL3AccessGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('sourceZoneName') is not None:
            self.source_zone_name = m.get('sourceZoneName')
        if m.get('sourceAccessGroupName') is not None:
            self.source_access_group_name = m.get('sourceAccessGroupName')
        return self
