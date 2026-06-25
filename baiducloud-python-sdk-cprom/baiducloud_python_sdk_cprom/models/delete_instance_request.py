"""
Request entity for DeleteInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteInstanceRequest(AbstractModel):
    """
    Request entity for DeleteInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, delete_grafana=None):
        """
        Initialize DeleteInstanceRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param delete_grafana: delete_grafana parameter
        :type delete_grafana: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.delete_grafana = delete_grafana

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
        :rtype: DeleteInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('deleteGrafana') is not None:
            self.delete_grafana = m.get('deleteGrafana')
        return self
