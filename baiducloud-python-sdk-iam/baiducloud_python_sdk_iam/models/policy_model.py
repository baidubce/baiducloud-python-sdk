"""
PolicyModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PolicyModel(AbstractModel):
    """
    PolicyModel
    """

    def __init__(
        self, id=None, name=None, type=None, create_time=None, attach_time=None, description=None, document=None
    ):
        """
        Initialize PolicyModel instance.

        :param id: 策略id
        :type id: str (optional)

        :param name: 策略名称
        :type name: str (optional)

        :param type: 策略类型，可选：Custom - 自定义策略；System - 系统内置策略
        :type type: str (optional)

        :param create_time: 创建时间
        :type create_time: datetime (optional)

        :param attach_time: 绑定时间
        :type attach_time: datetime (optional)

        :param description: 策略描述
        :type description: str (optional)

        :param document: 策略内容，要求为ACL格式序列化后得到的String
        :type document: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.type = type
        self.create_time = create_time
        self.attach_time = attach_time
        self.description = description
        self.document = document

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
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.attach_time is not None:
            result['attachTime'] = self.attach_time
        if self.description is not None:
            result['description'] = self.description
        if self.document is not None:
            result['document'] = self.document
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PolicyModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('attachTime') is not None:
            self.attach_time = m.get('attachTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('document') is not None:
            self.document = m.get('document')
        return self
