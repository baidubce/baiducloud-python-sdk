"""
ActionResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ActionResult(AbstractModel):
    """
    ActionResult
    """

    def __init__(self, action_id=None, action_name=None, run_id=None):
        """
        Initialize ActionResult instance.

        :param action_id: 命令ID
        :type action_id: str (optional)

        :param action_name: 命令名称，保存命令的时候返回
        :type action_name: str (optional)

        :param run_id: 执行id，仅在命令执行时返回
        :type run_id: str (optional)
        """
        super().__init__()
        self.action_id = action_id
        self.action_name = action_name
        self.run_id = run_id

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
        if self.action_id is not None:
            result['actionId'] = self.action_id
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.run_id is not None:
            result['runId'] = self.run_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ActionResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('actionId') is not None:
            self.action_id = m.get('actionId')
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('runId') is not None:
            self.run_id = m.get('runId')
        return self
