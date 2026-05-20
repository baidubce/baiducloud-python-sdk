"""
PublicRecord information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PublicRecord(AbstractModel):
    """
    PublicRecord
    """

    def __init__(
        self,
        id=None,
        rr=None,
        status=None,
        type=None,
        value=None,
        ttl=None,
        line=None,
        description=None,
        priority=None,
    ):
        """
        Initialize PublicRecord instance.

        :param id: 解析记录id。
        :type id: str (optional)

        :param rr: 主机记录。
        :type rr: str (optional)

        :param status: 域名状态，包含：正常(running)、暂停中(stopped)、服务异常(failed)。
        :type status: str (optional)

        :param type: 解析记录类型，包含：“A”，“CNAME”，“MX”，“TXT”，“NS”，“AAAA”，“SRV”。
        :type type: str (optional)

        :param value: value attribute
        :type value: str (optional)

        :param ttl: 解析记录在本地DNS服务器的缓存时间（单位：秒），基础版默认300秒，普惠版默认120秒，企业版默认1秒。取值为正整数。
        :type ttl: int (optional)

        :param line: line attribute
        :type line: str (optional)

        :param description: 描述，长度不超过255个字符。
        :type description: str (optional)

        :param priority: MX记录的优先级，取值范围：[0,50]。记录类型为MX记录时返回。
        :type priority: int (optional)
        """
        super().__init__()
        self.id = id
        self.rr = rr
        self.status = status
        self.type = type
        self.value = value
        self.ttl = ttl
        self.line = line
        self.description = description
        self.priority = priority

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.rr is not None:
            result['rr'] = self.rr
        if self.status is not None:
            result['status'] = self.status
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
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PublicRecord

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('rr') is not None:
            self.rr = m.get('rr')
        if m.get('status') is not None:
            self.status = m.get('status')
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
