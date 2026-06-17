"""
Request entity for FieldCapsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FieldCapsRequest(AbstractModel):
    """
    Request entity for FieldCapsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, fields):
        """
        Initialize FieldCapsRequest request entity.

        :param name: name parameter
        :type name: str (required)

        :param fields: 索引字段名称，支持*通配符模糊匹配
        :type fields: List[str] (required)
        """
        super().__init__()
        self.name = name
        self.fields = fields

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
        if self.fields is not None:
            result['fields'] = self.fields
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FieldCapsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        return self
