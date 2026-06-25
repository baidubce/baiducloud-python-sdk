"""
EscalateParam information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cprom.models.claim_condition import ClaimCondition

from baiducloud_python_sdk_cprom.models.notify_action import NotifyAction


class EscalateParam(AbstractModel):
    """
    EscalateParam
    """

    def __init__(self, rank=None, condition=None, notify_action=None):
        """
        Initialize EscalateParam instance.

        :param rank: 升级通知策略级别，1，2，3, xx时间未响应升级到1级->2级->3级
        :type rank: int (optional)

        :param condition: condition attribute
        :type condition: ClaimCondition (optional)

        :param notify_action: notify_action attribute
        :type notify_action: NotifyAction (optional)
        """
        super().__init__()
        self.rank = rank
        self.condition = condition
        self.notify_action = notify_action

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
        if self.rank is not None:
            result['rank'] = self.rank
        if self.condition is not None:
            result['condition'] = self.condition.to_dict()
        if self.notify_action is not None:
            result['notifyAction'] = self.notify_action.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EscalateParam

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('rank') is not None:
            self.rank = m.get('rank')
        if m.get('condition') is not None:
            self.condition = ClaimCondition().from_dict(m.get('condition'))
        if m.get('notifyAction') is not None:
            self.notify_action = NotifyAction().from_dict(m.get('notifyAction'))
        return self
