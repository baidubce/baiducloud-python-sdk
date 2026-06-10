"""
Request entity for GetVolumeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetVolumeRequest(AbstractModel):
    """
    Request entity for GetVolumeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_id):
        """
        Initialize GetVolumeRequest request entity.

        :param volume_id: volume_id parameter
        :type volume_id: str (required)
        """
        super().__init__()
        self.volume_id = volume_id

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetVolumeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        return self
