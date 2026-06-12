"""
Request entity for DescribeDatasetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_aihc.models.permission_entry import PermissionEntry
from baiducloud_python_sdk_aihc.models.permission_entry import PermissionEntry
from baiducloud_python_sdk_aihc.models.dataset_version_entry import DatasetVersionEntry


class DescribeDatasetResponse(BceResponse):
    """
    DescribeDatasetResponse
    """

    def __init__(
        self,
        id=None,
        name=None,
        storage_type=None,
        storage_instance=None,
        import_format=None,
        description=None,
        owner=None,
        owner_name=None,
        visibility_scope=None,
        visibility_user=None,
        visibility_group=None,
        permission=None,
        latest_version_id=None,
        latest_version=None,
        latest_version_entry=None,
        created_at=None,
        updated_at=None,
    ):
        """
        Initialize DescribeDatasetResponse response.

        :param id: 数据集ID
        :type id: str (optional)

        :param name: 数据集名称
        :type name: str (optional)

        :param storage_type: 存储类型PFS：并行存储PFSBOS：对象存储BOS
        :type storage_type: str (optional)

        :param storage_instance: 存储实例
        :type storage_instance: str (optional)

        :param import_format: 导入格式FILE：文件FOLDER：文件夹
        :type import_format: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param owner: 所有者
        :type owner: str (optional)

        :param owner_name: 所有者名称
        :type owner_name: str (optional)

        :param visibility_scope: 可见范围ALL_PEOPLE：所有人可见ONLY_OWNER：仅所有者可读写USER_GROUP：指定范围可用
        :type visibility_scope: str (optional)

        :param visibility_user: visibility_user field
        :type visibility_user: List[PermissionEntry] (optional)

        :param visibility_group: visibility_group field
        :type visibility_group: List[PermissionEntry] (optional)

        :param permission: 当前用户拥有的读写权限：r：只读rw：读写
        :type permission: str (optional)

        :param latest_version_id: 最新版本ID
        :type latest_version_id: str (optional)

        :param latest_version: 最新版本号
        :type latest_version: str (optional)

        :param latest_version_entry: latest_version_entry field
        :type latest_version_entry: DatasetVersionEntry (optional)

        :param created_at: 创建时间
        :type created_at: str (optional)

        :param updated_at: 更新时间
        :type updated_at: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.storage_type = storage_type
        self.storage_instance = storage_instance
        self.import_format = import_format
        self.description = description
        self.owner = owner
        self.owner_name = owner_name
        self.visibility_scope = visibility_scope
        self.visibility_user = visibility_user
        self.visibility_group = visibility_group
        self.permission = permission
        self.latest_version_id = latest_version_id
        self.latest_version = latest_version
        self.latest_version_entry = latest_version_entry
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.id is not None:
            result['id'] = self.id
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
        if self.owner_name is not None:
            result['ownerName'] = self.owner_name
        if self.visibility_scope is not None:
            result['visibilityScope'] = self.visibility_scope
        if self.visibility_user is not None:
            result['visibilityUser'] = [i.to_dict() for i in self.visibility_user]
        if self.visibility_group is not None:
            result['visibilityGroup'] = [i.to_dict() for i in self.visibility_group]
        if self.permission is not None:
            result['permission'] = self.permission
        if self.latest_version_id is not None:
            result['latestVersionId'] = self.latest_version_id
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.latest_version_entry is not None:
            result['latestVersionEntry'] = self.latest_version_entry.to_dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeDatasetResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
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
        if m.get('ownerName') is not None:
            self.owner_name = m.get('ownerName')
        if m.get('visibilityScope') is not None:
            self.visibility_scope = m.get('visibilityScope')
        if m.get('visibilityUser') is not None:
            self.visibility_user = [PermissionEntry().from_dict(i) for i in m.get('visibilityUser')]
        if m.get('visibilityGroup') is not None:
            self.visibility_group = [PermissionEntry().from_dict(i) for i in m.get('visibilityGroup')]
        if m.get('permission') is not None:
            self.permission = m.get('permission')
        if m.get('latestVersionId') is not None:
            self.latest_version_id = m.get('latestVersionId')
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('latestVersionEntry') is not None:
            self.latest_version_entry = DatasetVersionEntry().from_dict(m.get('latestVersionEntry'))
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self
