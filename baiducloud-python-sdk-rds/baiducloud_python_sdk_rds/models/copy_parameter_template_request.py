"""
Request entity for CopyParameterTemplateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CopyParameterTemplateRequest(AbstractModel):
    """
    Request entity for CopyParameterTemplateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, desc, template_id):
        """
        Initialize CopyParameterTemplateRequest request entity.

        :param name: 复制后模板的名称。
        :type name: str (required)

        :param desc: 复制后模板的备注。
        :type desc: str (required)

        :param template_id: 复制的模板 ID。
        :type template_id: str (required)
        """
        super().__init__()
        self.name = name
        self.desc = desc
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
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CopyParameterTemplateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self
