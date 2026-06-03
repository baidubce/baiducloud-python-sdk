"""
Request entity for ListVpcLinksResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.privatelinks import Privatelinks


class ListVpcLinksResponse(BceResponse):
    """
    ListVpcLinksResponse
    """

    def __init__(self, domain=None, items=None):
        """
        Initialize ListVpcLinksResponse response.

        :param domain: 私有网络域名
        :type domain: str (optional)

        :param items: 私有网络结果列表
        :type items: List[Privatelinks] (optional)
        """
        super().__init__()
        self.domain = domain
        self.items = items

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.items is not None:
            result['items'] = [i.to_dict() for i in self.items]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListVpcLinksResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('items') is not None:
            self.items = [Privatelinks().from_dict(i) for i in m.get('items')]
        return self
