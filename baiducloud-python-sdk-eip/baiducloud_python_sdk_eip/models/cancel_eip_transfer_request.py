"""
Request entity for CancelEipTransferRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CancelEipTransferRequest(AbstractModel):
    """
    Request entity for CancelEipTransferRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, transfer_id_list, client_token=None):
        """
        Initialize CancelEipTransferRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param transfer_id_list: 转移资源短ID列表,单次最多接收30个。
        :type transfer_id_list: List[str] (required)
        """
        super().__init__()
        self.client_token = client_token
        self.transfer_id_list = transfer_id_list

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
        if self.transfer_id_list is not None:
            result['transferIdList'] = self.transfer_id_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CancelEipTransferRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('transferIdList') is not None:
            self.transfer_id_list = m.get('transferIdList')
        return self
