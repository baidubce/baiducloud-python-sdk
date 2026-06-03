"""
Request entity for CreateL2PolicyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateL2PolicyResponse(BceResponse):
    """
    CreateL2PolicyResponse
    """

    def __init__(self, request_id=None, policy_id=None):
        """
        Initialize CreateL2PolicyResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type request_id: str (optional)

        :param policy_id: 对应的policyId
        :type policy_id: str (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.policy_id = policy_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateL2PolicyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        return self
