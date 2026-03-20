"""
EipModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_eip.models.tag_model import TagModel


class EipModel(AbstractModel):
    """
    EipModel
    """

    def __init__(
        self,
        name=None,
        eip=None,
        eip_id=None,
        status=None,
        eip_instance_type=None,
        instance_type=None,
        instance_id=None,
        share_group_id=None,
        default_domestic_bandwidth=None,
        bandwidth_in_mbps=None,
        bw_short_id=None,
        bw_bandwidth_in_mbps=None,
        domestic_bw_short_id=None,
        domestic_bw_bandwidth_in_mbps=None,
        payment_timing=None,
        billing_method=None,
        create_time=None,
        expire_time=None,
        region=None,
        route_type=None,
        tags=None,
        delete_protect=None,
        native_group=None,
        original_bandwidth=None,
        origin_product_type=None,
        origin_sub_product_type=None,
    ):
        """
        Initialize EipModel instance.

        :param name: EIP的名字
        :type name: str (optional)

        :param eip: EIP地址，点分十进制表示
        :type eip: str (optional)

        :param eip_id: EIP ID
        :type eip_id: str (optional)

        :param status: EIP状态
        :type status: str (optional)

        :param eip_instance_type: EIP实例类型
        :type eip_instance_type: str (optional)

        :param instance_type: 绑定实例类型，若EIP处于未绑定状态，此项值为空
        :type instance_type: str (optional)

        :param instance_id: 实例ID，若EIP处于未绑定状态，此项值为空
        :type instance_id: str (optional)

        :param share_group_id: 共享带宽组ID，若为普通EIP，此项值为空
        :type share_group_id: str (optional)

        :param default_domestic_bandwidth: 默认跨境加速带宽，仅香港区域有该属性，单位为Mbps
        :type default_domestic_bandwidth: int (optional)

        :param bandwidth_in_mbps: 公网带宽，单位为Mbps
        :type bandwidth_in_mbps: int (optional)

        :param bw_short_id: 带宽包ID
        :type bw_short_id: str (optional)

        :param bw_bandwidth_in_mbps: 带宽包带宽，单位为Mbps
        :type bw_bandwidth_in_mbps: int (optional)

        :param domestic_bw_short_id: 跨境加速包ID
        :type domestic_bw_short_id: str (optional)

        :param domestic_bw_bandwidth_in_mbps: 跨境加速包带宽，单位为Mbps
        :type domestic_bw_bandwidth_in_mbps: int (optional)

        :param payment_timing: 付款时间，预支付（Prepaid）和后支付（Postpaid）
        :type payment_timing: str (optional)

        :param billing_method: 计费方式，按流量（ByTraffic）和按带宽（ByBandwidth，只有后付费产品此参数才有值
        :type billing_method: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param expire_time: 过期时间，只有预付费产品此参数才有值
        :type expire_time: str (optional)

        :param region: 当前EIP所属区域
        :type region: str (optional)

        :param route_type: EIP线路类型
        :type route_type: str (optional)

        :param tags: 绑定的标签集合
        :type tags: List[TagModel] (optional)

        :param delete_protect: 是否开启释放保护
        :type delete_protect: bool (optional)

        :param native_group: 标记EIP是否为原生EIP，true：原生EIP，false：非原生EIP。（只有查询共享带宽详情接口该字段才存在。）
        :type native_group: bool (optional)

        :param original_bandwidth: eip原始带宽（移入group前的带宽），如果是原生EIP，（只有查询共享带宽详情接口该字段才存在。）
        :type original_bandwidth: int (optional)

        :param origin_product_type: group 内 EIP 原始计费类型，如果是原生EIP，值为空，（只有查询共享带宽详情接口该字段才存在。）
        :type origin_product_type: str (optional)

        :param origin_sub_product_type: group 内 EIP 原始计费子类型，如果是原生EIP，值为空。（只有查询共享带宽详情接口该字段才存在。）
        :type origin_sub_product_type: str (optional)
        """
        super().__init__()
        self.name = name
        self.eip = eip
        self.eip_id = eip_id
        self.status = status
        self.eip_instance_type = eip_instance_type
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.share_group_id = share_group_id
        self.default_domestic_bandwidth = default_domestic_bandwidth
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.bw_short_id = bw_short_id
        self.bw_bandwidth_in_mbps = bw_bandwidth_in_mbps
        self.domestic_bw_short_id = domestic_bw_short_id
        self.domestic_bw_bandwidth_in_mbps = domestic_bw_bandwidth_in_mbps
        self.payment_timing = payment_timing
        self.billing_method = billing_method
        self.create_time = create_time
        self.expire_time = expire_time
        self.region = region
        self.route_type = route_type
        self.tags = tags
        self.delete_protect = delete_protect
        self.native_group = native_group
        self.original_bandwidth = original_bandwidth
        self.origin_product_type = origin_product_type
        self.origin_sub_product_type = origin_sub_product_type

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
        if self.name is not None:
            result['name'] = self.name
        if self.eip is not None:
            result['eip'] = self.eip
        if self.eip_id is not None:
            result['eipId'] = self.eip_id
        if self.status is not None:
            result['status'] = self.status
        if self.eip_instance_type is not None:
            result['eipInstanceType'] = self.eip_instance_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.share_group_id is not None:
            result['shareGroupId'] = self.share_group_id
        if self.default_domestic_bandwidth is not None:
            result['defaultDomesticBandwidth'] = self.default_domestic_bandwidth
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.bw_short_id is not None:
            result['bwShortId'] = self.bw_short_id
        if self.bw_bandwidth_in_mbps is not None:
            result['bwBandwidthInMbps'] = self.bw_bandwidth_in_mbps
        if self.domestic_bw_short_id is not None:
            result['domesticBwShortId'] = self.domestic_bw_short_id
        if self.domestic_bw_bandwidth_in_mbps is not None:
            result['domesticBwBandwidthInMbps'] = self.domestic_bw_bandwidth_in_mbps
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.region is not None:
            result['region'] = self.region
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        if self.native_group is not None:
            result['nativeGroup'] = self.native_group
        if self.original_bandwidth is not None:
            result['originalBandwidth'] = self.original_bandwidth
        if self.origin_product_type is not None:
            result['originProductType'] = self.origin_product_type
        if self.origin_sub_product_type is not None:
            result['originSubProductType'] = self.origin_sub_product_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EipModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('eipId') is not None:
            self.eip_id = m.get('eipId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('eipInstanceType') is not None:
            self.eip_instance_type = m.get('eipInstanceType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('shareGroupId') is not None:
            self.share_group_id = m.get('shareGroupId')
        if m.get('defaultDomesticBandwidth') is not None:
            self.default_domestic_bandwidth = m.get('defaultDomesticBandwidth')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('bwShortId') is not None:
            self.bw_short_id = m.get('bwShortId')
        if m.get('bwBandwidthInMbps') is not None:
            self.bw_bandwidth_in_mbps = m.get('bwBandwidthInMbps')
        if m.get('domesticBwShortId') is not None:
            self.domestic_bw_short_id = m.get('domesticBwShortId')
        if m.get('domesticBwBandwidthInMbps') is not None:
            self.domestic_bw_bandwidth_in_mbps = m.get('domesticBwBandwidthInMbps')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        if m.get('nativeGroup') is not None:
            self.native_group = m.get('nativeGroup')
        if m.get('originalBandwidth') is not None:
            self.original_bandwidth = m.get('originalBandwidth')
        if m.get('originProductType') is not None:
            self.origin_product_type = m.get('originProductType')
        if m.get('originSubProductType') is not None:
            self.origin_sub_product_type = m.get('originSubProductType')
        return self
