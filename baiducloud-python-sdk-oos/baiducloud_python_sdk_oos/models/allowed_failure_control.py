"""
AllowedFailureControl information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AllowedFailureControl(AbstractModel):
    """
    AllowedFailureControl
    """

    def __init__(self, ratio=None, count=None):
        """
        Initialize AllowedFailureControl instance.

        :param ratio: 允许失败比例，取值 [0,1]
        :type ratio: float (optional)

        :param count: 允许失败个数；ratio 与 count 不能同时设置
        :type count: int (optional)
        """
        super().__init__()
        self.ratio = ratio
        self.count = count

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
        if self.ratio is not None:
            result['ratio'] = self.ratio
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AllowedFailureControl

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self
