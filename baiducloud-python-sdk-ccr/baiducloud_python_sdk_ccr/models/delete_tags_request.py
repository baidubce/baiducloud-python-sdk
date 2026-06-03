"""
Request entity for DeleteTagsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteTagsRequest(AbstractModel):
    """
    Request entity for DeleteTagsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, project_name, repository_name, items):
        """
        Initialize DeleteTagsRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param project_name: project_name parameter
        :type project_name: str (required)

        :param repository_name: repository_name parameter
        :type repository_name: str (required)

        :param items: 待删除的Tag名称数组，最大100个
        :type items: List[str] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.project_name = project_name
        self.repository_name = repository_name
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
        :rtype: DeleteTagsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('repositoryName') is not None:
            self.repository_name = m.get('repositoryName')
        if m.get('items') is not None:
            self.items = m.get('items')
        return self
