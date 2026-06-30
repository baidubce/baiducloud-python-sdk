"""
VolumeMount information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VolumeMount(AbstractModel):
    """
    VolumeMount
    """

    def __init__(self, name=None, type=None, mount_path=None, read_only=None):
        """
        Initialize VolumeMount instance.

        :param name: 数据卷名称
        :type name: str (optional)

        :param type: 数据卷类型
        :type type: str (optional)

        :param mount_path: 容器挂载数据卷目录
        :type mount_path: str (optional)

        :param read_only: 是否只读，默认false
        :type read_only: bool (optional)
        """
        super().__init__()
        self.name = name
        self.type = type
        self.mount_path = mount_path
        self.read_only = read_only

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
        if self.type is not None:
            result['type'] = self.type
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VolumeMount

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self
