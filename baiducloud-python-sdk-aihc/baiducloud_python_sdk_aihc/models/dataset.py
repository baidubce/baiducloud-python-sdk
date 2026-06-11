"""
Dataset information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aihc.models.permission_entry import PermissionEntry

from baiducloud_python_sdk_aihc.models.permission_entry import PermissionEntry


class Dataset(AbstractModel):
    """
    Dataset
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
        created_at=None,
        updated_at=None,
    ):
        """
        Initialize Dataset instance.

        :param id: 是
        :type id: str (optional)

        :param name: 是
        :type name: str (optional)

        :param storage_type: 是
        :type storage_type: str (optional)

        :param storage_instance: 是
        :type storage_instance: str (optional)

        :param import_format: 是
        :type import_format: str (optional)

        :param description: 否
        :type description: str (optional)

        :param owner: 是
        :type owner: str (optional)

        :param owner_name: 是
        :type owner_name: str (optional)

        :param visibility_scope: 是
        :type visibility_scope: str (optional)

        :param visibility_user: 否
        :type visibility_user: List[PermissionEntry] (optional)

        :param visibility_group: 否
        :type visibility_group: List[PermissionEntry] (optional)

        :param permission: 是
        :type permission: str (optional)

        :param latest_version_id: 否
        :type latest_version_id: str (optional)

        :param latest_version: 否
        :type latest_version: str (optional)

        :param created_at: 是
        :type created_at: str (optional)

        :param updated_at: 是
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
        self.created_at = created_at
        self.updated_at = updated_at

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
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Dataset

        :raises TypeError: If input is not a dictionary type
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
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        return self
