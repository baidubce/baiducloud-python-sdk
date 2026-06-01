"""
SpanMessage information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SpanMessage(AbstractModel):
    """
    SpanMessage
    """

    def __init__(self, role=None, content=None, content_ref=None):
        """
        Initialize SpanMessage instance.

        :param role: 消息角色，如 user、assistant
        :type role: str (optional)

        :param content: 直接指定内容，content和contentRef只会有一个被设置，值可以是任意类型
        :type content: str (optional)

        :param content_ref: 通过引用路径指定内容
        :type content_ref: List[str] (optional)
        """
        super().__init__()
        self.role = role
        self.content = content
        self.content_ref = content_ref

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
        if self.role is not None:
            result['role'] = self.role
        if self.content is not None:
            result['content'] = self.content
        if self.content_ref is not None:
            result['contentRef'] = self.content_ref
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SpanMessage

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('contentRef') is not None:
            self.content_ref = m.get('contentRef')
        return self
