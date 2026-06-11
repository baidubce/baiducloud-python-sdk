"""
Request entity for CreateADatasetV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_aihc.models.permission_entry import PermissionEntry
from baiducloud_python_sdk_aihc.models.permission_entry import PermissionEntry
from baiducloud_python_sdk_aihc.models.dataset_version_entry import DatasetVersionEntry


class CreateADatasetV2Request(AbstractModel):
    """
    Request entity for CreateADatasetV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        storage_type,
        storage_instance,
        import_format,
        visibility_scope,
        init_version_entry,
        description=None,
        owner=None,
        visibility_user=None,
        visibility_group=None,
    ):
        """
        Initialize CreateADatasetV2Request request entity.

        :param name: 数据集名称支持小写字母、数字和-，必须以小写字母开头，必须以小写字母或数字结尾，长度限制1-50。
        :type name: str (required)

        :param storage_type: 存储类型，可选项：PFS、BOS
        :type storage_type: str (required)

        :param storage_instance: 存储实例ID，对应PFS、BOS的ID
        :type storage_instance: str (required)

        :param import_format: 导入格式<br>FILE：文件<br>FOLDER：文件夹
        :type import_format: str (required)

        :param description: 数据集的描述
        :type description: str (optional)

        :param owner: 所有者，不传递时默认为创建者
        :type owner: str (optional)

        :param visibility_scope: visibility_scope parameter
        :type visibility_scope: str (required)

        :param visibility_user: visibility_user parameter
        :type visibility_user: List[PermissionEntry] (optional)

        :param visibility_group: visibility_group parameter
        :type visibility_group: List[PermissionEntry] (optional)

        :param init_version_entry: init_version_entry parameter
        :type init_version_entry: DatasetVersionEntry (required)
        """
        super().__init__()
        self.name = name
        self.storage_type = storage_type
        self.storage_instance = storage_instance
        self.import_format = import_format
        self.description = description
        self.owner = owner
        self.visibility_scope = visibility_scope
        self.visibility_user = visibility_user
        self.visibility_group = visibility_group
        self.init_version_entry = init_version_entry

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.storage_instance is not None:
            result['storageInstance'] = self.storage_instance
        if self.import_format is not None:
            result['importFormat'] = self.import_format
        if self.description is not None:
            result['description'] = self.description
        if self.owner is not None:
            result['owner'] = self.owner
        if self.visibility_scope is not None:
            result['visibilityScope'] = self.visibility_scope
        if self.visibility_user is not None:
            result['visibilityUser'] = [i.to_dict() for i in self.visibility_user]
        if self.visibility_group is not None:
            result['visibilityGroup'] = [i.to_dict() for i in self.visibility_group]
        if self.init_version_entry is not None:
            result['initVersionEntry'] = self.init_version_entry.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateADatasetV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('storageInstance') is not None:
            self.storage_instance = m.get('storageInstance')
        if m.get('importFormat') is not None:
            self.import_format = m.get('importFormat')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('visibilityScope') is not None:
            self.visibility_scope = m.get('visibilityScope')
        if m.get('visibilityUser') is not None:
            self.visibility_user = [PermissionEntry().from_dict(i) for i in m.get('visibilityUser')]
        if m.get('visibilityGroup') is not None:
            self.visibility_group = [PermissionEntry().from_dict(i) for i in m.get('visibilityGroup')]
        if m.get('initVersionEntry') is not None:
            self.init_version_entry = DatasetVersionEntry().from_dict(m.get('initVersionEntry'))
        return self
