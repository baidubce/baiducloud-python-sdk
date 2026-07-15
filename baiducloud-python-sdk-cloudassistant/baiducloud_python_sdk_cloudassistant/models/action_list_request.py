"""
Request entity for ActionListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cloudassistant.models.action_filter import ActionFilter


class ActionListRequest(AbstractModel):
    """
    Request entity for ActionListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, page_no, page_size, action, locale=None, sort=None, ascending=None):
        """
        Initialize ActionListRequest request entity.

        :param locale: locale parameter
        :type locale: str (optional)

        :param page_no: 页码
        :type page_no: int (required)

        :param page_size: 页大小
        :type page_size: int (required)

        :param sort: 排序字段，可选值createTime（命令创建时间）
        :type sort: str (optional)

        :param ascending: 是否升序，默认false
        :type ascending: bool (optional)

        :param action: action parameter
        :type action: ActionFilter (required)
        """
        super().__init__()
        self.locale = locale
        self.page_no = page_no
        self.page_size = page_size
        self.sort = sort
        self.ascending = ascending
        self.action = action

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
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sort is not None:
            result['sort'] = self.sort
        if self.ascending is not None:
            result['ascending'] = self.ascending
        if self.action is not None:
            result['action'] = self.action.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ActionListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('ascending') is not None:
            self.ascending = m.get('ascending')
        if m.get('action') is not None:
            self.action = ActionFilter().from_dict(m.get('action'))
        return self
