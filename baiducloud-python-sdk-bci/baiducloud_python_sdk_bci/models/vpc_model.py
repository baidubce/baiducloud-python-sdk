"""
VpcModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VpcModel(AbstractModel):
    """
    VpcModel
    """

    def __init__(self, vpc_id=None, name=None, cidr=None, create_time=None, description=None, is_default=None):
        """
        Initialize VpcModel instance.

        :param vpc_id: vpc Id
        :type vpc_id: str (optional)

        :param name: vpc名称
        :type name: str (optional)

        :param cidr: 网段及子网掩码
        :type cidr: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param description: vpc描述
        :type description: str (optional)

        :param is_default: 是否是默认vpc
        :type is_default: bool (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.name = name
        self.cidr = cidr
        self.create_time = create_time
        self.description = description
        self.is_default = is_default

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
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.name is not None:
            result['name'] = self.name
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VpcModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        return self
