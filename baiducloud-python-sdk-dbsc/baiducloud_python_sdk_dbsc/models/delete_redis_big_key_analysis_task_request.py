"""
Request entity for DeleteRedisBigKeyAnalysisTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteRedisBigKeyAnalysisTaskRequest(AbstractModel):
    """
    Request entity for DeleteRedisBigKeyAnalysisTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ids, app_id):
        """
        Initialize DeleteRedisBigKeyAnalysisTaskRequest request entity.

        :param ids: ids parameter
        :type ids: List (required)

        :param app_id: 集群ID
        :type app_id: str (required)
        """
        super().__init__()
        self.ids = ids
        self.app_id = app_id

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
        if self.app_id is not None:
            result['appId'] = self.app_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteRedisBigKeyAnalysisTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        return self
