"""
Request entity for GetParameterTemplateDetailsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetParameterTemplateDetailsRequest(AbstractModel):
    """
    Request entity for GetParameterTemplateDetailsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, template_id):
        """
        Initialize GetParameterTemplateDetailsRequest request entity.

        :param template_id: template_id parameter
        :type template_id: str (required)
        """
        super().__init__()
        self.template_id = template_id

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
        :rtype: GetParameterTemplateDetailsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self
