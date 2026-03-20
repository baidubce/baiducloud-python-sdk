"""
Cgw information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Cgw(AbstractModel):
    """
    Cgw
    """

    def __init__(self, cgw_id=None, name=None, ip=None, description=None, created_time=None, updated_time=None):
        """
        Initialize Cgw instance.

        :param cgw_id: 用户网关ID
        :type cgw_id: str (optional)

        :param name: 用户网关名称
        :type name: str (optional)

        :param ip: 用户网关IP
        :type ip: str (optional)

        :param description: 用户网关描述
        :type description: str (optional)

        :param created_time: 用户网关创建时间，北京时间
        :type created_time: str (optional)

        :param updated_time: 用户网关修改时间，北京时间
        :type updated_time: str (optional)
        """
        super().__init__()
        self.cgw_id = cgw_id
        self.name = name
        self.ip = ip
        self.description = description
        self.created_time = created_time
        self.updated_time = updated_time

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.cgw_id is not None:
            result['cgwId'] = self.cgw_id
        if self.name is not None:
            result['name'] = self.name
        if self.ip is not None:
            result['ip'] = self.ip
        if self.description is not None:
            result['description'] = self.description
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Cgw

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cgwId') is not None:
            self.cgw_id = m.get('cgwId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self
