"""
DownloadTaskListResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.task import Task


class DownloadTaskListResult(AbstractModel):
    """
    DownloadTaskListResult
    """

    def __init__(self, tasks=None, total=None, order_by=None, order=None, page_no=None, page_size=None):
        """
        Initialize DownloadTaskListResult instance.

        :param tasks: 下载任务列表
        :type tasks: List[Task] (optional)

        :param total: 总数
        :type total: int (optional)

        :param order_by: 排序字段
        :type order_by: str (optional)

        :param order: 排序顺序
        :type order: str (optional)

        :param page_no: 页码
        :type page_no: int (optional)

        :param page_size: 每页大小
        :type page_size: int (optional)
        """
        super().__init__()
        self.tasks = tasks
        self.total = total
        self.order_by = order_by
        self.order = order
        self.page_no = page_no
        self.page_size = page_size

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
        if self.tasks is not None:
            result['tasks'] = [i.to_dict() for i in self.tasks]
        if self.total is not None:
            result['total'] = self.total
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DownloadTaskListResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tasks') is not None:
            self.tasks = [Task().from_dict(i) for i in m.get('tasks')]
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
