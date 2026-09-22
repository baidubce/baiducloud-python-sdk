"""
Request entity for ModifyParameterTemplateNameRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyParameterTemplateNameRequest(AbstractModel):
    """
    Request entity for ModifyParameterTemplateNameRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, template_show_id, name):
        """
        Initialize ModifyParameterTemplateNameRequest request entity.

        :param template_show_id: template_show_id parameter
        :type template_show_id: str (required)

        :param name: 新的实例名称。要求：<br> 大小写字母、数字、中文以及-_/.特殊字符，必须以字母或者中文开头，长度1-65<br>
        :type name: str (required)
        """
        super().__init__()
        self.template_show_id = template_show_id
        self.name = name

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
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyParameterTemplateNameRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('templateShowId') is not None:
            self.template_show_id = m.get('templateShowId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
