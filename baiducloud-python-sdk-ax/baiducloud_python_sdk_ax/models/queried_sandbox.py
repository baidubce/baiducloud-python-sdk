"""
QueriedSandbox information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueriedSandbox(AbstractModel):
    """
    QueriedSandbox
    """

    def __init__(
        self,
        sandbox_id=None,
        state=None,
        metadata=None,
        cpu_count=None,
        memory_mb=None,
        started_at=None,
        end_at=None,
        envd_version=None,
        envd_access_token=None,
        template_id=None,
        image_path=None,
    ):
        """
        Initialize QueriedSandbox instance.

        :param sandbox_id: 沙箱实例 ID。
        :type sandbox_id: str (optional)

        :param state: 沙箱当前状态，可取 running、paused、killing、killed。
        :type state: str (optional)

        :param metadata: 沙箱 metadata。
        :type metadata: Dict[str, str] (optional)

        :param cpu_count: CPU 核数。
        :type cpu_count: int (optional)

        :param memory_mb: 内存大小，单位为 MiB。
        :type memory_mb: int (optional)

        :param started_at: 沙箱启动时间，RFC3339 格式。
        :type started_at: str (optional)

        :param end_at: 沙箱结束时间，RFC3339 格式。
        :type end_at: str (optional)

        :param envd_version: 沙箱运行时 envd 版本。
        :type envd_version: str (optional)

        :param envd_access_token: 访问沙箱 envd 的临时 token。
        :type envd_access_token: str (optional)

        :param template_id: 创建沙箱使用的模板 ID。
        :type template_id: str (optional)

        :param image_path: 沙箱实际使用的镜像地址。
        :type image_path: str (optional)
        """
        super().__init__()
        self.sandbox_id = sandbox_id
        self.state = state
        self.metadata = metadata
        self.cpu_count = cpu_count
        self.memory_mb = memory_mb
        self.started_at = started_at
        self.end_at = end_at
        self.envd_version = envd_version
        self.envd_access_token = envd_access_token
        self.template_id = template_id
        self.image_path = image_path

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
        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id
        if self.state is not None:
            result['state'] = self.state
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.memory_mb is not None:
            result['memoryMB'] = self.memory_mb
        if self.started_at is not None:
            result['startedAt'] = self.started_at
        if self.end_at is not None:
            result['endAt'] = self.end_at
        if self.envd_version is not None:
            result['envdVersion'] = self.envd_version
        if self.envd_access_token is not None:
            result['envdAccessToken'] = self.envd_access_token
        if self.template_id is not None:
            result['templateID'] = self.template_id
        if self.image_path is not None:
            result['imagePath'] = self.image_path
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueriedSandbox

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('memoryMB') is not None:
            self.memory_mb = m.get('memoryMB')
        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')
        if m.get('endAt') is not None:
            self.end_at = m.get('endAt')
        if m.get('envdVersion') is not None:
            self.envd_version = m.get('envdVersion')
        if m.get('envdAccessToken') is not None:
            self.envd_access_token = m.get('envdAccessToken')
        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')
        if m.get('imagePath') is not None:
            self.image_path = m.get('imagePath')
        return self
