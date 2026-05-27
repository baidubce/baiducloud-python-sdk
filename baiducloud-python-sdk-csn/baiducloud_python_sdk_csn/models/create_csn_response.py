"""
Request entity for CreateCsnResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateCsnResponse(BceResponse):
    """
    CreateCsnResponse
    """

    def __init__(self, csn_id=None):
        """
        Initialize CreateCsnResponse response.

        :param csn_id: 云智能网的ID
        :type csn_id: str (optional)
        """
        super().__init__()
        self.csn_id = csn_id

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
        if self.csn_id is not None:
            result['csnId'] = self.csn_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateCsnResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnId') is not None:
            self.csn_id = m.get('csnId')
        return self
