"""
Request entity for GetParameterTemplateListResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rds.models.template import Template


class GetParameterTemplateListResponse(BceResponse):
    """
    GetParameterTemplateListResponse
    """

    def __init__(self, list=None, page=None, perpage=None, total=None):
        """
        Initialize GetParameterTemplateListResponse response.

        :param list: 参数模板列表。
        :type list: List[Template] (optional)

        :param page: 当前页号。
        :type page: int (optional)

        :param perpage: 每页数量。
        :type perpage: int (optional)

        :param total: 总数。
        :type total: int (optional)
        """
        super().__init__()
        self.list = list
        self.page = page
        self.perpage = perpage
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
        if self.list is not None:
            result['list'] = [i.to_dict() for i in self.list]
        if self.page is not None:
            result['page'] = self.page
        if self.perpage is not None:
            result['perpage'] = self.perpage
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
        :rtype: GetParameterTemplateListResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('list') is not None:
            self.list = [Template().from_dict(i) for i in m.get('list')]
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('perpage') is not None:
            self.perpage = m.get('perpage')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self
