"""
ListInstancesByInstanceGroupIDPage information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListInstancesByInstanceGroupIDPage(AbstractModel):
    """
    ListInstancesByInstanceGroupIDPage
    """

    def __init__(self, page_no=None, page_size=None, total_count=None, list=None):
        """
        Initialize ListInstancesByInstanceGroupIDPage instance.

        :param page_no:
        :type page_no: int (optional)

        :param page_size:
        :type page_size: int (optional)

        :param total_count:
        :type total_count: int (optional)

        :param list:
        :type list: List[object] (optional)
        """
        super().__init__()
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.list = list

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
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.list is not None:
            result['list'] = self.list
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListInstancesByInstanceGroupIDPage

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('list') is not None:
            self.list = m.get('list')
        return self
