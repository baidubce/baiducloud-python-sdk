"""
Request entity for CreateSandboxRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateSandboxRequest(AbstractModel):
    """
    Request entity for CreateSandboxRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        template_id,
        timeout=None,
        metadata=None,
        env_vars=None,
        secure=None,
        allow_internet_access=None,
        auto_pause=None,
        auto_resume=None,
        runtime_type=None,
        mcp=None,
        volume_mounts=None,
    ):
        """
        Initialize CreateSandboxRequest request entity.

        :param template_id: 沙箱模板 ID。
        :type template_id: str (required)

        :param timeout: 沙箱超时时间，单位秒。
        :type timeout: int (optional)

        :param metadata: 沙箱标签元数据。
        :type metadata: Dict[str, str] (optional)

        :param env_vars: 沙箱环境变量。
        :type env_vars: Dict[str, str] (optional)

        :param secure: 是否对沙箱的全部系统通信进行加密。
        :type secure: bool (optional)

        :param allow_internet_access: 是否允许沙箱访问公网。
        :type allow_internet_access: bool (optional)

        :param auto_pause: 超时后是否自动暂停沙箱。
        :type auto_pause: bool (optional)

        :param auto_resume: 暂停沙箱后的自动恢复配置，含 enabled（Boolean）字段。
        :type auto_resume: Dict[str, object] (optional)

        :param runtime_type: 沙箱运行时类型，可选 kata；仅白名单用户可指定，默认空为 CRIU。
        :type runtime_type: str (optional)

        :param mcp: 沙箱的 MCP 配置。
        :type mcp: Dict[str, object] (optional)

        :param volume_mounts: 挂载到沙箱的 NFS 卷列表，元素含 name、path、subPath、readOnly 字段。
        :type volume_mounts: List[Dict[str, object]] (optional)
        """
        super().__init__()
        self.template_id = template_id
        self.timeout = timeout
        self.metadata = metadata
        self.env_vars = env_vars
        self.secure = secure
        self.allow_internet_access = allow_internet_access
        self.auto_pause = auto_pause
        self.auto_resume = auto_resume
        self.runtime_type = runtime_type
        self.mcp = mcp
        self.volume_mounts = volume_mounts

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
        if self.template_id is not None:
            result['templateID'] = self.template_id
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.env_vars is not None:
            result['envVars'] = self.env_vars
        if self.secure is not None:
            result['secure'] = self.secure
        if self.allow_internet_access is not None:
            result['allow_internet_access'] = self.allow_internet_access
        if self.auto_pause is not None:
            result['autoPause'] = self.auto_pause
        if self.auto_resume is not None:
            result['autoResume'] = self.auto_resume
        if self.runtime_type is not None:
            result['runtimeType'] = self.runtime_type
        if self.mcp is not None:
            result['mcp'] = self.mcp
        if self.volume_mounts is not None:
            result['volumeMounts'] = self.volume_mounts
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSandboxRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')
        if m.get('envVars') is not None:
            self.env_vars = m.get('envVars')
        if m.get('secure') is not None:
            self.secure = m.get('secure')
        if m.get('allow_internet_access') is not None:
            self.allow_internet_access = m.get('allow_internet_access')
        if m.get('autoPause') is not None:
            self.auto_pause = m.get('autoPause')
        if m.get('autoResume') is not None:
            self.auto_resume = m.get('autoResume')
        if m.get('runtimeType') is not None:
            self.runtime_type = m.get('runtimeType')
        if m.get('mcp') is not None:
            self.mcp = m.get('mcp')
        if m.get('volumeMounts') is not None:
            self.volume_mounts = m.get('volumeMounts')
        return self
