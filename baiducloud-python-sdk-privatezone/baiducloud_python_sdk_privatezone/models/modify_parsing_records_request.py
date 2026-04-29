"""
Request entity for ModifyParsingRecordsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyParsingRecordsRequest(AbstractModel):
    """
    Request entity for ModifyParsingRecordsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, record_id, rr, value, type, client_token=None, ttl=None, priority=None, description=None):
        """
        Initialize ModifyParsingRecordsRequest request entity.

        :param record_id: record_id parameter
        :type record_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param rr: 主机记录
        :type rr: str (required)

        :param value: 记录值
        :type value: str (required)

        :param type: 解析记录类型，目前支持A, AAAA,CNAME, TXT, MX, PTR, SRV
        :type type: str (required)

        :param ttl: 生存时间，值为[5,24*3600]，默认为60
        :type ttl: int (optional)

        :param priority: MX记录的优先级，取值范围：[0,100]。记录类型为MX记录时，此参数必选。
        :type priority: int (optional)

        :param description: 描述
        :type description: str (optional)
        """
        super().__init__()
        self.record_id = record_id
        self.client_token = client_token
        self.rr = rr
        self.value = value
        self.type = type
        self.ttl = ttl
        self.priority = priority
        self.description = description

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
        if self.rr is not None:
            result['rr'] = self.rr
        if self.value is not None:
            result['value'] = self.value
        if self.type is not None:
            result['type'] = self.type
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.priority is not None:
            result['priority'] = self.priority
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyParsingRecordsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('rr') is not None:
            self.rr = m.get('rr')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
