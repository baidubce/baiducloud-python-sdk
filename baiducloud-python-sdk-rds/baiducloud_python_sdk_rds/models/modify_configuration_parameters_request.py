"""
Request entity for ModifyConfigurationParametersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.parameter import Parameter


class ModifyConfigurationParametersRequest(AbstractModel):
    """
    Request entity for ModifyConfigurationParametersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, effective_time, parameters):
        """
        Initialize ModifyConfigurationParametersRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param effective_time: 实际生效方式：立即执行（immediate）、维护时间执行（timewindow）
        :type effective_time: str (required)

        :param parameters: 需要修改的参数列表
        :type parameters: List[Parameter] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.effective_time = effective_time
        self.parameters = parameters

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
        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time
        if self.parameters is not None:
            result['parameters'] = [i.to_dict() for i in self.parameters]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyConfigurationParametersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')
        if m.get('parameters') is not None:
            self.parameters = [Parameter().from_dict(i) for i in m.get('parameters')]
        return self
