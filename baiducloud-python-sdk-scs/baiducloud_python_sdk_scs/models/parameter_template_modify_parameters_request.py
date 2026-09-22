"""
Request entity for ParameterTemplateModifyParametersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.parameters import Parameters


class ParameterTemplateModifyParametersRequest(AbstractModel):
    """
    Request entity for ParameterTemplateModifyParametersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, template_show_id, parameters):
        """
        Initialize ParameterTemplateModifyParametersRequest request entity.

        :param template_show_id: template_show_id parameter
        :type template_show_id: str (required)

        :param parameters: 要添加的参数集合
        :type parameters: List[Parameters] (required)
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
            result['parameters'] = [i.to_dict() for i in self.parameters]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ParameterTemplateModifyParametersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('templateShowId') is not None:
            self.template_show_id = m.get('templateShowId')
        if m.get('parameters') is not None:
            self.parameters = [Parameters().from_dict(i) for i in m.get('parameters')]
        return self
