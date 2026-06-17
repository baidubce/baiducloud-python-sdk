"""
Request entity for CreateAutoRenewRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateAutoRenewRuleRequest(AbstractModel):
    """
    Request entity for CreateAutoRenewRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, renew_time_unit, renew_time, renew_eip=None):
        """
        Initialize CreateAutoRenewRuleRequest request entity.

        :param instance_id: 实例Id
        :type instance_id: str (required)

        :param renew_time_unit: 续费时间，单位：month，支持1, 2, 3, 4, 5, 6, 7, 8, 9；单位：year，支持1, 2, 3
        :type renew_time_unit: str (required)

        :param renew_time: 续费时长
        :type renew_time: int (required)

        :param renew_eip: 是否合并eip自动续费，默认值为true。
        :type renew_eip: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.renew_time_unit = renew_time_unit
        self.renew_time = renew_time
        self.renew_eip = renew_eip

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.renew_time_unit is not None:
            result['renewTimeUnit'] = self.renew_time_unit
        if self.renew_time is not None:
            result['renewTime'] = self.renew_time
        if self.renew_eip is not None:
            result['renewEip'] = self.renew_eip
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAutoRenewRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('renewTimeUnit') is not None:
            self.renew_time_unit = m.get('renewTimeUnit')
        if m.get('renewTime') is not None:
            self.renew_time = m.get('renewTime')
        if m.get('renewEip') is not None:
            self.renew_eip = m.get('renewEip')
        return self
