"""
Request entity for CreateRenewResourceRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateRenewResourceRuleRequest(AbstractModel):
    """
    Request entity for CreateRenewResourceRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, service_type, region, instance_id, renew_time_unit, renew_time, account_id=None):
        """
        Initialize CreateRenewResourceRuleRequest request entity.

        :param account_id: account_id parameter
        :type account_id: str (optional)

        :param service_type: 产品类型，例：BCC，EIP等
        :type service_type: str (required)

        :param region: 区域，例如：bj
        :type region: str (required)

        :param instance_id: 资源长ID，是资源的唯一标示uuid，指定需要配置的资源
        :type instance_id: str (required)

        :param renew_time_unit: 自动续费时长单位，只有两种，month&year，分别表示按月和按年
        :type renew_time_unit: str (required)

        :param renew_time: renew_time parameter
        :type renew_time: str (required)
        """
        super().__init__()
        self.account_id = account_id
        self.service_type = service_type
        self.region = region
        self.instance_id = instance_id
        self.renew_time_unit = renew_time_unit
        self.renew_time = renew_time

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
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.region is not None:
            result['region'] = self.region
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.renew_time_unit is not None:
            result['renewTimeUnit'] = self.renew_time_unit
        if self.renew_time is not None:
            result['renewTime'] = self.renew_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateRenewResourceRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('renewTimeUnit') is not None:
            self.renew_time_unit = m.get('renewTimeUnit')
        if m.get('renewTime') is not None:
            self.renew_time = m.get('renewTime')
        return self
