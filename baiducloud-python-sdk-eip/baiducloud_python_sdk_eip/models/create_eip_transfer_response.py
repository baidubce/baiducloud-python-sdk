"""
Request entity for CreateEipTransferResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_eip.models.transfer_info import TransferInfo


class CreateEipTransferResponse(BceResponse):
    """
    CreateEipTransferResponse
    """

    def __init__(self, transfers=None):
        """
        Initialize CreateEipTransferResponse response.

        :param transfers: 转移信息
        :type transfers: List[TransferInfo] (optional)
        """
        super().__init__()
        self.transfers = transfers

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
        if self.transfers is not None:
            result['transfers'] = [i.to_dict() for i in self.transfers]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateEipTransferResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('transfers') is not None:
            self.transfers = [TransferInfo().from_dict(i) for i in m.get('transfers')]
        return self
