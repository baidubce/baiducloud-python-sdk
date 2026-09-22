"""
SubnetInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SubnetInfo(AbstractModel):
    """
    SubnetInfo
    """

    def __init__(self, subnet_id=None, name=None, cidr=None, az=None):
        """
        Initialize SubnetInfo instance.

        :param subnet_id: 子网短ID
        :type subnet_id: str (optional)

        :param name: 子网名称
        :type name: str (optional)

        :param cidr: 子网网段
        :type cidr: str (optional)

        :param az: 子网所在可用区
        :type az: str (optional)
        """
        super().__init__()
        self.subnet_id = subnet_id
        self.name = name
        self.cidr = cidr
        self.az = az

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
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.name is not None:
            result['name'] = self.name
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.az is not None:
            result['az'] = self.az
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SubnetInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('az') is not None:
            self.az = m.get('az')
        return self
