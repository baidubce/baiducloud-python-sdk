"""
Request entity for DoesTheInstanceSupportEnablingAutomaticExpansionResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DoesTheInstanceSupportEnablingAutomaticExpansionResponse(BceResponse):
    """
    DoesTheInstanceSupportEnablingAutomaticExpansionResponse
    """

    def __init__(self, support_enable_disk_auto_resize=None):
        """
        Initialize DoesTheInstanceSupportEnablingAutomaticExpansionResponse response.

        :param support_enable_disk_auto_resize: 实例是否支持启用存储自动扩容，0表示不支持，1表示支持
        :type support_enable_disk_auto_resize: int (optional)
        """
        super().__init__()
        self.support_enable_disk_auto_resize = support_enable_disk_auto_resize

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
        if self.support_enable_disk_auto_resize is not None:
            result['supportEnableDiskAutoResize'] = self.support_enable_disk_auto_resize
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DoesTheInstanceSupportEnablingAutomaticExpansionResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('supportEnableDiskAutoResize') is not None:
            self.support_enable_disk_auto_resize = m.get('supportEnableDiskAutoResize')
        return self
