"""
Request entity for DescribeNotifyTemplatesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcm.models.notify_template import NotifyTemplate
from baiducloud_python_sdk_bcm.models.silence_period import SilencePeriod
from baiducloud_python_sdk_bcm.models.notify_receiver import NotifyReceiver
from baiducloud_python_sdk_bcm.models.callback import Callback


class DescribeNotifyTemplatesResponse(BceResponse):
    """
    DescribeNotifyTemplatesResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        notify_templates=None,
        notify_templates_id=None,
        notify_templates_name=None,
        notify_templates_source=None,
        notify_templates_silence_periods=None,
        notify_templates_receivers=None,
        notify_templates_callbacks=None,
    ):
        """
        Initialize DescribeNotifyTemplatesResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 响应码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param notify_templates: 通知模板列表
        :type notify_templates: List[NotifyTemplate] (optional)

        :param notify_templates_id: 通知模板ID
        :type notify_templates_id: str (optional)

        :param notify_templates_name: 通知模板名称
        :type notify_templates_name: str (optional)

        :param notify_templates_source: 模板来源，可选值：SYSTEM（默认通知模板）/ CUSTOM（用户自定义创建）
        :type notify_templates_source: str (optional)

        :param notify_templates_silence_periods: 静默时间段列表
        :type notify_templates_silence_periods: List[SilencePeriod] (optional)

        :param notify_templates_receivers: 通知接收者列表
        :type notify_templates_receivers: List[NotifyReceiver] (optional)

        :param notify_templates_callbacks: 回调配置列表
        :type notify_templates_callbacks: List[Callback] (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.notify_templates = notify_templates
        self.notify_templates_id = notify_templates_id
        self.notify_templates_name = notify_templates_name
        self.notify_templates_source = notify_templates_source
        self.notify_templates_silence_periods = notify_templates_silence_periods
        self.notify_templates_receivers = notify_templates_receivers
        self.notify_templates_callbacks = notify_templates_callbacks

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
        if self.notify_templates is not None:
            result['notifyTemplates'] = [i.to_dict() for i in self.notify_templates]
        if self.notify_templates_id is not None:
            result['notifyTemplates.id'] = self.notify_templates_id
        if self.notify_templates_name is not None:
            result['notifyTemplates.name'] = self.notify_templates_name
        if self.notify_templates_source is not None:
            result['notifyTemplates.source'] = self.notify_templates_source
        if self.notify_templates_silence_periods is not None:
            result['notifyTemplates.silencePeriods'] = [i.to_dict() for i in self.notify_templates_silence_periods]
        if self.notify_templates_receivers is not None:
            result['notifyTemplates.receivers'] = [i.to_dict() for i in self.notify_templates_receivers]
        if self.notify_templates_callbacks is not None:
            result['notifyTemplates.callbacks'] = [i.to_dict() for i in self.notify_templates_callbacks]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeNotifyTemplatesResponse

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
        if m.get('notifyTemplates') is not None:
            self.notify_templates = [NotifyTemplate().from_dict(i) for i in m.get('notifyTemplates')]
        if m.get('notifyTemplates.id') is not None:
            self.notify_templates_id = m.get('notifyTemplates.id')
        if m.get('notifyTemplates.name') is not None:
            self.notify_templates_name = m.get('notifyTemplates.name')
        if m.get('notifyTemplates.source') is not None:
            self.notify_templates_source = m.get('notifyTemplates.source')
        if m.get('notifyTemplates.silencePeriods') is not None:
            self.notify_templates_silence_periods = [
                SilencePeriod().from_dict(i) for i in m.get('notifyTemplates.silencePeriods')
            ]
        if m.get('notifyTemplates.receivers') is not None:
            self.notify_templates_receivers = [
                NotifyReceiver().from_dict(i) for i in m.get('notifyTemplates.receivers')
            ]
        if m.get('notifyTemplates.callbacks') is not None:
            self.notify_templates_callbacks = [Callback().from_dict(i) for i in m.get('notifyTemplates.callbacks')]
        return self
