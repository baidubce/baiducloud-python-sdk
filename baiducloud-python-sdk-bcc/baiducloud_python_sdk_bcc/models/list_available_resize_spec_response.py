"""
Request entity for ListAvailableResizeSpecResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ListAvailableResizeSpecResponse(BceResponse):
    """
    ListAvailableResizeSpecResponse
    """

    def __init__(self, spec_list=None):
        """
        Initialize ListAvailableResizeSpecResponse response.

        :param spec_list: 可变配规格列表
        :type spec_list: List[str] (optional)
        """
        super().__init__()
        self.spec_list = spec_list

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
        if self.spec_list is not None:
            result['specList'] = self.spec_list
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListAvailableResizeSpecResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('specList') is not None:
            self.spec_list = m.get('specList')
        return self
