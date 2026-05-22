"""
AppPolicyForUpdate information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AppPolicyForUpdate(AbstractModel):
    """
    AppPolicyForUpdate
    """

    def __init__(self, policy_id=None, priority=None, description=None):
        """
        Initialize AppPolicyForUpdate instance.

        :param policy_id: 转发策略id。
        :type policy_id: str (optional)

        :param priority: priority attribute
        :type priority: int (optional)

        :param description: 描述信息。最大200字符。priority和description不能同时为空。
        :type description: str (optional)
        """
        super().__init__()
        self.policy_id = policy_id
        self.priority = priority
        self.description = description

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
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.priority is not None:
            result['priority'] = self.priority
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppPolicyForUpdate

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
