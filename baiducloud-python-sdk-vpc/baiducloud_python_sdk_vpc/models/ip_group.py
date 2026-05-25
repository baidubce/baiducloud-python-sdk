"""
IpGroup information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IpGroup(AbstractModel):
    """
    IpGroup
    """

    def __init__(
        self, ip_group_id=None, name=None, description=None, ip_version=None, ip_set_ids=None, binded_instance_num=None
    ):
        """
        Initialize IpGroup instance.

        :param ip_group_id: IP地址族的ID
        :type ip_group_id: str (optional)

        :param name: IP地址族的名称
        :type name: str (optional)

        :param description: IP地址族的描述
        :type description: str (optional)

        :param ip_version: ipVersion，取值IPv4或IPv6
        :type ip_version: str (optional)

        :param ip_set_ids: 关联的IP地址组ID列表
        :type ip_set_ids: List[str] (optional)

        :param binded_instance_num: IP地址族绑定实例数量
        :type binded_instance_num: int (optional)
        """
        super().__init__()
        self.ip_group_id = ip_group_id
        self.name = name
        self.description = description
        self.ip_version = ip_version
        self.ip_set_ids = ip_set_ids
        self.binded_instance_num = binded_instance_num

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
        if self.ip_group_id is not None:
            result['ipGroupId'] = self.ip_group_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.ip_set_ids is not None:
            result['ipSetIds'] = self.ip_set_ids
        if self.binded_instance_num is not None:
            result['bindedInstanceNum'] = self.binded_instance_num
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IpGroup

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipGroupId') is not None:
            self.ip_group_id = m.get('ipGroupId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('ipSetIds') is not None:
            self.ip_set_ids = m.get('ipSetIds')
        if m.get('bindedInstanceNum') is not None:
            self.binded_instance_num = m.get('bindedInstanceNum')
        return self
