"""
Request entity for CreateDeploySetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateDeploySetResponse(BceResponse):
    """
    CreateDeploySetResponse
    """

    def __init__(self, deploy_set_ids=None):
        """
        Initialize CreateDeploySetResponse response.

        :param deploy_set_ids: 部署集Ids
        :type deploy_set_ids: List[str] (optional)
        """
        super().__init__()
        self.deploy_set_ids = deploy_set_ids

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.deploy_set_ids is not None:
            result['deploySetIds'] = self.deploy_set_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDeploySetResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('deploySetIds') is not None:
            self.deploy_set_ids = m.get('deploySetIds')
        return self
