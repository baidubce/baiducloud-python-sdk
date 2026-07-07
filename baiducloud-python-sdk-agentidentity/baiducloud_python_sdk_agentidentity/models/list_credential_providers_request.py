"""
Request entity for ListCredentialProvidersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListCredentialProvidersRequest(AbstractModel):
    """
    Request entity for ListCredentialProvidersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, page_no=None, page_size=None, type=None, name=None):
        """
        Initialize ListCredentialProvidersRequest request entity.

        :param page_no: 页码，默认 1
        :type page_no: int (optional)

        :param page_size: 每页数量，默认 10，最大 100
        :type page_size: int (optional)

        :param type: 按类型过滤：API_KEY / OAUTH2 / STS
        :type type: str (optional)

        :param name: 按名称过滤
        :type name: str (optional)
        """
        super().__init__()
        self.page_no = page_no
        self.page_size = page_size
        self.type = type
        self.name = name

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
        if self.type is not None:
            result['type'] = self.type
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListCredentialProvidersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
