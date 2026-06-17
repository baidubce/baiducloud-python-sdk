"""
Request entity for ListInstanceEnisResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.eni_info import EniInfo


class ListInstanceEnisResponse(BceResponse):
    """
    ListInstanceEnisResponse
    """

    def __init__(self, enis=None):
        """
        Initialize ListInstanceEnisResponse response.

        :param enis: 网卡信息列表
        :type enis: List[EniInfo] (optional)
        """
        super().__init__()
        self.enis = enis

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
        if self.enis is not None:
            result['enis'] = [i.to_dict() for i in self.enis]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListInstanceEnisResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enis') is not None:
            self.enis = [EniInfo().from_dict(i) for i in m.get('enis')]
        return self
