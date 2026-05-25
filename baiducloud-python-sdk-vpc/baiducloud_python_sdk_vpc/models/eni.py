"""
Eni information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.private_ip import PrivateIP

from baiducloud_python_sdk_vpc.models.private_ip import PrivateIP

from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class Eni(AbstractModel):
    """
    Eni
    """

    def __init__(
        self,
        eni_id=None,
        name=None,
        zone_name=None,
        description=None,
        instance_id=None,
        mac_address=None,
        vpc_id=None,
        subnet_id=None,
        status=None,
        private_ip_set=None,
        ipv6_private_ip_set=None,
        tags=None,
    ):
        """
        Initialize Eni instance.

        :param eni_id: 弹性网卡的ID
        :type eni_id: str (optional)

        :param name: 弹性网卡的名称
        :type name: str (optional)

        :param zone_name: 弹性网卡所属的可用区
        :type zone_name: str (optional)

        :param description: 弹性网卡的描述
        :type description: str (optional)

        :param instance_id: 挂载的云主机ID
        :type instance_id: str (optional)

        :param mac_address: 弹性网卡的mac地址
        :type mac_address: str (optional)

        :param vpc_id: 弹性网卡的VPC ID
        :type vpc_id: str (optional)

        :param subnet_id: 弹性网卡的子网ID
        :type subnet_id: str (optional)

        :param status: 弹性网卡的状态
        :type status: str (optional)

        :param private_ip_set: 弹性网卡的IPv4 IP集合
        :type private_ip_set: List[PrivateIP] (optional)

        :param ipv6_private_ip_set: 弹性网卡的IPv6 IP集合
        :type ipv6_private_ip_set: List[PrivateIP] (optional)

        :param tags: 弹性网卡绑定的标签集合
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.eni_id = eni_id
        self.name = name
        self.zone_name = zone_name
        self.description = description
        self.instance_id = instance_id
        self.mac_address = mac_address
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.status = status
        self.private_ip_set = private_ip_set
        self.ipv6_private_ip_set = ipv6_private_ip_set
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
        if self.eni_id is not None:
            result['eniId'] = self.eni_id
        if self.name is not None:
            result['name'] = self.name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.mac_address is not None:
            result['macAddress'] = self.mac_address
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.status is not None:
            result['status'] = self.status
        if self.private_ip_set is not None:
            result['privateIpSet'] = [i.to_dict() for i in self.private_ip_set]
        if self.ipv6_private_ip_set is not None:
            result['ipv6PrivateIpSet'] = [i.to_dict() for i in self.ipv6_private_ip_set]
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
        :rtype: Eni

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('macAddress') is not None:
            self.mac_address = m.get('macAddress')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('privateIpSet') is not None:
            self.private_ip_set = [PrivateIP().from_dict(i) for i in m.get('privateIpSet')]
        if m.get('ipv6PrivateIpSet') is not None:
            self.ipv6_private_ip_set = [PrivateIP().from_dict(i) for i in m.get('ipv6PrivateIpSet')]
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
