"""
SubnetVo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.tag import Tag


class SubnetVo(AbstractModel):
    """
    SubnetVo
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
        subnet_id=None,
        az=None,
        vpc_short_id=None,
        subnet_uuid=None,
        account_id=None,
        subnet_type=None,
        type=None,
        created_time=None,
        updated_time=None,
        used_ips=None,
        total_ips=None,
        tags=None,
        zone_name=None,
        enable_ipv6=None,
    ):
        """
        Initialize SubnetVo instance.

        :param vpc_id: vpcID
        :type vpc_id: str (optional)

        :param short_id: 子网短ID
        :type short_id: str (optional)

        :param name: 子网名称
        :type name: str (optional)

        :param cidr: IPV4地址及子网掩码 例如：192.168.0.0/20
        :type cidr: str (optional)

        :param status: 子网状态， 0表示可用、1表示创建中、大于等于2时表示不可用
        :type status: int (optional)

        :param create_time: 创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'
        :type create_time: date (optional)

        :param description: 描述
        :type description: str (optional)

        :param default_vpc: 是否默认子网。 true：有、false：没有；默认false
        :type default_vpc: bool (optional)

        :param ipv6_cidr: IPV6地址及子网掩码 例如：240c:4081:8005:2e03::/64
        :type ipv6_cidr: str (optional)

        :param auxiliary_cidr: Ipv4地址（vpc辅网络）
        :type auxiliary_cidr: List[str] (optional)

        :param relay: 是否开启replay。true：开启、false：未开启；默认false
        :type relay: bool (optional)

        :param subnet_id: 子网ID
        :type subnet_id: str (optional)

        :param az: zone+子网序列 ,例如:zoneA
        :type az: str (optional)

        :param vpc_short_id: vpc短ID
        :type vpc_short_id: str (optional)

        :param subnet_uuid: 子网序列ID
        :type subnet_uuid: str (optional)

        :param account_id: 账户ID
        :type account_id: str (optional)

        :param subnet_type: 设备类型 BCC(1), BBC（2）, BCC\\_NAT（3）,BBC\\_NAT（4）
        :type subnet_type: int (optional)

        :param type: type attribute
        :type type: int (optional)

        :param created_time: 创建时间
        :type created_time: str (optional)

        :param updated_time: 更新时间
        :type updated_time: str (optional)

        :param used_ips: 使用连接数
        :type used_ips: int (optional)

        :param total_ips: 总数连接数
        :type total_ips: int (optional)

        :param tags: 分组标签
        :type tags: List[Tag] (optional)

        :param zone_name: 区域名称
        :type zone_name: str (optional)

        :param enable_ipv6: IPV6 json字符串
        :type enable_ipv6: str (optional)
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
        self.subnet_id = subnet_id
        self.az = az
        self.vpc_short_id = vpc_short_id
        self.subnet_uuid = subnet_uuid
        self.account_id = account_id
        self.subnet_type = subnet_type
        self.type = type
        self.created_time = created_time
        self.updated_time = updated_time
        self.used_ips = used_ips
        self.total_ips = total_ips
        self.tags = tags
        self.zone_name = zone_name
        self.enable_ipv6 = enable_ipv6

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
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.az is not None:
            result['az'] = self.az
        if self.vpc_short_id is not None:
            result['vpcShortId'] = self.vpc_short_id
        if self.subnet_uuid is not None:
            result['subnetUuid'] = self.subnet_uuid
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.subnet_type is not None:
            result['subnetType'] = self.subnet_type
        if self.type is not None:
            result['type'] = self.type
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        if self.used_ips is not None:
            result['usedIps'] = self.used_ips
        if self.total_ips is not None:
            result['totalIps'] = self.total_ips
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.enable_ipv6 is not None:
            result['enable_ipv6'] = self.enable_ipv6
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SubnetVo

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
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('az') is not None:
            self.az = m.get('az')
        if m.get('vpcShortId') is not None:
            self.vpc_short_id = m.get('vpcShortId')
        if m.get('subnetUuid') is not None:
            self.subnet_uuid = m.get('subnetUuid')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('subnetType') is not None:
            self.subnet_type = m.get('subnetType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        if m.get('usedIps') is not None:
            self.used_ips = m.get('usedIps')
        if m.get('totalIps') is not None:
            self.total_ips = m.get('totalIps')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('enable_ipv6') is not None:
            self.enable_ipv6 = m.get('enable_ipv6')
        return self
