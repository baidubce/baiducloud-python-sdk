"""
Request entity for BatchGetLogStoreRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.log_store_batch_request import LogStoreBatchRequest


class BatchGetLogStoreRequest(AbstractModel):
    """
    Request entity for BatchGetLogStoreRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, log_stores):
        """
        Initialize BatchGetLogStoreRequest request entity.

        :param log_stores: 待查询的日志集，每次最大查询100个
        :type log_stores: List[LogStoreBatchRequest] (required)
        """
        super().__init__()
        self.log_stores = log_stores

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
        if self.log_stores is not None:
            result['LogStores'] = [i.to_dict() for i in self.log_stores]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchGetLogStoreRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('LogStores') is not None:
            self.log_stores = [LogStoreBatchRequest().from_dict(i) for i in m.get('LogStores')]
        return self
