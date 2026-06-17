"""
TaskConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.src_config import SrcConfig

from baiducloud_python_sdk_bls.models.dest_config import DestConfig


class TaskConfig(AbstractModel):
    """
    TaskConfig
    """

    def __init__(self, src_config=None, dest_config=None):
        """
        Initialize TaskConfig instance.

        :param src_config: src_config attribute
        :type src_config: SrcConfig (optional)

        :param dest_config: dest_config attribute
        :type dest_config: DestConfig (optional)
        """
        super().__init__()
        self.src_config = src_config
        self.dest_config = dest_config

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
        if self.src_config is not None:
            result['srcConfig'] = self.src_config.to_dict()
        if self.dest_config is not None:
            result['destConfig'] = self.dest_config.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TaskConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('srcConfig') is not None:
            self.src_config = SrcConfig().from_dict(m.get('srcConfig'))
        if m.get('destConfig') is not None:
            self.dest_config = DestConfig().from_dict(m.get('destConfig'))
        return self
