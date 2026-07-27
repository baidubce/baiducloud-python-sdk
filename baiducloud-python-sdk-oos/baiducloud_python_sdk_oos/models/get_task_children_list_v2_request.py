"""
Request entity for GetTaskChildrenListV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetTaskChildrenListV2Request(AbstractModel):
    """
    Request entity for GetTaskChildrenListV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, page_no, page_size, locale=None, execution_id=None, task_id=None, states=None):
        """
        Initialize GetTaskChildrenListV2Request request entity.

        :param locale: locale parameter
        :type locale: str (optional)

        :param execution_id: 执行（Execution）ID
        :type execution_id: str (optional)

        :param task_id: 任务（Task）ID
        :type task_id: str (optional)

        :param states: 按state进行筛选，选填，若未设置，返回所有状态的子执行
        :type states: List[str] (optional)

        :param page_no: 页数，从 1 开始计数
        :type page_no: int (required)

        :param page_size: 每页展示数量，最大值 100，最小值 1
        :type page_size: int (required)
        """
        super().__init__()
        self.locale = locale
        self.execution_id = execution_id
        self.task_id = task_id
        self.states = states
        self.page_no = page_no
        self.page_size = page_size

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
        if self.execution_id is not None:
            result['executionId'] = self.execution_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.states is not None:
            result['states'] = self.states
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetTaskChildrenListV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        if m.get('executionId') is not None:
            self.execution_id = m.get('executionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('states') is not None:
            self.states = m.get('states')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
