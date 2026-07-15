"""
ChildRun information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cloudassistant.models.output import Output


class ChildRun(AbstractModel):
    """
    ChildRun
    """

    def __init__(
        self,
        id=None,
        state=None,
        target=None,
        created_timestamp=None,
        finished_timestamp=None,
        output=None,
        log=None,
        error_code=None,
        fail_reason=None,
    ):
        """
        Initialize ChildRun instance.

        :param id: 子执行ID
        :type id: str (optional)

        :param state: 执行状态。枚举值：FAILED（执行失败），RUNNING（执行中），SUCCESS（执行完成）
        :type state: str (optional)

        :param target: 子执行对应的实例信息
        :type target: object (optional)

        :param created_timestamp: 子执行开始时间。unix时间戳，单位：毫秒
        :type created_timestamp: int (optional)

        :param finished_timestamp: 子执行结束时间，仅执行结束时返回。unix时间戳，单位：毫秒。
        :type finished_timestamp: int (optional)

        :param output: output attribute
        :type output: Output (optional)

        :param log: 子执行日志内容，仅当请求参数 withLog=true 时返回
        :type log: str (optional)

        :param error_code: 错误码
        :type error_code: str (optional)

        :param fail_reason: 子执行失败原因
        :type fail_reason: str (optional)
        """
        super().__init__()
        self.id = id
        self.state = state
        self.target = target
        self.created_timestamp = created_timestamp
        self.finished_timestamp = finished_timestamp
        self.output = output
        self.log = log
        self.error_code = error_code
        self.fail_reason = fail_reason

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
        if self.state is not None:
            result['state'] = self.state
        if self.target is not None:
            result['target'] = self.target
        if self.created_timestamp is not None:
            result['createdTimestamp'] = self.created_timestamp
        if self.finished_timestamp is not None:
            result['finishedTimestamp'] = self.finished_timestamp
        if self.output is not None:
            result['output'] = self.output.to_dict()
        if self.log is not None:
            result['log'] = self.log
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.fail_reason is not None:
            result['failReason'] = self.fail_reason
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ChildRun

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('createdTimestamp') is not None:
            self.created_timestamp = m.get('createdTimestamp')
        if m.get('finishedTimestamp') is not None:
            self.finished_timestamp = m.get('finishedTimestamp')
        if m.get('output') is not None:
            self.output = Output().from_dict(m.get('output'))
        if m.get('log') is not None:
            self.log = m.get('log')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('failReason') is not None:
            self.fail_reason = m.get('failReason')
        return self
