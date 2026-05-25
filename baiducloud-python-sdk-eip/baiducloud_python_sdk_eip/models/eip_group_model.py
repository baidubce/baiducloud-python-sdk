"""
EipGroupModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_eip.models.tag_model import TagModel

from baiducloud_python_sdk_eip.models.eip_model import EipModel

from baiducloud_python_sdk_eip.models.eip_model import EipModel


class EipGroupModel(AbstractModel):
    """
    EipGroupModel
    """

    def __init__(
        self,
        name=None,
        status=None,
        id=None,
        bandwidth_in_mbps=None,
        default_domestic_bandwidth=None,
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
        eips=None,
        eipv6s=None,
    ):
        """
        Initialize EipGroupModel instance.

        :param name: 共享带宽名称
        :type name: str (optional)

        :param status: 共享带宽状态
        :type status: str (optional)

        :param id: 共享带宽ID
        :type id: str (optional)

        :param bandwidth_in_mbps: 共享带宽带宽值，单位为Mbps
        :type bandwidth_in_mbps: int (optional)

        :param default_domestic_bandwidth: 默认跨境加速带宽，仅香港区域有该属性，单位为Mbps
        :type default_domestic_bandwidth: int (optional)

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

        :param billing_method: billing_method attribute
        :type billing_method: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param expire_time: 过期时间，只有预付费产品此参数才有值
        :type expire_time: str (optional)

        :param region: 共享带宽所属区域
        :type region: str (optional)

        :param route_type: 共享带宽线路类型
        :type route_type: str (optional)

        :param tags: 绑定的标签集合
        :type tags: List[TagModel] (optional)

        :param eips: 共享带宽中的IPv4 EIP信息
        :type eips: List[EipModel] (optional)

        :param eipv6s: 共享带宽中的IPv6 EIP信息
        :type eipv6s: List[EipModel] (optional)
        """
        super().__init__()
        self.name = name
        self.status = status
        self.id = id
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.default_domestic_bandwidth = default_domestic_bandwidth
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
        self.eips = eips
        self.eipv6s = eipv6s

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
        if self.status is not None:
            result['status'] = self.status
        if self.id is not None:
            result['id'] = self.id
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.default_domestic_bandwidth is not None:
            result['defaultDomesticBandwidth'] = self.default_domestic_bandwidth
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
        if self.eips is not None:
            result['eips'] = [i.to_dict() for i in self.eips]
        if self.eipv6s is not None:
            result['eipv6s'] = [i.to_dict() for i in self.eipv6s]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EipGroupModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('defaultDomesticBandwidth') is not None:
            self.default_domestic_bandwidth = m.get('defaultDomesticBandwidth')
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
        if m.get('eips') is not None:
            self.eips = [EipModel().from_dict(i) for i in m.get('eips')]
        if m.get('eipv6s') is not None:
            self.eipv6s = [EipModel().from_dict(i) for i in m.get('eipv6s')]
        return self
