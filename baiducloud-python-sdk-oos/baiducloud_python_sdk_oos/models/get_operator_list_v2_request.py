"""
Request entity for GetOperatorListV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetOperatorListV2Request(AbstractModel):
    """
    Request entity for GetOperatorListV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, page_no, page_size, locale=None, operator=None, sort=None, ascending=None):
        """
        Initialize GetOperatorListV2Request request entity.

        :param locale: locale parameter
        :type locale: str (optional)

        :param operator: 系统模板操作符过滤条件
        :type operator: object (optional)

        :param sort: 排序字段
        :type sort: str (optional)

        :param ascending: 是否升序
        :type ascending: bool (optional)

        :param page_no: 页数，从 1 开始计数
        :type page_no: int (required)

        :param page_size: 每页展示数量，最大 100
        :type page_size: int (required)
        """
        super().__init__()
        self.locale = locale
        self.operator = operator
        self.sort = sort
        self.ascending = ascending
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
        if self.operator is not None:
            result['operator'] = self.operator
        if self.sort is not None:
            result['sort'] = self.sort
        if self.ascending is not None:
            result['ascending'] = self.ascending
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
        :rtype: GetOperatorListV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('ascending') is not None:
            self.ascending = m.get('ascending')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
