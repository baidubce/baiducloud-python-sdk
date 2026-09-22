"""
Request entity for CreateParameterTemplateResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateParameterTemplateResponse(BceResponse):
    """
    CreateParameterTemplateResponse
    """

    def __init__(self, template_id=None, template_show_id=None):
        """
        Initialize CreateParameterTemplateResponse response.

        :param template_id: 参数模版数字ID
        :type template_id: int (optional)

        :param template_show_id: 参数模版展示ID
        :type template_show_id: str (optional)
        """
        super().__init__()
        self.template_id = template_id
        self.template_show_id = template_show_id

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.template_show_id is not None:
            result['templateShowId'] = self.template_show_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateParameterTemplateResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('templateShowId') is not None:
            self.template_show_id = m.get('templateShowId')
        return self
