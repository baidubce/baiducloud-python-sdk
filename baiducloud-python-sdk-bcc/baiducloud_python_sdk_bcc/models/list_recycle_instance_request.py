"""
Request entity for ListRecycleInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListRecycleInstanceRequest(AbstractModel):
    """
    Request entity for ListRecycleInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        marker=None,
        max_keys=None,
        instance_id=None,
        name=None,
        payment_timing=None,
        recycle_begin=None,
        recycle_end=None,
    ):
        """
        Initialize ListRecycleInstanceRequest request entity.

        :param marker: 批量获取列表的查询的起始位置，是一个由系统生成的字符串
        :type marker: str (optional)

        :param max_keys: 每页包含的最大数量，最大数量通常不超过1000，缺省值为1000。
        :type max_keys: int (optional)

        :param instance_id: 虚机Id
        :type instance_id: str (optional)

        :param name: 虚机名称
        :type name: str (optional)

        :param payment_timing: 支付方式，包括包年包月（Prepaid）和按量付费（Postpaid）
        :type payment_timing: str (optional)

        :param recycle_begin: 查询进入回收站时间大于等于该起始时间，格式yyyy-MM-ddTHH:mm:ssZ
        :type recycle_begin: str (optional)

        :param recycle_end: 查询进入回收站时间小于等于该终止时间，格式yyyy-MM-ddTHH:mm:ssZ
        :type recycle_end: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.instance_id = instance_id
        self.name = name
        self.payment_timing = payment_timing
        self.recycle_begin = recycle_begin
        self.recycle_end = recycle_end

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.name is not None:
            result['name'] = self.name
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.recycle_begin is not None:
            result['recycleBegin'] = self.recycle_begin
        if self.recycle_end is not None:
            result['recycleEnd'] = self.recycle_end
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListRecycleInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('recycleBegin') is not None:
            self.recycle_begin = m.get('recycleBegin')
        if m.get('recycleEnd') is not None:
            self.recycle_end = m.get('recycleEnd')
        return self
