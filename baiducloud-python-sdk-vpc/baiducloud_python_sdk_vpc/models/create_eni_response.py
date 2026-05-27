"""
Request entity for CreateEniResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateEniResponse(BceResponse):
    """
    CreateEniResponse
    """

    def __init__(self, eni_id=None):
        """
        Initialize CreateEniResponse response.

        :param eni_id: 弹性网卡的ID
        :type eni_id: str (optional)
        """
        super().__init__()
        self.eni_id = eni_id

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
        if self.eni_id is not None:
            result['eniId'] = self.eni_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateEniResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')
        return self
