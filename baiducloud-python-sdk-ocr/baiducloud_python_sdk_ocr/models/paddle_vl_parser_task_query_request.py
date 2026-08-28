"""
Request entity for PaddleVlParserTaskQueryRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PaddleVlParserTaskQueryRequest(AbstractModel):
    """
    Request entity for PaddleVlParserTaskQueryRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, task_id):
        """
        Initialize PaddleVlParserTaskQueryRequest request entity.

        :param task_id: 发送提交请求时返回的task_id
        :type task_id: str (required)
        """
        super().__init__()
        self.task_id = task_id

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
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PaddleVlParserTaskQueryRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self
