"""
TensorboardConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TensorboardConfig(AbstractModel):
    """
    TensorboardConfig
    """

    def __init__(self, enable=None, log_path=None):
        """
        Initialize TensorboardConfig instance.

        :param enable: 否
        :type enable: bool (optional)

        :param log_path: 否
        :type log_path: str (optional)
        """
        super().__init__()
        self.enable = enable
        self.log_path = log_path

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
        if self.enable is not None:
            result['enable'] = self.enable
        if self.log_path is not None:
            result['logPath'] = self.log_path
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TensorboardConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('logPath') is not None:
            self.log_path = m.get('logPath')
        return self
