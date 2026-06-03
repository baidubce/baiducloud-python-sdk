"""
Request entity for ListInstancesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListInstancesRequest(AbstractModel):
    """
    Request entity for ListInstancesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, page_no=None, page_size=None, keyword_type=None, keyword=None, acrossregion=None):
        """
        Initialize ListInstancesRequest request entity.

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)

        :param keyword_type: keyword_type parameter
        :type keyword_type: str (optional)

        :param keyword: keyword parameter
        :type keyword: str (optional)

        :param acrossregion: acrossregion parameter
        :type acrossregion: str (optional)
        """
        super().__init__()
        self.page_no = page_no
        self.page_size = page_size
        self.keyword_type = keyword_type
        self.keyword = keyword
        self.acrossregion = acrossregion

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
        :rtype: ListInstancesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('keywordType') is not None:
            self.keyword_type = m.get('keywordType')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('acrossregion') is not None:
            self.acrossregion = m.get('acrossregion')
        return self
