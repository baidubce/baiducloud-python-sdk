"""
CsnBp information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_csn.models.tag_model import TagModel


class CsnBp(AbstractModel):
    """
    CsnBp
    """

    def __init__(
        self,
        csn_bp_id=None,
        name=None,
        bandwidth=None,
        used_bandwidth=None,
        csn_id=None,
        interwork_type=None,
        interwork_region=None,
        status=None,
        payment_timing=None,
        expire_time=None,
        created_time=None,
        tags=None,
    ):
        """
        Initialize CsnBp instance.

        :param csn_bp_id: 带宽包的ID
        :type csn_bp_id: str (optional)

        :param name: 带宽包的名称
        :type name: str (optional)

        :param bandwidth: 带宽包的总带宽
        :type bandwidth: str (optional)

        :param used_bandwidth: 带宽包的已分配带宽
        :type used_bandwidth: str (optional)

        :param csn_id: 绑定云智能网实例
        :type csn_id: str (optional)

        :param interwork_type: interwork_type attribute
        :type interwork_type: str (optional)

        :param interwork_region: interwork_region attribute
        :type interwork_region: str (optional)

        :param status: 带宽包状态，取值[ available \\| stopped ]，分别表示可用、已到期
        :type status: str (optional)

        :param payment_timing: 带宽包的付费方式，取值[ PrePaid \\| PostPaid ]，分别表示预付费、后付费
        :type payment_timing: str (optional)

        :param expire_time: 到期时间，标准UTC格式
        :type expire_time: str (optional)

        :param created_time: 购买时间，标准UTC格式
        :type created_time: str (optional)

        :param tags: vpc绑定的标签集合
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.csn_bp_id = csn_bp_id
        self.name = name
        self.bandwidth = bandwidth
        self.used_bandwidth = used_bandwidth
        self.csn_id = csn_id
        self.interwork_type = interwork_type
        self.interwork_region = interwork_region
        self.status = status
        self.payment_timing = payment_timing
        self.expire_time = expire_time
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
        if self.csn_bp_id is not None:
            result['csnBpId'] = self.csn_bp_id
        if self.name is not None:
            result['name'] = self.name
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.used_bandwidth is not None:
            result['usedBandwidth'] = self.used_bandwidth
        if self.csn_id is not None:
            result['csnId'] = self.csn_id
        if self.interwork_type is not None:
            result['interworkType'] = self.interwork_type
        if self.interwork_region is not None:
            result['interworkRegion'] = self.interwork_region
        if self.status is not None:
            result['status'] = self.status
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
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
        :rtype: CsnBp

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnBpId') is not None:
            self.csn_bp_id = m.get('csnBpId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('usedBandwidth') is not None:
            self.used_bandwidth = m.get('usedBandwidth')
        if m.get('csnId') is not None:
            self.csn_id = m.get('csnId')
        if m.get('interworkType') is not None:
            self.interwork_type = m.get('interworkType')
        if m.get('interworkRegion') is not None:
            self.interwork_region = m.get('interworkRegion')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
