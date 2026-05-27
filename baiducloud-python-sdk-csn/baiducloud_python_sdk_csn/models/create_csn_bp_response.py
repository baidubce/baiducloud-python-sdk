"""
Request entity for CreateCsnBpResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateCsnBpResponse(BceResponse):
    """
    CreateCsnBpResponse
    """

    def __init__(self, csn_bp_id=None):
        """
        Initialize CreateCsnBpResponse response.

        :param csn_bp_id: 带宽包的ID
        :type csn_bp_id: str (optional)
        """
        super().__init__()
        self.csn_bp_id = csn_bp_id

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
        if self.csn_bp_id is not None:
            result['csnBpId'] = self.csn_bp_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateCsnBpResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnBpId') is not None:
            self.csn_bp_id = m.get('csnBpId')
        return self
