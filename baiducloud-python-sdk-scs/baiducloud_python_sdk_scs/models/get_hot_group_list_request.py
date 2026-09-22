"""
Request entity for GetHotGroupListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetHotGroupListRequest(AbstractModel):
    """
    Request entity for GetHotGroupListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, page_size, page_no):
        """
        Initialize GetHotGroupListRequest request entity.

        :param page_size: 每页数量
        :type page_size: int (required)

        :param page_no: 页码
        :type page_no: int (required)
        """
        super().__init__()
        self.page_size = page_size
        self.page_no = page_no

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
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetHotGroupListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        return self
