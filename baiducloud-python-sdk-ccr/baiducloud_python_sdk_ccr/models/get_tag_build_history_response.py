"""
Request entity for GetTagBuildHistoryResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.build_history import BuildHistory


class GetTagBuildHistoryResponse(BceResponse):
    """
    GetTagBuildHistoryResponse
    """

    def __init__(self, items=None):
        """
        Initialize GetTagBuildHistoryResponse response.

        :param items: 目标Tag构建历史集合
        :type items: List[BuildHistory] (optional)
        """
        super().__init__()
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
        :rtype: GetTagBuildHistoryResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('items') is not None:
            self.items = [BuildHistory().from_dict(i) for i in m.get('items')]
        return self
