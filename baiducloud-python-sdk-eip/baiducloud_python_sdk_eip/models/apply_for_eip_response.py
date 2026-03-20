"""
Request entity for ApplyForEipResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ApplyForEipResponse(BceResponse):
    """
    ApplyForEipResponse
    """

    def __init__(self, eip=None):
        """
        Initialize ApplyForEipResponse response.

        :param eip: 分配的EIP地址
        :type eip: str (optional)
        """
        super().__init__()
        self.eip = eip

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
        if self.eip is not None:
            result['eip'] = self.eip
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ApplyForEipResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        return self
