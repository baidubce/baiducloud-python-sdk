"""
Request entity for DeleteParameterTemplateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteParameterTemplateRequest(AbstractModel):
    """
    Request entity for DeleteParameterTemplateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, template_show_id):
        """
        Initialize DeleteParameterTemplateRequest request entity.

        :param template_show_id: template_show_id parameter
        :type template_show_id: str (required)
        """
        super().__init__()
        self.template_show_id = template_show_id

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
        :rtype: DeleteParameterTemplateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('templateShowId') is not None:
            self.template_show_id = m.get('templateShowId')
        return self
