"""
Request entity for StepsToObtainNodeEventsV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cce.models.step import Step


class StepsToObtainNodeEventsV2Response(BceResponse):
    """
    StepsToObtainNodeEventsV2Response
    """

    def __init__(self, status=None, steps=None, request_id=None):
        """
        Initialize StepsToObtainNodeEventsV2Response response.

        :param status: 事件类型
        :type status: str (optional)

        :param steps: 集群操作步骤
        :type steps: List[Step] (optional)

        :param request_id: 请求ID
        :type request_id: str (optional)
        """
        super().__init__()
        self.status = status
        self.steps = steps
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
        if self.status is not None:
            result['status'] = self.status
        if self.steps is not None:
            result['steps'] = [i.to_dict() for i in self.steps]
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
        :rtype: StepsToObtainNodeEventsV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('steps') is not None:
            self.steps = [Step().from_dict(i) for i in m.get('steps')]
        if m.get('requestID') is not None:
            self.request_id = m.get('requestID')
        return self
