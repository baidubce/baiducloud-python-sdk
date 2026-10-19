"""
RoleInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RoleInfo(AbstractModel):
    """
    RoleInfo
    """

    def __init__(self, id=None, azone=None, subnet_id=None, name=None, vpc_cidr=None, short_id=None):
        """
        Initialize RoleInfo instance.

        :param id: 节点ID。
        :type id: str (optional)

        :param azone: 可用区名称，多个逗号分隔。
        :type azone: str (optional)

        :param subnet_id: 子网ID，多个逗号分隔。
        :type subnet_id: str (optional)

        :param name: 角色名称。
        :type name: str (optional)

        :param vpc_cidr: VPC地址。
        :type vpc_cidr: str (optional)

        :param short_id: 短ID。
        :type short_id: str (optional)
        """
        super().__init__()
        self.id = id
        self.azone = azone
        self.subnet_id = subnet_id
        self.name = name
        self.vpc_cidr = vpc_cidr
        self.short_id = short_id

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
        if self.id is not None:
            result['id'] = self.id
        if self.azone is not None:
            result['azone'] = self.azone
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.name is not None:
            result['name'] = self.name
        if self.vpc_cidr is not None:
            result['vpcCidr'] = self.vpc_cidr
        if self.short_id is not None:
            result['shortId'] = self.short_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RoleInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('azone') is not None:
            self.azone = m.get('azone')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcCidr') is not None:
            self.vpc_cidr = m.get('vpcCidr')
        if m.get('shortId') is not None:
            self.short_id = m.get('shortId')
        return self
