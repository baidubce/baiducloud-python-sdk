"""
DagActionModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DagActionModel(AbstractModel):
    """
    DagActionModel
    """

    def __init__(self, pause=None, resume=None):
        """
        Initialize DagActionModel instance.

        :param pause: 是否暂停
        :type pause: bool (optional)

        :param resume: 是否恢复
        :type resume: bool (optional)
        """
        super().__init__()
        self.pause = pause
        self.resume = resume

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
        if self.pause is not None:
            result['pause'] = self.pause
        if self.resume is not None:
            result['resume'] = self.resume
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DagActionModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pause') is not None:
            self.pause = m.get('pause')
        if m.get('resume') is not None:
            self.resume = m.get('resume')
        return self
