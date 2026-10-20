"""
Request entity for InstanceEnablesAutomaticRenewalRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceEnablesAutomaticRenewalRequest(AbstractModel):
    """
    Request entity for InstanceEnablesAutomaticRenewalRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_ids=None, auto_renew_time_unit=None, auto_renew_time=None):
        """
        Initialize InstanceEnablesAutomaticRenewalRequest request entity.

        :param instance_ids: 实例ID列表
        :type instance_ids: List[str] (optional)

        :param auto_renew_time_unit: 自动续费周期单位（年：year；月：month）
        :type auto_renew_time_unit: str (optional)

        :param auto_renew_time: 续费周期按月（不超过9个月）按年付费（不超过3年）
        :type auto_renew_time: int (optional)
        """
        super().__init__()
        self.instance_ids = instance_ids
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
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
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
        :rtype: InstanceEnablesAutomaticRenewalRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        return self
