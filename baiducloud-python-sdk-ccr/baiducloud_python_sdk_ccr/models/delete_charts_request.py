"""
Request entity for DeleteChartsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteChartsRequest(AbstractModel):
    """
    Request entity for DeleteChartsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, project_name, items):
        """
        Initialize DeleteChartsRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param project_name: project_name parameter
        :type project_name: str (required)

        :param items: Chart名称数组
        :type items: List[str] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.project_name = project_name
        self.items = items

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
        if self.items is not None:
            result['items'] = self.items
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteChartsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('items') is not None:
            self.items = m.get('items')
        return self
