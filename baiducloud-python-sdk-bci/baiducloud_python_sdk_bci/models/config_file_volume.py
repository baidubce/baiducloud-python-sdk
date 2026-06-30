"""
ConfigFileVolume information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bci.models.config_file_detail import ConfigFileDetail


class ConfigFileVolume(AbstractModel):
    """
    ConfigFileVolume
    """

    def __init__(self, name=None, default_mode=None, config_files=None):
        """
        Initialize ConfigFileVolume instance.

        :param name: ConfigFileVolume名称
        :type name: str (optional)

        :param default_mode: 默认权限
        :type default_mode: int (optional)

        :param config_files: ConfigFile数据卷信息
        :type config_files: List[ConfigFileDetail] (optional)
        """
        super().__init__()
        self.name = name
        self.default_mode = default_mode
        self.config_files = config_files

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
        if self.name is not None:
            result['name'] = self.name
        if self.default_mode is not None:
            result['defaultMode'] = self.default_mode
        if self.config_files is not None:
            result['configFiles'] = [i.to_dict() for i in self.config_files]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ConfigFileVolume

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('defaultMode') is not None:
            self.default_mode = m.get('defaultMode')
        if m.get('configFiles') is not None:
            self.config_files = [ConfigFileDetail().from_dict(i) for i in m.get('configFiles')]
        return self
