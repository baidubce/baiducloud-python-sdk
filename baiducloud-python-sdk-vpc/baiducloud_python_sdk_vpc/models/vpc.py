"""
Vpc information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class Vpc(AbstractModel):
    """
    Vpc
    """

    def __init__(
        self,
        vpc_id=None,
        name=None,
        cidr=None,
        ipv6_cidr=None,
        description=None,
        is_default=None,
        relay=None,
        secondary_cidr=None,
        tags=None,
    ):
        """
        Initialize Vpc instance.

        :param vpc_id: VPC的ID
        :type vpc_id: str (optional)

        :param name: 名称
        :type name: str (optional)

        :param cidr: 网段及子网掩码
        :type cidr: str (optional)

        :param ipv6_cidr: VPC的IPv6网段
        :type ipv6_cidr: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param is_default: 是否为默认VPC，true:是，false:否
        :type is_default: bool (optional)

        :param relay: 是否开启VPC中继，true:是，false:否
        :type relay: bool (optional)

        :param secondary_cidr: VPC的辅助网段CIDR列表
        :type secondary_cidr: List[str] (optional)

        :param tags: VPC绑定的标签集合
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.name = name
        self.cidr = cidr
        self.ipv6_cidr = ipv6_cidr
        self.description = description
        self.is_default = is_default
        self.relay = relay
        self.secondary_cidr = secondary_cidr
        self.tags = tags

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
        if self.ipv6_cidr is not None:
            result['ipv6Cidr'] = self.ipv6_cidr
        if self.description is not None:
            result['description'] = self.description
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.relay is not None:
            result['relay'] = self.relay
        if self.secondary_cidr is not None:
            result['secondaryCidr'] = self.secondary_cidr
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Vpc

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
        if m.get('ipv6Cidr') is not None:
            self.ipv6_cidr = m.get('ipv6Cidr')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('relay') is not None:
            self.relay = m.get('relay')
        if m.get('secondaryCidr') is not None:
            self.secondary_cidr = m.get('secondaryCidr')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
