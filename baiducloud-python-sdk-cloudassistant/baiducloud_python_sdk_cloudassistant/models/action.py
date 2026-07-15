"""
Action information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cloudassistant.models.command import Command

from baiducloud_python_sdk_cloudassistant.models.file_upload import FileUpload


class Action(AbstractModel):
    """
    Action
    """

    def __init__(
        self,
        id=None,
        ref=None,
        type=None,
        name=None,
        alias=None,
        description=None,
        timeout_second=None,
        command=None,
        file_upload=None,
        supported_instance_types=None,
        created_timestamp=None,
        updated_timestamp=None,
    ):
        """
        Initialize Action instance.

        :param id: 命令ID，系统自动生成，仅被保存的命令拥有
        :type id: str (optional)

        :param ref: Action ID，仅用于更新命令接口。通常引用已有的 Action ID，例如命令执行场景（命令列表查询不返回）
        :type ref: str (optional)

        :param type: Action类型。COMMAND（命令），FILE_UPLOAD（上传文件）
        :type type: str (optional)

        :param name: 命令名称，仅被保存的命令拥有
        :type name: str (optional)

        :param alias: Action 别名
        :type alias: str (optional)

        :param description: Action 描述
        :type description: str (optional)

        :param timeout_second: 动作的超时时间（秒）
        :type timeout_second: int (optional)

        :param command: command attribute
        :type command: Command (optional)

        :param file_upload: file_upload attribute
        :type file_upload: FileUpload (optional)

        :param supported_instance_types: 此公共命令支持的实例类型列表，根据命令创建执行时，根据此字段确定展示那些实例列表，目前支持：BCC、BBC、HPAS
        :type supported_instance_types: List[str] (optional)

        :param created_timestamp: 命令创建时间。unix时间戳（毫秒）
        :type created_timestamp: int (optional)

        :param updated_timestamp: 命令最后一次被修改时间。unix时间戳（毫秒）
        :type updated_timestamp: int (optional)
        """
        super().__init__()
        self.id = id
        self.ref = ref
        self.type = type
        self.name = name
        self.alias = alias
        self.description = description
        self.timeout_second = timeout_second
        self.command = command
        self.file_upload = file_upload
        self.supported_instance_types = supported_instance_types
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp

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
        if self.ref is not None:
            result['ref'] = self.ref
        if self.type is not None:
            result['type'] = self.type
        if self.name is not None:
            result['name'] = self.name
        if self.alias is not None:
            result['alias'] = self.alias
        if self.description is not None:
            result['description'] = self.description
        if self.timeout_second is not None:
            result['timeoutSecond'] = self.timeout_second
        if self.command is not None:
            result['command'] = self.command.to_dict()
        if self.file_upload is not None:
            result['fileUpload'] = self.file_upload.to_dict()
        if self.supported_instance_types is not None:
            result['supportedInstanceTypes'] = self.supported_instance_types
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.updated_timestamp is not None:
            result['updatedTimestamp'] = self.updated_timestamp
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Action

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ref') is not None:
            self.ref = m.get('ref')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('timeoutSecond') is not None:
            self.timeout_second = m.get('timeoutSecond')
        if m.get('command') is not None:
            self.command = Command().from_dict(m.get('command'))
        if m.get('fileUpload') is not None:
            self.file_upload = FileUpload().from_dict(m.get('fileUpload'))
        if m.get('supportedInstanceTypes') is not None:
            self.supported_instance_types = m.get('supportedInstanceTypes')
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('updatedTimestamp') is not None:
            self.updated_timestamp = m.get('updatedTimestamp')
        return self
