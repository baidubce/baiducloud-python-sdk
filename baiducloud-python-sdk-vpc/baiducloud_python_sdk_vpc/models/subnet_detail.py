"""
SubnetDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class SubnetDetail(AbstractModel):
    """
    SubnetDetail
    """

    def __init__(
        self,
        subnet_id=None,
        name=None,
        zone_name=None,
        cidr=None,
        ipv6_cidr=None,
        vpc_id=None,
        subnet_type=None,
        description=None,
        available_ip=None,
        available_unreserved_ip=None,
        created_time=None,
        tags=None,
    ):
        """
        Initialize SubnetDetail instance.

        :param subnet_id: 子网ID
        :type subnet_id: str (optional)

        :param name: 子网名称
        :type name: str (optional)

        :param zone_name: 可用区名称
        :type zone_name: str (optional)

        :param cidr: 子网CIDR
        :type cidr: str (optional)

        :param ipv6_cidr: 子网的IPv6网段
        :type ipv6_cidr: str (optional)

        :param vpc_id: 子网所属VPC的ID
        :type vpc_id: str (optional)

        :param subnet_type: 子网类型，\"BCC”、\"BCC_NAT”、”BBC”
        :type subnet_type: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param available_ip: 子网内可用IP数
        :type available_ip: int (optional)

        :param available_unreserved_ip: 子网内除预留网段外的可用IP数
        :type available_unreserved_ip: int (optional)

        :param created_time: 子网的创建时间
        :type created_time: str (optional)

        :param tags: 子网绑定的标签列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.subnet_id = subnet_id
        self.name = name
        self.zone_name = zone_name
        self.cidr = cidr
        self.ipv6_cidr = ipv6_cidr
        self.vpc_id = vpc_id
        self.subnet_type = subnet_type
        self.description = description
        self.available_ip = available_ip
        self.available_unreserved_ip = available_unreserved_ip
        self.created_time = created_time
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
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.name is not None:
            result['name'] = self.name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.ipv6_cidr is not None:
            result['ipv6Cidr'] = self.ipv6_cidr
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_type is not None:
            result['subnetType'] = self.subnet_type
        if self.description is not None:
            result['description'] = self.description
        if self.available_ip is not None:
            result['availableIp'] = self.available_ip
        if self.available_unreserved_ip is not None:
            result['availableUnreservedIp'] = self.available_unreserved_ip
        if self.created_time is not None:
            result['createdTime'] = self.created_time
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
        :rtype: SubnetDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('ipv6Cidr') is not None:
            self.ipv6_cidr = m.get('ipv6Cidr')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetType') is not None:
            self.subnet_type = m.get('subnetType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('availableIp') is not None:
            self.available_ip = m.get('availableIp')
        if m.get('availableUnreservedIp') is not None:
            self.available_unreserved_ip = m.get('availableUnreservedIp')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
