"""
Request entity for CreateLbdcRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.billing_for_create import BillingForCreate
from baiducloud_python_sdk_blb.models.reservation_for_create import ReservationForCreate
from baiducloud_python_sdk_blb.models.tag_model import TagModel


class CreateLbdcRequest(AbstractModel):
    """
    Request entity for CreateLbdcRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, name, type, ccu_count, billing, client_token=None, desc=None, renew_reservation=None, tags=None
    ):
        """
        Initialize CreateLbdcRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 集群名称，长度1~65个字节，字母开头，_可包含字母数字-/.字符
        :type name: str (required)

        :param type: 集群类型，取值为\"4Layer\"或者\"7Layer\"
        :type type: str (required)

        :param ccu_count: 集群性能容量单位CCU（Cluster Capacity Unit）是用来衡量BLB集群处理流量时涉及的各个指标。
        :type ccu_count: int (required)

        :param desc: LBDC的描述，最大支持200字符
        :type desc: str (optional)

        :param billing: billing parameter
        :type billing: BillingForCreate (required)

        :param renew_reservation: renew_reservation parameter
        :type renew_reservation: ReservationForCreate (optional)

        :param tags: 标签
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.type = type
        self.ccu_count = ccu_count
        self.desc = desc
        self.billing = billing
        self.renew_reservation = renew_reservation
        self.tags = tags

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
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.ccu_count is not None:
            result['ccuCount'] = self.ccu_count
        if self.desc is not None:
            result['desc'] = self.desc
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.renew_reservation is not None:
            result['renewReservation'] = self.renew_reservation.to_dict()
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateLbdcRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('ccuCount') is not None:
            self.ccu_count = m.get('ccuCount')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('billing') is not None:
            self.billing = BillingForCreate().from_dict(m.get('billing'))
        if m.get('renewReservation') is not None:
            self.renew_reservation = ReservationForCreate().from_dict(m.get('renewReservation'))
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
