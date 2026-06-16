"""
PassInstanceModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PassInstanceModel(AbstractModel):
    """
    PassInstanceModel
    """

    def __init__(self, application=None, instance_count=None):
        """
        Initialize PassInstanceModel instance.

        :param application: 应用名称
        :type application: str (optional)

        :param instance_count: 实例数量
        :type instance_count: int (optional)
        """
        super().__init__()
        self.application = application
        self.instance_count = instance_count

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
        if self.application is not None:
            result['application'] = self.application
        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PassInstanceModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('application') is not None:
            self.application = m.get('application')
        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')
        return self
