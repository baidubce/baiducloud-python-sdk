"""
Request entity for RenewReservedInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RenewReservedInstanceRequest(AbstractModel):
    """
    Request entity for RenewReservedInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        reserved_instance_ids,
        reserved_instance_time,
        reserved_instance_time_unit=None,
        auto_renew=None,
        auto_renew_time_unit=None,
        auto_renew_time=None,
    ):
        """
        Initialize RenewReservedInstanceRequest request entity.

        :param reserved_instance_ids: 实例券id集合
        :type reserved_instance_ids: List[str] (required)

        :param reserved_instance_time: 预留实例券续费时长，支持3，6，9，12，24，36个月，必须与购买时长保持一致
        :type reserved_instance_time: str (required)

        :param reserved_instance_time_unit: 预留实例券购买时长单位，默认为month，不可变更
        :type reserved_instance_time_unit: str (optional)

        :param auto_renew: 自动续费开关，默认为false
        :type auto_renew: bool (optional)

        :param auto_renew_time_unit: 预留实例券自动续费时长单位，默认为month，不可变更
        :type auto_renew_time_unit: str (optional)

        :param auto_renew_time: auto_renew_time parameter
        :type auto_renew_time: int (optional)
        """
        super().__init__()
        self.reserved_instance_ids = reserved_instance_ids
        self.reserved_instance_time = reserved_instance_time
        self.reserved_instance_time_unit = reserved_instance_time_unit
        self.auto_renew = auto_renew
        self.auto_renew_time_unit = auto_renew_time_unit
        self.auto_renew_time = auto_renew_time

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
        if self.reserved_instance_ids is not None:
            result['reservedInstanceIds'] = self.reserved_instance_ids
        if self.reserved_instance_time is not None:
            result['reservedInstanceTime'] = self.reserved_instance_time
        if self.reserved_instance_time_unit is not None:
            result['reservedInstanceTimeUnit'] = self.reserved_instance_time_unit
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RenewReservedInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservedInstanceIds') is not None:
            self.reserved_instance_ids = m.get('reservedInstanceIds')
        if m.get('reservedInstanceTime') is not None:
            self.reserved_instance_time = m.get('reservedInstanceTime')
        if m.get('reservedInstanceTimeUnit') is not None:
            self.reserved_instance_time_unit = m.get('reservedInstanceTimeUnit')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        return self
