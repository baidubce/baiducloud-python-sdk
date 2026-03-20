"""
Request entity for CreateTbspRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateTbspRequest(AbstractModel):
    """
    Request entity for CreateTbspRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        line_type,
        ip_capacity,
        reservation_length,
        reservation_time_unit,
        client_token=None,
        auto_renew_time=None,
        auto_renew_time_unit=None,
    ):
        """
        Initialize CreateTbspRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: DDoS增强防护包名称
        :type name: str (required)

        :param line_type: 线路类型（支持BGP/BGP_S，分别代表标准BGP/增强BGP）
        :type line_type: str (required)

        :param ip_capacity: 单个服务包的IP容量（1/5/30/100）
        :type ip_capacity: int (required)

        :param reservation_length: 购买时长（按天：1-20；按月：3，6； 按年：1-3）
        :type reservation_length: int (required)

        :param reservation_time_unit: 购买时长单位（DAY/MONTH/YEAR）
        :type reservation_time_unit: str (required)

        :param auto_renew_time: 自动续费周期，创建TBSP同时开通自动续费（按月：1-9； 按年：1-3）
        :type auto_renew_time: int (optional)

        :param auto_renew_time_unit: 自动续费周期单位，创建TBSP同时开通自动续费（MONTH/YEAR）
        :type auto_renew_time_unit: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.line_type = line_type
        self.ip_capacity = ip_capacity
        self.reservation_length = reservation_length
        self.reservation_time_unit = reservation_time_unit
        self.auto_renew_time = auto_renew_time
        self.auto_renew_time_unit = auto_renew_time_unit

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
        if self.line_type is not None:
            result['lineType'] = self.line_type
        if self.ip_capacity is not None:
            result['ipCapacity'] = self.ip_capacity
        if self.reservation_length is not None:
            result['reservationLength'] = self.reservation_length
        if self.reservation_time_unit is not None:
            result['reservationTimeUnit'] = self.reservation_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateTbspRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('lineType') is not None:
            self.line_type = m.get('lineType')
        if m.get('ipCapacity') is not None:
            self.ip_capacity = m.get('ipCapacity')
        if m.get('reservationLength') is not None:
            self.reservation_length = m.get('reservationLength')
        if m.get('reservationTimeUnit') is not None:
            self.reservation_time_unit = m.get('reservationTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        return self
