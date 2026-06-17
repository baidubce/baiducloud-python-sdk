"""
Request entity for AcceptReservedInstanceTransferRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AcceptReservedInstanceTransferRequest(AbstractModel):
    """
    Request entity for AcceptReservedInstanceTransferRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, transfer_record_id, ehc_cluster_id=None):
        """
        Initialize AcceptReservedInstanceTransferRequest request entity.

        :param transfer_record_id: 要接受的预留实例券转移记录id
        :type transfer_record_id: str (required)

        :param ehc_cluster_id: 接收roce预留实例券时可选参数，若为空则使用默认EHC集群
        :type ehc_cluster_id: str (optional)
        """
        super().__init__()
        self.transfer_record_id = transfer_record_id
        self.ehc_cluster_id = ehc_cluster_id

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
        if self.transfer_record_id is not None:
            result['transferRecordId'] = self.transfer_record_id
        if self.ehc_cluster_id is not None:
            result['ehcClusterId'] = self.ehc_cluster_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AcceptReservedInstanceTransferRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('transferRecordId') is not None:
            self.transfer_record_id = m.get('transferRecordId')
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        return self
