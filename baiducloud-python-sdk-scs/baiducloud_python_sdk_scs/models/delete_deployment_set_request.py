"""
Request entity for DeleteDeploymentSetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteDeploymentSetRequest(AbstractModel):
    """
    Request entity for DeleteDeploymentSetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, deploy_set_id):
        """
        Initialize DeleteDeploymentSetRequest request entity.

        :param deploy_set_id: deploy_set_id parameter
        :type deploy_set_id: str (required)
        """
        super().__init__()
        self.deploy_set_id = deploy_set_id

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
        :rtype: DeleteDeploymentSetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('deploySetId') is not None:
            self.deploy_set_id = m.get('deploySetId')
        return self
