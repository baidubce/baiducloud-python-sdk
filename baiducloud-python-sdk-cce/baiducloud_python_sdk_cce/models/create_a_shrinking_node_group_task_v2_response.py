"""
CreateAShrinkingNodeGroupTaskV2Response information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateAShrinkingNodeGroupTaskV2Response(BceResponse):
    """
    CreateAShrinkingNodeGroupTaskV2Response
    """

    def __init__(self, task_id=None, request_id=None):
        """
        Initialize CreateAShrinkingNodeGroupTaskV2Response instance.

        :param task_id: 节点组扩容任务 ID
        :type task_id: str (optional)

        :param request_id: 请求 ID, 问题定位提供该 ID
        :type request_id: str (optional)
        """
        super().__init__()
        self.task_id = task_id
        self.request_id = request_id

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.task_id is not None:
            result['taskID'] = self.task_id
        if self.request_id is not None:
            result['requestID'] = self.request_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAShrinkingNodeGroupTaskV2Response

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('taskID') is not None:
            self.task_id = m.get('taskID')
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        return self
