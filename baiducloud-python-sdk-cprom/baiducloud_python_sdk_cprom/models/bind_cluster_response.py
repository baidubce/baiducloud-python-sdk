"""
Request entity for BindClusterResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class BindClusterResponse(BceResponse):
    """
    BindClusterResponse
    """

    def __init__(self, binding_status=None):
        """
        Initialize BindClusterResponse response.

        :param binding_status: 绑定状态。绑定请求返回 `Binding`，解绑请求返回 `Unbinding`。
        :type binding_status: str (optional)
        """
        super().__init__()
        self.binding_status = binding_status

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
        if self.binding_status is not None:
            result['bindingStatus'] = self.binding_status
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindClusterResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bindingStatus') is not None:
            self.binding_status = m.get('bindingStatus')
        return self
