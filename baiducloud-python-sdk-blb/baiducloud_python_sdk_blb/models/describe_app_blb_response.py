"""
Request entity for DescribeAppBlbResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_blb.models.listener_model import ListenerModel
from baiducloud_python_sdk_blb.models.tag_model import TagModel


class DescribeAppBlbResponse(BceResponse):
    """
    DescribeAppBlbResponse
    """

    def __init__(
        self,
        blb_id=None,
        status=None,
        desc=None,
        address=None,
        public_ip=None,
        cidr=None,
        vpc_name=None,
        subnet_cider=None,
        subnet_name=None,
        create_time=None,
        release_time=None,
        listener=None,
        tags=None,
        allow_delete=None,
        allow_modify=None,
        modification_protection_reason=None,
        payment_timing=None,
        billing_method=None,
        performance_level=None,
        expire_time=None,
        eip_route_type=None,
        public_ipv6=None,
        eip_v6_route_type=None,
    ):
        """
        Initialize DescribeAppBlbResponse response.

        :param blb_id: LoadBalancer的标识符
        :type blb_id: str (optional)

        :param status: BLB状态
        :type status: str (optional)

        :param desc: LoadBalancer的描述
        :type desc: str (optional)

        :param address: LoadBalancer的内网地址
        :type address: str (optional)

        :param public_ip: LoadBalancer的公网地址
        :type public_ip: str (optional)

        :param cidr: LoadBalancer所在网络cidr
        :type cidr: str (optional)

        :param vpc_name: LoadBalancer所属vpc名称
        :type vpc_name: str (optional)

        :param subnet_cider: LoadBalancer所属子网cidr
        :type subnet_cider: str (optional)

        :param subnet_name: LoadBalancer所属子网名称
        :type subnet_name: str (optional)

        :param create_time: LoadBalancer创建时间
        :type create_time: str (optional)

        :param release_time: LoadBalancer自动释放时间
        :type release_time: str (optional)

        :param listener: LoadBalancer下挂载监听器列表
        :type listener: List[ListenerModel] (optional)

        :param tags: 标签键值对列表
        :type tags: List[TagModel] (optional)

        :param allow_delete: 是否允许删除
        :type allow_delete: bool (optional)

        :param allow_modify: 是否允许控制台进行修改
        :type allow_modify: bool (optional)

        :param modification_protection_reason: 开启修改保护原因
        :type modification_protection_reason: str (optional)

        :param payment_timing: 付款时间，预支付（Prepaid）或后支付（Postpaid）
        :type payment_timing: str (optional)

        :param billing_method: 计费方式，\"ByCapacityUnit\" 按使用量 \"BySpec\" 按固定规格
        :type billing_method: str (optional)

        :param performance_level: performance_level field
        :type performance_level: str (optional)

        :param expire_time: 预付费实例的过期时间
        :type expire_time: str (optional)

        :param eip_route_type: EIP线路类型
        :type eip_route_type: str (optional)

        :param public_ipv6: 如果LoadBalancer绑定过EIPv6，则显示该项，否则不显示
        :type public_ipv6: str (optional)

        :param eip_v6_route_type: EIPV6线路类型
        :type eip_v6_route_type: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.status = status
        self.desc = desc
        self.address = address
        self.public_ip = public_ip
        self.cidr = cidr
        self.vpc_name = vpc_name
        self.subnet_cider = subnet_cider
        self.subnet_name = subnet_name
        self.create_time = create_time
        self.release_time = release_time
        self.listener = listener
        self.tags = tags
        self.allow_delete = allow_delete
        self.allow_modify = allow_modify
        self.modification_protection_reason = modification_protection_reason
        self.payment_timing = payment_timing
        self.billing_method = billing_method
        self.performance_level = performance_level
        self.expire_time = expire_time
        self.eip_route_type = eip_route_type
        self.public_ipv6 = public_ipv6
        self.eip_v6_route_type = eip_v6_route_type

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.blb_id is not None:
            result['blbId'] = self.blb_id
        if self.status is not None:
            result['status'] = self.status
        if self.desc is not None:
            result['desc'] = self.desc
        if self.address is not None:
            result['address'] = self.address
        if self.public_ip is not None:
            result['publicIp'] = self.public_ip
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.vpc_name is not None:
            result['vpcName'] = self.vpc_name
        if self.subnet_cider is not None:
            result['subnetCider'] = self.subnet_cider
        if self.subnet_name is not None:
            result['subnetName'] = self.subnet_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.release_time is not None:
            result['releaseTime'] = self.release_time
        if self.listener is not None:
            result['listener'] = [i.to_dict() for i in self.listener]
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.allow_delete is not None:
            result['allowDelete'] = self.allow_delete
        if self.allow_modify is not None:
            result['allowModify'] = self.allow_modify
        if self.modification_protection_reason is not None:
            result['modificationProtectionReason'] = self.modification_protection_reason
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.eip_route_type is not None:
            result['eipRouteType'] = self.eip_route_type
        if self.public_ipv6 is not None:
            result['publicIpv6'] = self.public_ipv6
        if self.eip_v6_route_type is not None:
            result['eipV6RouteType'] = self.eip_v6_route_type
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAppBlbResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('publicIp') is not None:
            self.public_ip = m.get('publicIp')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('vpcName') is not None:
            self.vpc_name = m.get('vpcName')
        if m.get('subnetCider') is not None:
            self.subnet_cider = m.get('subnetCider')
        if m.get('subnetName') is not None:
            self.subnet_name = m.get('subnetName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')
        if m.get('listener') is not None:
            self.listener = [ListenerModel().from_dict(i) for i in m.get('listener')]
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('allowDelete') is not None:
            self.allow_delete = m.get('allowDelete')
        if m.get('allowModify') is not None:
            self.allow_modify = m.get('allowModify')
        if m.get('modificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('modificationProtectionReason')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('eipRouteType') is not None:
            self.eip_route_type = m.get('eipRouteType')
        if m.get('publicIpv6') is not None:
            self.public_ipv6 = m.get('publicIpv6')
        if m.get('eipV6RouteType') is not None:
            self.eip_v6_route_type = m.get('eipV6RouteType')
        return self
