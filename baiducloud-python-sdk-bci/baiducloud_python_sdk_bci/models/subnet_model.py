"""
SubnetModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SubnetModel(AbstractModel):
    """
    SubnetModel
    """

    def __init__(
        self, subnet_id=None, name=None, cidr=None, vpc_id=None, subnet_type=None, description=None, create_time=None
    ):
        """
        Initialize SubnetModel instance.

        :param subnet_id: 子网ID
        :type subnet_id: str (optional)

        :param name: 子网名称
        :type name: str (optional)

        :param cidr: 网段及子网掩码
        :type cidr: str (optional)

        :param vpc_id: vpcID
        :type vpc_id: str (optional)

        :param subnet_type: 子网类型：BCC、BBC、BCC_NAT、BBC_NAT
        :type subnet_type: str (optional)

        :param description: subnet描述
        :type description: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)
        """
        super().__init__()
        self.subnet_id = subnet_id
        self.name = name
        self.cidr = cidr
        self.vpc_id = vpc_id
        self.subnet_type = subnet_type
        self.description = description
        self.create_time = create_time

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
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_type is not None:
            result['subnetType'] = self.subnet_type
        if self.description is not None:
            result['description'] = self.description
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SubnetModel

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
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetType') is not None:
            self.subnet_type = m.get('subnetType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self
