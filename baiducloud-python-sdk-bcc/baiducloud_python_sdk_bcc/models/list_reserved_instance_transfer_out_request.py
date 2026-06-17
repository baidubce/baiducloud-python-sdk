"""
Request entity for ListReservedInstanceTransferOutRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListReservedInstanceTransferOutRequest(AbstractModel):
    """
    Request entity for ListReservedInstanceTransferOutRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, marker=None, max_keys=None, reserved_instance_ids=None, transfer_record_ids=None, spec=None, status=None
    ):
        """
        Initialize ListReservedInstanceTransferOutRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param reserved_instance_ids: 通过预留实例券id列表过滤
        :type reserved_instance_ids: List[str] (optional)

        :param transfer_record_ids: 通过预留实例券转移记录id列表过滤
        :type transfer_record_ids: List[str] (optional)

        :param spec: 通过实例规格过滤
        :type spec: str (optional)

        :param status: 通过转移记录状态过滤
        :type status: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.reserved_instance_ids = reserved_instance_ids
        self.transfer_record_ids = transfer_record_ids
        self.spec = spec
        self.status = status

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
        if self.transfer_record_ids is not None:
            result['transferRecordIds'] = self.transfer_record_ids
        if self.spec is not None:
            result['spec'] = self.spec
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListReservedInstanceTransferOutRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('reservedInstanceIds') is not None:
            self.reserved_instance_ids = m.get('reservedInstanceIds')
        if m.get('transferRecordIds') is not None:
            self.transfer_record_ids = m.get('transferRecordIds')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
