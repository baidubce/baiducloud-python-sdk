"""
Request entity for ValidateAlarmConditionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ValidateAlarmConditionRequest(AbstractModel):
    """
    Request entity for ValidateAlarmConditionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, field_types, conditions):
        """
        Initialize ValidateAlarmConditionRequest request entity.

        :param field_types: 字段名称和类型，按照sql的顺序
        :type field_types: List[str] (required)

        :param conditions: 执行条件列表
        :type conditions: List[str] (required)
        """
        super().__init__()
        self.field_types = field_types
        self.conditions = conditions

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
        if self.field_types is not None:
            result['fieldTypes'] = self.field_types
        if self.conditions is not None:
            result['conditions'] = self.conditions
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ValidateAlarmConditionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fieldTypes') is not None:
            self.field_types = m.get('fieldTypes')
        if m.get('conditions') is not None:
            self.conditions = m.get('conditions')
        return self
