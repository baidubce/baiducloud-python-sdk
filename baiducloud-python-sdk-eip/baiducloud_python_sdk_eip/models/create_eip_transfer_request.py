"""
Request entity for CreateEipTransferRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateEipTransferRequest(AbstractModel):
    """
    Request entity for CreateEipTransferRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, transfer_type, transfer_resource_list, to_user_id, client_token=None):
        """
        Initialize CreateEipTransferRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param transfer_type: 转移资源类型。eip
        :type transfer_type: str (required)

        :param transfer_resource_list: 转移资源短ID列表,单次最多转移30个。
        :type transfer_resource_list: List[str] (required)

        :param to_user_id: 目标账号ID。
        :type to_user_id: str (required)
        """
        super().__init__()
        self.client_token = client_token
        self.transfer_type = transfer_type
        self.transfer_resource_list = transfer_resource_list
        self.to_user_id = to_user_id

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
        if self.transfer_type is not None:
            result['transferType'] = self.transfer_type
        if self.transfer_resource_list is not None:
            result['transferResourceList'] = self.transfer_resource_list
        if self.to_user_id is not None:
            result['toUserId'] = self.to_user_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateEipTransferRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('transferType') is not None:
            self.transfer_type = m.get('transferType')
        if m.get('transferResourceList') is not None:
            self.transfer_resource_list = m.get('transferResourceList')
        if m.get('toUserId') is not None:
            self.to_user_id = m.get('toUserId')
        return self
