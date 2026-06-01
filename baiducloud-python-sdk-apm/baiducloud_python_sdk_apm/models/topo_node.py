"""
TopoNode information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TopoNode(AbstractModel):
    """
    TopoNode
    """

    def __init__(
        self,
        service_name=None,
        language=None,
        type=None,
        inferred=None,
        component=None,
        requests=None,
        requests_per_second=None,
        errors=None,
        error_rate=None,
        duration_seconds=None,
        state=None,
    ):
        """
        Initialize TopoNode instance.

        :param service_name: 应用名
        :type service_name: str (optional)

        :param language: 语言
        :type language: str (optional)

        :param type: type attribute
        :type type: str (optional)

        :param inferred: 是否是推断出的节点
        :type inferred: bool (optional)

        :param component: 组件类型
        :type component: str (optional)

        :param requests: 总请求数
        :type requests: int (optional)

        :param requests_per_second: 每秒请求数
        :type requests_per_second: float (optional)

        :param errors: 错误数
        :type errors: int (optional)

        :param error_rate: 错误率
        :type error_rate: float (optional)

        :param duration_seconds: 平均响应时间，单位：秒
        :type duration_seconds: float (optional)

        :param state: 节点状态，可选项：`OK` - 正常，`WARNING` - 警示，`ERROR` - 异常
        :type state: str (optional)
        """
        super().__init__()
        self.service_name = service_name
        self.language = language
        self.type = type
        self.inferred = inferred
        self.component = component
        self.requests = requests
        self.requests_per_second = requests_per_second
        self.errors = errors
        self.error_rate = error_rate
        self.duration_seconds = duration_seconds
        self.state = state

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
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.language is not None:
            result['language'] = self.language
        if self.type is not None:
            result['type'] = self.type
        if self.inferred is not None:
            result['inferred'] = self.inferred
        if self.component is not None:
            result['component'] = self.component
        if self.requests is not None:
            result['requests'] = self.requests
        if self.requests_per_second is not None:
            result['requestsPerSecond'] = self.requests_per_second
        if self.errors is not None:
            result['errors'] = self.errors
        if self.error_rate is not None:
            result['errorRate'] = self.error_rate
        if self.duration_seconds is not None:
            result['durationSeconds'] = self.duration_seconds
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TopoNode

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('inferred') is not None:
            self.inferred = m.get('inferred')
        if m.get('component') is not None:
            self.component = m.get('component')
        if m.get('requests') is not None:
            self.requests = m.get('requests')
        if m.get('requestsPerSecond') is not None:
            self.requests_per_second = m.get('requestsPerSecond')
        if m.get('errors') is not None:
            self.errors = m.get('errors')
        if m.get('errorRate') is not None:
            self.error_rate = m.get('errorRate')
        if m.get('durationSeconds') is not None:
            self.duration_seconds = m.get('durationSeconds')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self
