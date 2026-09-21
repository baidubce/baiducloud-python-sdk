"""
Request entity for ListRedisBigKeyAnalysisTasksRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListRedisBigKeyAnalysisTasksRequest(AbstractModel):
    """
    Request entity for ListRedisBigKeyAnalysisTasksRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, app_id, cluster_id=None, data_type=None, order_by=None):
        """
        Initialize ListRedisBigKeyAnalysisTasksRequest request entity.

        :param app_id: app_id parameter
        :type app_id: str (required)

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (optional)

        :param data_type: data_type parameter
        :type data_type: str (optional)

        :param order_by: order_by parameter
        :type order_by: str (optional)
        """
        super().__init__()
        self.app_id = app_id
        self.cluster_id = cluster_id
        self.data_type = data_type
        self.order_by = order_by

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListRedisBigKeyAnalysisTasksRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        return self
