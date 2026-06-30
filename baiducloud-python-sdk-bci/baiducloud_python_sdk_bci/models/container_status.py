"""
ContainerStatus information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ContainerStatus(AbstractModel):
    """
    ContainerStatus
    """

    def __init__(
        self,
        state=None,
        reason=None,
        message=None,
        start_time=None,
        finish_time=None,
        detail_status=None,
        exit_code=None,
    ):
        """
        Initialize ContainerStatus instance.

        :param state: 状态：Waiting、Running、Terminated
        :type state: str (optional)

        :param reason: 状态Reason
        :type reason: str (optional)

        :param message: 状态信息
        :type message: str (optional)

        :param start_time: 运行开始时间
        :type start_time: str (optional)

        :param finish_time: 运行结束时间
        :type finish_time: str (optional)

        :param detail_status: 状态详情
        :type detail_status: str (optional)

        :param exit_code: 运行退出码
        :type exit_code: int (optional)
        """
        super().__init__()
        self.state = state
        self.reason = reason
        self.message = message
        self.start_time = start_time
        self.finish_time = finish_time
        self.detail_status = detail_status
        self.exit_code = exit_code

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
        if self.state is not None:
            result['state'] = self.state
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.detail_status is not None:
            result['detailStatus'] = self.detail_status
        if self.exit_code is not None:
            result['exitCode'] = self.exit_code
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ContainerStatus

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('detailStatus') is not None:
            self.detail_status = m.get('detailStatus')
        if m.get('exitCode') is not None:
            self.exit_code = m.get('exitCode')
        return self
