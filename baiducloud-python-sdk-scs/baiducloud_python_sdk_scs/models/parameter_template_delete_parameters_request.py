"""
Request entity for ParameterTemplateDeleteParametersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ParameterTemplateDeleteParametersRequest(AbstractModel):
    """
    Request entity for ParameterTemplateDeleteParametersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, template_show_id, parameters):
        """
        Initialize ParameterTemplateDeleteParametersRequest request entity.

        :param template_show_id: template_show_id parameter
        :type template_show_id: str (required)

        :param parameters: 要删除的参数名称集合
        :type parameters: List[str] (required)
        """
        super().__init__()
        self.template_show_id = template_show_id
        self.parameters = parameters

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
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ParameterTemplateDeleteParametersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('templateShowId') is not None:
            self.template_show_id = m.get('templateShowId')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self
