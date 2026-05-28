"""
Request entity for CreateRecordRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateRecordRequest(AbstractModel):
    """
    Request entity for CreateRecordRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, zone_name, rr, type, value, client_token=None, ttl=None, line=None, description=None, priority=None
    ):
        """
        Initialize CreateRecordRequest request entity.

        :param zone_name: zone_name parameter
        :type zone_name: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param rr: 主机记录，例如“www”。记录值和zone的name长度加在一起不能超过255字符。
        :type rr: str (required)

        :param type: 解析记录类型，包含：“A”, “CNAME”, “MX”, “TXT”, “NS”, “AAAA”, “SRV”。
        :type type: str (required)

        :param value: value parameter
        :type value: str (required)

        :param ttl: 解析记录在本地DNS服务器的缓存时间（单位：秒），基础版默认300秒，普惠版默认120秒，企业版默认1秒。取值为正整数。
        :type ttl: int (optional)

        :param line: line parameter
        :type line: str (optional)

        :param description: 描述，长度不超过255个字符。
        :type description: str (optional)

        :param priority: MX记录的优先级，取值范围：[0,50]。记录类型为MX记录时，此参数必选。
        :type priority: int (optional)
        """
        super().__init__()
        self.zone_name = zone_name
        self.client_token = client_token
        self.rr = rr
        self.type = type
        self.value = value
        self.ttl = ttl
        self.line = line
        self.description = description
        self.priority = priority

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
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.line is not None:
            result['line'] = self.line
        if self.description is not None:
            result['description'] = self.description
        if self.priority is not None:
            result['priority'] = self.priority
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateRecordRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('rr') is not None:
            self.rr = m.get('rr')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('line') is not None:
            self.line = m.get('line')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        return self
