"""
Request entity for GetRedisBigKeyAnalysisResultRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetRedisBigKeyAnalysisResultRequest(AbstractModel):
    """
    Request entity for GetRedisBigKeyAnalysisResultRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, app_id, page_size=None):
        """
        Initialize GetRedisBigKeyAnalysisResultRequest request entity.

        :param app_id: app_id parameter
        :type app_id: str (required)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.app_id = app_id
        self.page_size = page_size

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
        :rtype: GetRedisBigKeyAnalysisResultRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
