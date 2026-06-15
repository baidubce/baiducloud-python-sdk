"""
Request entity for DescribeNotifyTemplateResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcm.models.silence_period import SilencePeriod
from baiducloud_python_sdk_bcm.models.notify_receiver import NotifyReceiver
from baiducloud_python_sdk_bcm.models.callback import Callback


class DescribeNotifyTemplateResponse(BceResponse):
    """
    DescribeNotifyTemplateResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        id=None,
        name=None,
        source=None,
        silence_periods=None,
        receivers=None,
        callbacks=None,
    ):
        """
        Initialize DescribeNotifyTemplateResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 响应码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param id: 通知模板ID
        :type id: str (optional)

        :param name: 通知模板名称
        :type name: str (optional)

        :param source: 模板来源，可选值：SYSTEM / CUSTOM
        :type source: str (optional)

        :param silence_periods: 静默时间段列表
        :type silence_periods: List[SilencePeriod] (optional)

        :param receivers: 通知接收者列表
        :type receivers: List[NotifyReceiver] (optional)

        :param callbacks: 回调配置列表
        :type callbacks: List[Callback] (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.id = id
        self.name = name
        self.source = source
        self.silence_periods = silence_periods
        self.receivers = receivers
        self.callbacks = callbacks

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
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.silence_periods is not None:
            result['silencePeriods'] = [i.to_dict() for i in self.silence_periods]
        if self.receivers is not None:
            result['receivers'] = [i.to_dict() for i in self.receivers]
        if self.callbacks is not None:
            result['callbacks'] = [i.to_dict() for i in self.callbacks]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeNotifyTemplateResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('silencePeriods') is not None:
            self.silence_periods = [SilencePeriod().from_dict(i) for i in m.get('silencePeriods')]
        if m.get('receivers') is not None:
            self.receivers = [NotifyReceiver().from_dict(i) for i in m.get('receivers')]
        if m.get('callbacks') is not None:
            self.callbacks = [Callback().from_dict(i) for i in m.get('callbacks')]
        return self
