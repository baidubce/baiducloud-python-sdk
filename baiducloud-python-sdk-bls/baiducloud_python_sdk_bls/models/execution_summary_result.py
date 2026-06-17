"""
ExecutionSummaryResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.execution_stats import ExecutionStats


class ExecutionSummaryResult(AbstractModel):
    """
    ExecutionSummaryResult
    """

    def __init__(self, execution_stats=None, page_no=None, page_size=None, total_count=None):
        """
        Initialize ExecutionSummaryResult instance.

        :param execution_stats: 执行统计列表
        :type execution_stats: List[ExecutionStats] (optional)

        :param page_no: 第几页
        :type page_no: int (optional)

        :param page_size: 每页展示数量
        :type page_size: int (optional)

        :param total_count: 总数
        :type total_count: int (optional)
        """
        super().__init__()
        self.execution_stats = execution_stats
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count

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
        if self.execution_stats is not None:
            result['executionStats'] = [i.to_dict() for i in self.execution_stats]
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ExecutionSummaryResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('executionStats') is not None:
            self.execution_stats = [ExecutionStats().from_dict(i) for i in m.get('executionStats')]
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self
