"""
Request entity for DescribeModelVersionResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_aihc.models.model_version_entry import ModelVersionEntry


class DescribeModelVersionResponse(BceResponse):
    """
    DescribeModelVersionResponse
    """

    def __init__(
        self,
        name=None,
        id=None,
        init_source=None,
        model_format=None,
        description=None,
        created_at=None,
        updated_at=None,
        owner=None,
        owner_name=None,
        visibility_scope=None,
        version_entry=None,
    ):
        """
        Initialize DescribeModelVersionResponse response.

        :param name: 模型名称
        :type name: str (optional)

        :param id: 模型ID
        :type id: str (optional)

        :param init_source: 模型创建时的来源UserUpload：用户上传
        :type init_source: str (optional)

        :param model_format: 模型格式
        :type model_format: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param created_at: 模型创建时间
        :type created_at: str (optional)

        :param updated_at: 模型更新时间
        :type updated_at: str (optional)

        :param owner: 所有者
        :type owner: str (optional)

        :param owner_name: 所有者名称
        :type owner_name: str (optional)

        :param visibility_scope: 可见范围
        :type visibility_scope: str (optional)

        :param version_entry: version_entry field
        :type version_entry: ModelVersionEntry (optional)
        """
        super().__init__()
        self.name = name
        self.id = id
        self.init_source = init_source
        self.model_format = model_format
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.owner = owner
        self.owner_name = owner_name
        self.visibility_scope = visibility_scope
        self.version_entry = version_entry

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
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.init_source is not None:
            result['initSource'] = self.init_source
        if self.model_format is not None:
            result['modelFormat'] = self.model_format
        if self.description is not None:
            result['description'] = self.description
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_name is not None:
            result['ownerName'] = self.owner_name
        if self.visibility_scope is not None:
            result['visibilityScope'] = self.visibility_scope
        if self.version_entry is not None:
            result['versionEntry'] = self.version_entry.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeModelVersionResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('initSource') is not None:
            self.init_source = m.get('initSource')
        if m.get('modelFormat') is not None:
            self.model_format = m.get('modelFormat')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('ownerName') is not None:
            self.owner_name = m.get('ownerName')
        if m.get('visibilityScope') is not None:
            self.visibility_scope = m.get('visibilityScope')
        if m.get('versionEntry') is not None:
            self.version_entry = ModelVersionEntry().from_dict(m.get('versionEntry'))
        return self
