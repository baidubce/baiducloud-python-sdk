"""
BLBModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.tag_model import TagModel


class BLBModel(AbstractModel):
    """
    BLBModel
    """

    def __init__(
        self,
        blb_id=None,
        name=None,
        desc=None,
        address=None,
        status=None,
        vpc_id=None,
        subnet_id=None,
        public_ip=None,
        tags=None,
        allow_delete=None,
        allow_modify=None,
        modification_protection_reason=None,
        eip_route_type=None,
        public_ipv6=None,
        eip_v6_route_type=None,
        payment_timing=None,
        billing_method=None,
    ):
        """
        Initialize BLBModel instance.

        :param blb_id: LoadBalancer的标识符
        :type blb_id: str (optional)

        :param name: LoadBalancer的名称
        :type name: str (optional)

        :param desc: LoadBalancer的描述
        :type desc: str (optional)

        :param address: 分配的内网服务地址IP，通过这个IP即能通过内网访问该实例
        :type address: str (optional)

        :param status: BLB状态
        :type status: str (optional)

        :param vpc_id: vpc 的ID
        :type vpc_id: str (optional)

        :param subnet_id: subnet 的ID
        :type subnet_id: str (optional)

        :param public_ip: 如果LoadBalancer绑定过EIP，则显示该项，否则不显示
        :type public_ip: str (optional)

        :param tags: 标签键值对列表
        :type tags: List[TagModel] (optional)

        :param allow_delete: 是否允许删除
        :type allow_delete: bool (optional)

        :param allow_modify: 是否允许修改
        :type allow_modify: bool (optional)

        :param modification_protection_reason: 开启修改保护原因
        :type modification_protection_reason: str (optional)

        :param eip_route_type: EIP线路类型
        :type eip_route_type: str (optional)

        :param public_ipv6: 如果LoadBalancer绑定过EIPv6，则显示该项，否则不显示
        :type public_ipv6: str (optional)

        :param eip_v6_route_type: EIPV6线路类型
        :type eip_v6_route_type: str (optional)

        :param payment_timing: 计费方式 取值：\"Postpaid\" 后付费 \"Prepaid\" 预付费
        :type payment_timing: str (optional)

        :param billing_method: 计费方式 取值：\"ByCapacityUnit\" 按使用量 \"BySpec\" 按固定规格
        :type billing_method: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.name = name
        self.desc = desc
        self.address = address
        self.status = status
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.public_ip = public_ip
        self.tags = tags
        self.allow_delete = allow_delete
        self.allow_modify = allow_modify
        self.modification_protection_reason = modification_protection_reason
        self.eip_route_type = eip_route_type
        self.public_ipv6 = public_ipv6
        self.eip_v6_route_type = eip_v6_route_type
        self.payment_timing = payment_timing
        self.billing_method = billing_method

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
        if self.blb_id is not None:
            result['blbId'] = self.blb_id
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.address is not None:
            result['address'] = self.address
        if self.status is not None:
            result['status'] = self.status
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.public_ip is not None:
            result['publicIp'] = self.public_ip
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.allow_delete is not None:
            result['allowDelete'] = self.allow_delete
        if self.allow_modify is not None:
            result['allowModify'] = self.allow_modify
        if self.modification_protection_reason is not None:
            result['modificationProtectionReason'] = self.modification_protection_reason
        if self.eip_route_type is not None:
            result['eipRouteType'] = self.eip_route_type
        if self.public_ipv6 is not None:
            result['publicIpv6'] = self.public_ipv6
        if self.eip_v6_route_type is not None:
            result['eipV6RouteType'] = self.eip_v6_route_type
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BLBModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('publicIp') is not None:
            self.public_ip = m.get('publicIp')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('allowDelete') is not None:
            self.allow_delete = m.get('allowDelete')
        if m.get('allowModify') is not None:
            self.allow_modify = m.get('allowModify')
        if m.get('modificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('modificationProtectionReason')
        if m.get('eipRouteType') is not None:
            self.eip_route_type = m.get('eipRouteType')
        if m.get('publicIpv6') is not None:
            self.public_ipv6 = m.get('publicIpv6')
        if m.get('eipV6RouteType') is not None:
            self.eip_v6_route_type = m.get('eipV6RouteType')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        return self
