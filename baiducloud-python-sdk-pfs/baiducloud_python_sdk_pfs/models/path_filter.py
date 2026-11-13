"""
PathFilter information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PathFilter(AbstractModel):
    """
    PathFilter
    """

    def __init__(self, type=None, pattern=None):
        """
        Initialize PathFilter instance.

        :param type: 过滤类型。0 后缀匹配（SUFFIX）；1 路径匹配（PATH_PATTERN）
        :type type: int (optional)

        :param pattern: 匹配规则，最长1000字节。
        :type pattern: str (optional)
        """
        super().__init__()
        self.type = type
        self.pattern = pattern

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
        if self.type is not None:
            result['type'] = self.type
        if self.pattern is not None:
            result['pattern'] = self.pattern
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PathFilter

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('pattern') is not None:
            self.pattern = m.get('pattern')
        return self
