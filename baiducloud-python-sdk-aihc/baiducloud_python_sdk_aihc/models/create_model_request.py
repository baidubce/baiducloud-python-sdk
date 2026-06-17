"""
Request entity for CreateModelRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_aihc.models.model_version_entry import ModelVersionEntry


class CreateModelRequest(AbstractModel):
    """
    Request entity for CreateModelRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, model_format, init_version_entry, description=None, owner=None, visibility_scope=None):
        """
        Initialize CreateModelRequest request entity.

        :param name: 模型名称支持小写字母、数字和-，必须以小写字母开头，必须以小写字母或数字结尾，长度限制1-50。
        :type name: str (required)

        :param description: 描述
        :type description: str (optional)

        :param model_format: 模型格式，HuggingFace、MegatronCore等
        :type model_format: str (required)

        :param owner: 所有者，不传递时默认为创建者
        :type owner: str (optional)

        :param visibility_scope: 可见范围ONLY_OWNER：仅所有者可读写
        :type visibility_scope: str (optional)

        :param init_version_entry: init_version_entry parameter
        :type init_version_entry: ModelVersionEntry (required)
        """
        super().__init__()
        self.name = name
        self.description = description
        self.model_format = model_format
        self.owner = owner
        self.visibility_scope = visibility_scope
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
        if self.description is not None:
            result['description'] = self.description
        if self.model_format is not None:
            result['modelFormat'] = self.model_format
        if self.owner is not None:
            result['owner'] = self.owner
        if self.visibility_scope is not None:
            result['visibilityScope'] = self.visibility_scope
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
        :rtype: CreateModelRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('modelFormat') is not None:
            self.model_format = m.get('modelFormat')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('visibilityScope') is not None:
            self.visibility_scope = m.get('visibilityScope')
        if m.get('initVersionEntry') is not None:
            self.init_version_entry = ModelVersionEntry().from_dict(m.get('initVersionEntry'))
        return self
