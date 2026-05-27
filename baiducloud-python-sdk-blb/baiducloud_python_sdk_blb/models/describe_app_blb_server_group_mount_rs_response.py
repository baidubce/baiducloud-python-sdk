"""
DescribeAppBlbServerGroupMountRsResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_blb.models.app_backend_server import AppBackendServer


class DescribeAppBlbServerGroupMountRsResponse(BceResponse):
    """
    DescribeAppBlbServerGroupMountRsResponse
    """

    def __init__(self, backend_server_list=None):
        """
        Initialize DescribeAppBlbServerGroupMountRsResponse instance.

        :param backend_server_list: 包含查询结果的列表
        :type backend_server_list: List[AppBackendServer] (optional)
        """
        super().__init__()
        self.backend_server_list = backend_server_list

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.backend_server_list is not None:
            result['backendServerList'] = [i.to_dict() for i in self.backend_server_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAppBlbServerGroupMountRsResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('backendServerList') is not None:
            self.backend_server_list = [AppBackendServer().from_dict(i) for i in m.get('backendServerList')]
        return self
