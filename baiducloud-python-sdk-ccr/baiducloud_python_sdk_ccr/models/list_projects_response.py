"""
Request entity for ListProjectsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.project import Project


class ListProjectsResponse(BceResponse):
    """
    ListProjectsResponse
    """

    def __init__(self, page_no=None, page_size=None, projects=None, total=None):
        """
        Initialize ListProjectsResponse response.

        :param page_no: 当前页
        :type page_no: int (optional)

        :param page_size: 每页记录数
        :type page_size: int (optional)

        :param projects: 命名空间列表
        :type projects: List[Project] (optional)

        :param total: 用户命名空间总数
        :type total: int (optional)
        """
        super().__init__()
        self.page_no = page_no
        self.page_size = page_size
        self.projects = projects
        self.total = total

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.projects is not None:
            result['projects'] = [i.to_dict() for i in self.projects]
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListProjectsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projects') is not None:
            self.projects = [Project().from_dict(i) for i in m.get('projects')]
        if m.get('total') is not None:
            self.total = m.get('total')
        return self
