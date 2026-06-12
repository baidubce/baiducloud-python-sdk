"""
AlarmRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.alarm_condition import AlarmCondition


class AlarmRule(AbstractModel):
    """
    AlarmRule
    """

    def __init__(self, conditions=None, pending_count=None, check_interval_seconds=None, content=None):
        """
        Initialize AlarmRule instance.

        :param conditions: 规则内的条件列表（AND规则）
        :type conditions: List[AlarmCondition] (optional)

        :param pending_count: 连续触发次数，取值范围：大于0
        :type pending_count: int (optional)

        :param check_interval_seconds: 检查间隔，单位：秒，取值范围：大于0
        :type check_interval_seconds: int (optional)

        :param content: 报警条件内容描述（仅在查询响应中返回）
        :type content: str (optional)
        """
        super().__init__()
        self.conditions = conditions
        self.pending_count = pending_count
        self.check_interval_seconds = check_interval_seconds
        self.content = content

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
        if self.conditions is not None:
            result['conditions'] = [i.to_dict() for i in self.conditions]
        if self.pending_count is not None:
            result['pendingCount'] = self.pending_count
        if self.check_interval_seconds is not None:
            result['checkIntervalSeconds'] = self.check_interval_seconds
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlarmRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('conditions') is not None:
            self.conditions = [AlarmCondition().from_dict(i) for i in m.get('conditions')]
        if m.get('pendingCount') is not None:
            self.pending_count = m.get('pendingCount')
        if m.get('checkIntervalSeconds') is not None:
            self.check_interval_seconds = m.get('checkIntervalSeconds')
        if m.get('content') is not None:
            self.content = m.get('content')
        return self
