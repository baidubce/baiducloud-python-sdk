"""
Request entity for GetTemplateDetailV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetTemplateDetailV2Request(AbstractModel):
    """
    Request entity for GetTemplateDetailV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id=None, name=None, type=None, locale=None):
        """
        Initialize GetTemplateDetailV2Request request entity.

        :param id: id parameter
        :type id: str (optional)

        :param name: name parameter
        :type name: str (optional)

        :param type: type parameter
        :type type: str (optional)

        :param locale: locale parameter
        :type locale: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.type = type
        self.locale = locale

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
        :rtype: GetTemplateDetailV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        return self
