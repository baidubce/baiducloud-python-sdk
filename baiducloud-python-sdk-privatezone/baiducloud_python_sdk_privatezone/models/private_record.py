"""
PrivateRecord information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PrivateRecord(AbstractModel):
    """
    PrivateRecord
    """

    def __init__(
        self, record_id=None, rr=None, value=None, status=None, type=None, ttl=None, priority=None, description=None
    ):
        """
        Initialize PrivateRecord instance.

        :param record_id: 解析记录的ID
        :type record_id: str (optional)

        :param rr: 主机记录
        :type rr: str (optional)

        :param value: 记录值
        :type value: str (optional)

        :param status: 解析记录状态
        :type status: str (optional)

        :param type: 解析记录的类型
        :type type: str (optional)

        :param ttl: 生存时间，默认为60
        :type ttl: int (optional)

        :param priority: MX记录优先级，其他类型该值为0
        :type priority: int (optional)

        :param description: 描述
        :type description: str (optional)
        """
        super().__init__()
        self.record_id = record_id
        self.rr = rr
        self.value = value
        self.status = status
        self.type = type
        self.ttl = ttl
        self.priority = priority
        self.description = description

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
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.rr is not None:
            result['rr'] = self.rr
        if self.value is not None:
            result['value'] = self.value
        if self.status is not None:
            result['status'] = self.status
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
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PrivateRecord

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('rr') is not None:
            self.rr = m.get('rr')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
