"""
Request entity for QueryTheConfigurationOfAutoscalerV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cce.models.autoscaler import Autoscaler


class QueryTheConfigurationOfAutoscalerV2Response(BceResponse):
    """
    QueryTheConfigurationOfAutoscalerV2Response
    """

    def __init__(self, autoscaler=None, request_id=None):
        """
        Initialize QueryTheConfigurationOfAutoscalerV2Response response.

        :param autoscaler: autoscaler field
        :type autoscaler: Autoscaler (optional)

        :param request_id: 请求 ID，问题定位时请提供该 ID
        :type request_id: str (optional)
        """
        super().__init__()
        self.autoscaler = autoscaler
        self.request_id = request_id

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
        if self.autoscaler is not None:
            result['autoscaler'] = self.autoscaler.to_dict()
        if self.request_id is not None:
            result['requestID'] = self.request_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryTheConfigurationOfAutoscalerV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('autoscaler') is not None:
            self.autoscaler = Autoscaler().from_dict(m.get('autoscaler'))
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        return self
