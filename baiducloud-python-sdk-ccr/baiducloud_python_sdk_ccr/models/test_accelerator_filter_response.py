"""
Request entity for TestAcceleratorFilterResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class TestAcceleratorFilterResponse(BceResponse):
    """
    TestAcceleratorFilterResponse
    """

    def __init__(self, matched=None):
        """
        Initialize TestAcceleratorFilterResponse response.

        :param matched: 验证是否满足按需加载规则
        :type matched: bool (optional)
        """
        super().__init__()
        self.matched = matched

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
        if self.matched is not None:
            result['matched'] = self.matched
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TestAcceleratorFilterResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('matched') is not None:
            self.matched = m.get('matched')
        return self
