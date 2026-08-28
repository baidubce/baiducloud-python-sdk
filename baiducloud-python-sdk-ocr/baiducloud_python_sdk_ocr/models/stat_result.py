"""
StatResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class StatResult(AbstractModel):
    """
    StatResult
    """

    def __init__(self, all=None, corrected=None, correcting=None):
        """
        Initialize StatResult instance.

        :param all: 本次批改任务的题目总数
        :type all: int (optional)

        :param corrected: 已完成批改的题目数量
        :type corrected: int (optional)

        :param correcting: 批改中的题目数量
        :type correcting: int (optional)
        """
        super().__init__()
        self.all = all
        self.corrected = corrected
        self.correcting = correcting

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
        if self.all is not None:
            result['all'] = self.all
        if self.corrected is not None:
            result['corrected'] = self.corrected
        if self.correcting is not None:
            result['correcting'] = self.correcting
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: StatResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('corrected') is not None:
            self.corrected = m.get('corrected')
        if m.get('correcting') is not None:
            self.correcting = m.get('correcting')
        return self
