"""
Request entity for CreateReservedInstanceTransferRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateReservedInstanceTransferRequest(AbstractModel):
    """
    Request entity for CreateReservedInstanceTransferRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, reserved_instance_ids, recipient_account_id):
        """
        Initialize CreateReservedInstanceTransferRequest request entity.

        :param reserved_instance_ids: 要转移的预留实例券id列表
        :type reserved_instance_ids: List[str] (required)

        :param recipient_account_id: 接收人的账号id
        :type recipient_account_id: str (required)
        """
        super().__init__()
        self.reserved_instance_ids = reserved_instance_ids
        self.recipient_account_id = recipient_account_id

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
        if self.reserved_instance_ids is not None:
            result['reservedInstanceIds'] = self.reserved_instance_ids
        if self.recipient_account_id is not None:
            result['recipientAccountId'] = self.recipient_account_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateReservedInstanceTransferRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservedInstanceIds') is not None:
            self.reserved_instance_ids = m.get('reservedInstanceIds')
        if m.get('recipientAccountId') is not None:
            self.recipient_account_id = m.get('recipientAccountId')
        return self
