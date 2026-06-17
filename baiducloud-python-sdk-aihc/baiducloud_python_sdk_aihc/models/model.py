"""
Model information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Model(AbstractModel):
    """
    Model
    """

    def __init__(
        self,
        id=None,
        name=None,
        init_source=None,
        latest_version=None,
        latest_version_id=None,
        model_format=None,
        description=None,
        updated_at=None,
        created_at=None,
        owner=None,
        owner_name=None,
        visibility_scope=None,
    ):
        """
        Initialize Model instance.

        :param id: 模型ID。新建模型时，无需指定ID。
        :type id: str (optional)

        :param name: 模型名称
        :type name: str (optional)

        :param init_source: 模型创建时的来源UserUpload：用户上传
        :type init_source: str (optional)

        :param latest_version: 最新版本
        :type latest_version: str (optional)

        :param latest_version_id: 最新版本ID
        :type latest_version_id: str (optional)

        :param model_format: 模型格式
        :type model_format: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param updated_at: 更新时间
        :type updated_at: str (optional)

        :param created_at: 创建时间
        :type created_at: str (optional)

        :param owner: 所有者
        :type owner: str (optional)

        :param owner_name: 所有者名称
        :type owner_name: str (optional)

        :param visibility_scope: 可见范围
        :type visibility_scope: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.init_source = init_source
        self.latest_version = latest_version
        self.latest_version_id = latest_version_id
        self.model_format = model_format
        self.description = description
        self.updated_at = updated_at
        self.created_at = created_at
        self.owner = owner
        self.owner_name = owner_name
        self.visibility_scope = visibility_scope

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
        if self.init_source is not None:
            result['initSource'] = self.init_source
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.latest_version_id is not None:
            result['latestVersionId'] = self.latest_version_id
        if self.model_format is not None:
            result['modelFormat'] = self.model_format
        if self.description is not None:
            result['description'] = self.description
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_name is not None:
            result['ownerName'] = self.owner_name
        if self.visibility_scope is not None:
            result['visibilityScope'] = self.visibility_scope
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Model

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('initSource') is not None:
            self.init_source = m.get('initSource')
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('latestVersionId') is not None:
            self.latest_version_id = m.get('latestVersionId')
        if m.get('modelFormat') is not None:
            self.model_format = m.get('modelFormat')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('ownerName') is not None:
            self.owner_name = m.get('ownerName')
        if m.get('visibilityScope') is not None:
            self.visibility_scope = m.get('visibilityScope')
        return self
