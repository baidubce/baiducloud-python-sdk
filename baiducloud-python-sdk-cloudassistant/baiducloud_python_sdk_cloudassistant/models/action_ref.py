"""
ActionRef information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ActionRef(AbstractModel):
    """
    ActionRef
    """

    def __init__(self, ref=None):
        """
        Initialize ActionRef instance.

        :param ref: 命令ID，创建执行时必须指定引用的那个命令
        :type ref: str (optional)
        """
        super().__init__()
        self.ref = ref

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
        if self.ref is not None:
            result['ref'] = self.ref
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ActionRef

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ref') is not None:
            self.ref = m.get('ref')
        return self
