"""
TriggerTarget information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TriggerTarget(AbstractModel):
    """
    TriggerTarget
    """

    def __init__(self, address=None, headers=None):
        """
        Initialize TriggerTarget instance.

        :param address: 触发器被触发后访问的 URL 地址
        :type address: str (optional)

        :param headers: 自定义 Header 信息<br>Header Key 仅支持 `Authorization`
        :type headers: Dict[str, str] (optional)
        """
        super().__init__()
        self.address = address
        self.headers = headers

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
        if self.address is not None:
            result['address'] = self.address
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TriggerTarget

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self
