"""
Request entity for GetTimeWindowResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.maintain_time import MaintainTime


class GetTimeWindowResponse(BceResponse):
    """
    GetTimeWindowResponse
    """

    def __init__(self, maintain_time=None):
        """
        Initialize GetTimeWindowResponse response.

        :param maintain_time: maintain_time field
        :type maintain_time: MaintainTime (optional)
        """
        super().__init__()
        self.maintain_time = maintain_time

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
        if self.maintain_time is not None:
            result['maintainTime'] = self.maintain_time.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetTimeWindowResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('maintainTime') is not None:
            self.maintain_time = MaintainTime().from_dict(m.get('maintainTime'))
        return self
