"""
Request entity for UpdateL3AccessGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateL3AccessGroupRequest(AbstractModel):
    """
    Request entity for UpdateL3AccessGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, access_group_name, zone_name, description=None):
        """
        Initialize UpdateL3AccessGroupRequest request entity.

        :param access_group_name: 定位用，不是要改成的新名字。字母开头，可含字母/数字/`.`/`_`/`-`，1~65 字节
        :type access_group_name: str (required)

        :param zone_name: 定位用，可用区名称
        :type zone_name: str (required)

        :param description: 要更新的描述，UTF-8 编码后不超过 1024 字节
        :type description: str (optional)
        """
        super().__init__()
        self.access_group_name = access_group_name
        self.zone_name = zone_name
        self.description = description

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateL3AccessGroupRequest

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
        return self
