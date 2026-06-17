"""
Request entity for BulkDeleteLogShipperRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BulkDeleteLogShipperRequest(AbstractModel):
    """
    Request entity for BulkDeleteLogShipperRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, log_shipper_ids):
        """
        Initialize BulkDeleteLogShipperRequest request entity.

        :param log_shipper_ids: 批量任务ID
        :type log_shipper_ids: List[str] (required)
        """
        super().__init__()
        self.log_shipper_ids = log_shipper_ids

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
        if self.log_shipper_ids is not None:
            result['logShipperIDs'] = self.log_shipper_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BulkDeleteLogShipperRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logShipperIDs') is not None:
            self.log_shipper_ids = m.get('logShipperIDs')
        return self
