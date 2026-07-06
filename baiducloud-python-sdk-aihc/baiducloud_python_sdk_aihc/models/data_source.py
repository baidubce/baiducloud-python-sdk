"""
DataSource information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aihc.models.option import Option


class DataSource(AbstractModel):
    """
    DataSource
    """

    def __init__(self, type=None, name=None, source_path=None, mount_path=None, options=None):
        """
        Initialize DataSource instance.

        :param type: 数据源类型，枚举值：pfs/hostpath/dataset/bos/cfs/rapidfs；
        :type type: str (optional)

        :param name: 数据源名称，如果type类型为pfs时，此处必须填写pfs实例id / type类型为bos时，默认为空
        :type name: str (optional)

        :param source_path: source_path attribute
        :type source_path: str (optional)

        :param mount_path: 容器内挂载路径
        :type mount_path: str (optional)

        :param options: options attribute
        :type options: Option (optional)
        """
        super().__init__()
        self.type = type
        self.name = name
        self.source_path = source_path
        self.mount_path = mount_path
        self.options = options

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
        if self.name is not None:
            result['name'] = self.name
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.options is not None:
            result['options'] = self.options.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DataSource

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('options') is not None:
            self.options = Option().from_dict(m.get('options'))
        return self
