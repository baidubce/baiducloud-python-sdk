"""
DatasetVersionEntry information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DatasetVersionEntry(AbstractModel):
    """
    DatasetVersionEntry
    """

    def __init__(self, id=None, version=None, description=None, storage_path=None, mount_path=None, create_user=None):
        """
        Initialize DatasetVersionEntry instance.

        :param id: 数据集版本ID。新建版本时，无需指定ID。
        :type id: str (optional)

        :param version: 版本号。新建版本时，无需指定版本号。
        :type version: str (optional)

        :param description: 版本描述
        :type description: str (optional)

        :param storage_path: 存储路径
        :type storage_path: str (optional)

        :param mount_path: 默认挂载路径
        :type mount_path: str (optional)

        :param create_user: 创建用户
        :type create_user: str (optional)
        """
        super().__init__()
        self.id = id
        self.version = version
        self.description = description
        self.storage_path = storage_path
        self.mount_path = mount_path
        self.create_user = create_user

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
        if self.id is not None:
            result['id'] = self.id
        if self.version is not None:
            result['version'] = self.version
        if self.description is not None:
            result['description'] = self.description
        if self.storage_path is not None:
            result['storagePath'] = self.storage_path
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.create_user is not None:
            result['createUser'] = self.create_user
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DatasetVersionEntry

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('storagePath') is not None:
            self.storage_path = m.get('storagePath')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        return self
