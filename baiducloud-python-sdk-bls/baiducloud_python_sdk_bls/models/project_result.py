"""
ProjectResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.project import Project


class ProjectResult(AbstractModel):
    """
    ProjectResult
    """

    def __init__(self, project=None):
        """
        Initialize ProjectResult instance.

        :param project: project attribute
        :type project: Project (optional)
        """
        super().__init__()
        self.project = project

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.project is not None:
            result['project'] = self.project.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ProjectResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('project') is not None:
            self.project = Project().from_dict(m.get('project'))
        return self
