"""
Request entity for ListIdpConfigurationsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListIdpConfigurationsRequest(AbstractModel):
    """
    Request entity for ListIdpConfigurationsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_pool_id, keyword=None, page_no=None, page_size=None):
        """
        Initialize ListIdpConfigurationsRequest request entity.

        :param user_pool_id: 用户池 ID
        :type user_pool_id: str (required)

        :param keyword: 按名称模糊搜索
        :type keyword: str (optional)

        :param page_no: 页码，默认 1
        :type page_no: int (optional)

        :param page_size: 每页数量，默认 10
        :type page_size: int (optional)
        """
        super().__init__()
        self.user_pool_id = user_pool_id
        self.keyword = keyword
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
        if self.user_pool_id is not None:
            result['userPoolId'] = self.user_pool_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
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
        :rtype: ListIdpConfigurationsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userPoolId') is not None:
            self.user_pool_id = m.get('userPoolId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
