"""
SimpleVpcVo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SimpleVpcVo(AbstractModel):
    """
    SimpleVpcVo
    """

    def __init__(
        self,
        vpc_id=None,
        short_id=None,
        name=None,
        cidr=None,
        status=None,
        create_time=None,
        description=None,
        default_vpc=None,
        ipv6_cidr=None,
        auxiliary_cidr=None,
        relay=None,
    ):
        """
        Initialize SimpleVpcVo instance.

        :param vpc_id: vpcID。
        :type vpc_id: str (optional)

        :param short_id: vpc短ID。
        :type short_id: str (optional)

        :param name: vpc名称。
        :type name: str (optional)

        :param cidr: Ipv4地址（vpc主网络）。
        :type cidr: str (optional)

        :param status: 子网状态 0表示可用、1表示创建中、大于等于2时表示不可用。
        :type status: int (optional)

        :param create_time: 创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'。
        :type create_time: date (optional)

        :param description: 子网描述。
        :type description: str (optional)

        :param default_vpc: 是否默认子网。 true：有、false：没有；默认false。
        :type default_vpc: bool (optional)

        :param ipv6_cidr: IPv6地址。
        :type ipv6_cidr: str (optional)

        :param auxiliary_cidr: Ipv4地址（vpc辅网络）。
        :type auxiliary_cidr: List[str] (optional)

        :param relay: 是否开启replay。true：开启、false：未开启；默认false。
        :type relay: bool (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.short_id = short_id
        self.name = name
        self.cidr = cidr
        self.status = status
        self.create_time = create_time
        self.description = description
        self.default_vpc = default_vpc
        self.ipv6_cidr = ipv6_cidr
        self.auxiliary_cidr = auxiliary_cidr
        self.relay = relay

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
        if self.short_id is not None:
            result['shortId'] = self.short_id
        if self.name is not None:
            result['name'] = self.name
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.status is not None:
            result['status'] = self.status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.default_vpc is not None:
            result['defaultVpc'] = self.default_vpc
        if self.ipv6_cidr is not None:
            result['ipv6Cidr'] = self.ipv6_cidr
        if self.auxiliary_cidr is not None:
            result['auxiliaryCidr'] = self.auxiliary_cidr
        if self.relay is not None:
            result['relay'] = self.relay
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SimpleVpcVo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('shortId') is not None:
            self.short_id = m.get('shortId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('defaultVpc') is not None:
            self.default_vpc = m.get('defaultVpc')
        if m.get('ipv6Cidr') is not None:
            self.ipv6_cidr = m.get('ipv6Cidr')
        if m.get('auxiliaryCidr') is not None:
            self.auxiliary_cidr = m.get('auxiliaryCidr')
        if m.get('relay') is not None:
            self.relay = m.get('relay')
        return self
