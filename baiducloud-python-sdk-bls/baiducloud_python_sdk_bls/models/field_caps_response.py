"""
Request entity for FieldCapsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.error import Error


class FieldCapsResponse(BceResponse):
    """
    FieldCapsResponse
    """

    def __init__(self, indices=None, fields=None, error=None, status=None):
        """
        Initialize FieldCapsResponse response.

        :param indices: 索引列表，目前只有一个元素
        :type indices: List[str] (optional)

        :param fields: 索引字段，字段名称-字段类型-字段元信息的关系
        :type fields: Dict[str, Dict[str, ModelField]] (optional)

        :param error: error field
        :type error: Error (optional)

        :param status: http状态码，比如：500
        :type status: int (optional)
        """
        super().__init__()
        self.indices = indices
        self.fields = fields
        self.error = error
        self.status = status

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
        if self.indices is not None:
            result['indices'] = self.indices
        if self.fields is not None:
            result['fields'] = self.fields
        if self.error is not None:
            result['error'] = self.error.to_dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FieldCapsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('indices') is not None:
            self.indices = m.get('indices')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('error') is not None:
            self.error = Error().from_dict(m.get('error'))
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
