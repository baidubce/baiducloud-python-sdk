"""
ActionFilter information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cloudassistant.models.command_filter import CommandFilter

from baiducloud_python_sdk_cloudassistant.models.file_upload_filter import FileUploadFilter


class ActionFilter(AbstractModel):
    """
    ActionFilter
    """

    def __init__(self, id=None, name=None, type=None, command=None, file_upload=None):
        """
        Initialize ActionFilter instance.

        :param id: 命令 ID，仅用来查询执行历史记录，例如：c-jPwwUBxxxxxxxxxx
        :type id: str (optional)

        :param name: 命令名称，仅用来查询执行历史记录
        :type name: str (optional)

        :param type: Action类型。COMMAND（命令），FILE_UPLOAD（上传文件）
        :type type: str (optional)

        :param command: command attribute
        :type command: CommandFilter (optional)

        :param file_upload: file_upload attribute
        :type file_upload: FileUploadFilter (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.type = type
        self.command = command
        self.file_upload = file_upload

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
        if self.type is not None:
            result['type'] = self.type
        if self.command is not None:
            result['command'] = self.command.to_dict()
        if self.file_upload is not None:
            result['fileUpload'] = self.file_upload.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ActionFilter

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('command') is not None:
            self.command = CommandFilter().from_dict(m.get('command'))
        if m.get('fileUpload') is not None:
            self.file_upload = FileUploadFilter().from_dict(m.get('fileUpload'))
        return self
