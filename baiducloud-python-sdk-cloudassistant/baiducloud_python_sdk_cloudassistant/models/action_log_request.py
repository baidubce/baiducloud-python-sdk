"""
Request entity for ActionLogRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ActionLogRequest(AbstractModel):
    """
    Request entity for ActionLogRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, run_id, child_id, cursor):
        """
        Initialize ActionLogRequest request entity.

        :param run_id: 执行ID
        :type run_id: str (required)

        :param child_id: 执行ID下某一子执行ID
        :type child_id: str (required)

        :param cursor: 首次请求为0，后续翻页，填写上一次请求返回的nextCursor
        :type cursor: int (required)
        """
        super().__init__()
        self.run_id = run_id
        self.child_id = child_id
        self.cursor = cursor

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
        if self.run_id is not None:
            result['runId'] = self.run_id
        if self.child_id is not None:
            result['childId'] = self.child_id
        if self.cursor is not None:
            result['cursor'] = self.cursor
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ActionLogRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('runId') is not None:
            self.run_id = m.get('runId')
        if m.get('childId') is not None:
            self.child_id = m.get('childId')
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        return self
