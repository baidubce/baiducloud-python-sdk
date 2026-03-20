"""
IpReserve information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IpReserve(AbstractModel):
    """
    IpReserve
    """

    def __init__(
        self,
        ip_reserve_id=None,
        subnet_id=None,
        ip_cidr=None,
        ip_version=None,
        description=None,
        created_time=None,
        updated_time=None,
    ):
        """
        Initialize IpReserve instance.

        :param ip_reserve_id: 预留网段的ID
        :type ip_reserve_id: str (optional)

        :param subnet_id: 预留网段所在的子网ID
        :type subnet_id: str (optional)

        :param ip_cidr: 预留网段的IP或CIDR
        :type ip_cidr: str (optional)

        :param ip_version: 预留网段的IP版本
        :type ip_version: str (optional)

        :param description: 预留网段的描述
        :type description: str (optional)

        :param created_time: 预留网段实例创建时间
        :type created_time: str (optional)

        :param updated_time: 预留网段实例更新时间
        :type updated_time: str (optional)
        """
        super().__init__()
        self.ip_reserve_id = ip_reserve_id
        self.subnet_id = subnet_id
        self.ip_cidr = ip_cidr
        self.ip_version = ip_version
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
        if self.ip_reserve_id is not None:
            result['ipReserveId'] = self.ip_reserve_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.ip_cidr is not None:
            result['ipCidr'] = self.ip_cidr
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
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
        :rtype: IpReserve

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipReserveId') is not None:
            self.ip_reserve_id = m.get('ipReserveId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('ipCidr') is not None:
            self.ip_cidr = m.get('ipCidr')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self
