"""
Request entity for CreateCfwResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateCfwResponse(BceResponse):
    """
    CreateCfwResponse
    """

    def __init__(self, cfw_id=None):
        """
        Initialize CreateCfwResponse response.

        :param cfw_id: 创建CFW策略的id
        :type cfw_id: str (optional)
        """
        super().__init__()
        self.cfw_id = cfw_id

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
        if self.cfw_id is not None:
            result['cfwId'] = self.cfw_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateCfwResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cfwId') is not None:
            self.cfw_id = m.get('cfwId')
        return self
