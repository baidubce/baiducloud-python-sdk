"""
Request entity for CreateGatewayLimitRulesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateGatewayLimitRulesResponse(BceResponse):
    """
    CreateGatewayLimitRulesResponse
    """

    def __init__(self, glr_id=None):
        """
        Initialize CreateGatewayLimitRulesResponse response.

        :param glr_id: 网关限速规则ID
        :type glr_id: str (optional)
        """
        super().__init__()
        self.glr_id = glr_id

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
            result['metadata'] = self.metadata
        if self.glr_id is not None:
            result['glrId'] = self.glr_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateGatewayLimitRulesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('glrId') is not None:
            self.glr_id = m.get('glrId')
        return self
