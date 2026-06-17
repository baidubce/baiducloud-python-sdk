"""
PolicyAction information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PolicyAction(AbstractModel):
    """
    PolicyAction
    """

    def __init__(self, notify_id=None):
        """
        Initialize PolicyAction instance.

        :param notify_id: 通知模板ID
        :type notify_id: str (optional)
        """
        super().__init__()
        self.notify_id = notify_id

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
        if self.notify_id is not None:
            result['notifyId'] = self.notify_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PolicyAction

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('notifyId') is not None:
            self.notify_id = m.get('notifyId')
        return self
