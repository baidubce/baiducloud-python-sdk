"""
ResponseHeaders information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aigw.models.custom_header import CustomHeader


class ResponseHeaders(AbstractModel):
    """
    ResponseHeaders
    """

    def __init__(self, enabled=None, headers=None):
        """
        Initialize ResponseHeaders instance.

        :param enabled: 是否启用自定义响应头
        :type enabled: bool (optional)

        :param headers: 响应头列表
        :type headers: List[CustomHeader] (optional)
        """
        super().__init__()
        self.enabled = enabled
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
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.headers is not None:
            result['headers'] = [i.to_dict() for i in self.headers]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResponseHeaders

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('headers') is not None:
            self.headers = [CustomHeader().from_dict(i) for i in m.get('headers')]
        return self
