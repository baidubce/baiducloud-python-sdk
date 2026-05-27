"""
Request entity for AddRecordResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class AddRecordResponse(BceResponse):
    """
    AddRecordResponse
    """

    def __init__(self, record_id=None):
        """
        Initialize AddRecordResponse response.

        :param record_id: 记录的ID
        :type record_id: str (optional)
        """
        super().__init__()
        self.record_id = record_id

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
        if self.record_id is not None:
            result['recordId'] = self.record_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddRecordResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        return self
