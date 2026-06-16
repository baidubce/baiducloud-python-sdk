"""
Request entity for CreateAspResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateAspResponse(BceResponse):
    """
    CreateAspResponse
    """

    def __init__(self, asp_id=None):
        """
        Initialize CreateAspResponse response.

        :param asp_id: 自动快照策略ID
        :type asp_id: str (optional)
        """
        super().__init__()
        self.asp_id = asp_id

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
        if self.asp_id is not None:
            result['aspId'] = self.asp_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAspResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('aspId') is not None:
            self.asp_id = m.get('aspId')
        return self
