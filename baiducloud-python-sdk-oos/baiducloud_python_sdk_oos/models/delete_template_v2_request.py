"""
Request entity for DeleteTemplateV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteTemplateV2Request(AbstractModel):
    """
    Request entity for DeleteTemplateV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, namespace=None):
        """
        Initialize DeleteTemplateV2Request request entity.

        :param namespace: namespace parameter
        :type namespace: str (optional)

        :param id: id parameter
        :type id: str (required)
        """
        super().__init__()
        self.namespace = namespace
        self.id = id

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
        :rtype: DeleteTemplateV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self
