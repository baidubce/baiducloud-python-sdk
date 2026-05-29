"""
ProjectListResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.project import Project

from baiducloud_python_sdk_bls.models.project import Project


class ProjectListResult(AbstractModel):
    """
    ProjectListResult
    """

    def __init__(
        self, order=None, order_by=None, page_no=None, page_size=None, total=None, default=None, projects=None
    ):
        """
        Initialize ProjectListResult instance.

        :param order: 排序规则，desc为降序，asc为升序
        :type order: str (optional)

        :param order_by: 排序字段
        :type order_by: str (optional)

        :param page_no: 起始页码
        :type page_no: int (optional)

        :param page_size: 每页显示数据大小
        :type page_size: int (optional)

        :param total: 总数目
        :type total: int (optional)

        :param default: default attribute
        :type default: Project (optional)

        :param projects: 日志组列表
        :type projects: List[Project] (optional)
        """
        super().__init__()
        self.order = order
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size
        self.total = total
        self.default = default
        self.projects = projects

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
        if self.order is not None:
            result['order'] = self.order
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        if self.default is not None:
            result['default'] = self.default.to_dict()
        if self.projects is not None:
            result['projects'] = [i.to_dict() for i in self.projects]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ProjectListResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('default') is not None:
            self.default = Project().from_dict(m.get('default'))
        if m.get('projects') is not None:
            self.projects = [Project().from_dict(i) for i in m.get('projects')]
        return self
