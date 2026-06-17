"""
Request entity for GetVolumeResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.volume_model import VolumeModel


class GetVolumeResponse(BceResponse):
    """
    GetVolumeResponse
    """

    def __init__(self, volume=None):
        """
        Initialize GetVolumeResponse response.

        :param volume: volume field
        :type volume: VolumeModel (optional)
        """
        super().__init__()
        self.volume = volume

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
        if self.volume is not None:
            result['volume'] = self.volume.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetVolumeResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volume') is not None:
            self.volume = VolumeModel().from_dict(m.get('volume'))
        return self
