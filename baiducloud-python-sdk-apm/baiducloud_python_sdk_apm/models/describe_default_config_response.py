"""
Request entity for DescribeDefaultConfigResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_apm.models.storage_config import StorageConfig
from baiducloud_python_sdk_apm.models.request_config import RequestConfig
from baiducloud_python_sdk_apm.models.topo_config import TopoConfig


class DescribeDefaultConfigResponse(BceResponse):
    """
    DescribeDefaultConfigResponse
    """

    def __init__(
        self, success=None, code=None, message=None, storage_config=None, request_config=None, topo_config=None
    ):
        """
        Initialize DescribeDefaultConfigResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 状态码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param storage_config: storage_config field
        :type storage_config: StorageConfig (optional)

        :param request_config: request_config field
        :type request_config: RequestConfig (optional)

        :param topo_config: topo_config field
        :type topo_config: TopoConfig (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.storage_config = storage_config
        self.request_config = request_config
        self.topo_config = topo_config

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
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.storage_config is not None:
            result['storageConfig'] = self.storage_config.to_dict()
        if self.request_config is not None:
            result['requestConfig'] = self.request_config.to_dict()
        if self.topo_config is not None:
            result['topoConfig'] = self.topo_config.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeDefaultConfigResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('storageConfig') is not None:
            self.storage_config = StorageConfig().from_dict(m.get('storageConfig'))
        if m.get('requestConfig') is not None:
            self.request_config = RequestConfig().from_dict(m.get('requestConfig'))
        if m.get('topoConfig') is not None:
            self.topo_config = TopoConfig().from_dict(m.get('topoConfig'))
        return self
