"""
Request entity for RevokeReservedInstanceTransferRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RevokeReservedInstanceTransferRequest(AbstractModel):
    """
    Request entity for RevokeReservedInstanceTransferRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, transfer_record_ids):
        """
        Initialize RevokeReservedInstanceTransferRequest request entity.

        :param transfer_record_ids: 要撤销的预留实例券id列表
        :type transfer_record_ids: List[str] (required)
        """
        super().__init__()
        self.transfer_record_ids = transfer_record_ids

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
        if self.transfer_record_ids is not None:
            result['transferRecordIds'] = self.transfer_record_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RevokeReservedInstanceTransferRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('transferRecordIds') is not None:
            self.transfer_record_ids = m.get('transferRecordIds')
        return self
