"""
Request entity for ListAsGroupV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListAsGroupV2Request(AbstractModel):
    """
    Request entity for ListAsGroupV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, page_no, page_size, keyword=None, keyword_type=None, sub_keyword_type=None, order=None, order_by=None
    ):
        """
        Initialize ListAsGroupV2Request request entity.

        :param keyword: keyword parameter
        :type keyword: str (optional)

        :param keyword_type: keyword_type parameter
        :type keyword_type: str (optional)

        :param sub_keyword_type: sub_keyword_type parameter
        :type sub_keyword_type: str (optional)

        :param order: order parameter
        :type order: str (optional)

        :param order_by: order_by parameter
        :type order_by: str (optional)

        :param page_no: page_no parameter
        :type page_no: int (required)

        :param page_size: page_size parameter
        :type page_size: int (required)
        """
        super().__init__()
        self.keyword = keyword
        self.keyword_type = keyword_type
        self.sub_keyword_type = sub_keyword_type
        self.order = order
        self.order_by = order_by
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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListAsGroupV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('keywordType') is not None:
            self.keyword_type = m.get('keywordType')
        if m.get('subKeywordType') is not None:
            self.sub_keyword_type = m.get('subKeywordType')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
