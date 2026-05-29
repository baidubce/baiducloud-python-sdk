"""
Request entity for UpdateProjectRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateProjectRequest(AbstractModel):
    """
    Request entity for UpdateProjectRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, uuid, description=None):
        """
        Initialize UpdateProjectRequest request entity.

        :param uuid: 日志组UUID
        :type uuid: str (required)

        :param description: 日志组是否置顶
        :type description: bool (optional)
        """
        super().__init__()
        self.uuid = uuid
        self.description = description

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
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateProjectRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
