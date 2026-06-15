"""
Request entity for UpdateNotifyTemplateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcm.models.silence_period import SilencePeriod
from baiducloud_python_sdk_bcm.models.notify_receiver import NotifyReceiver
from baiducloud_python_sdk_bcm.models.callback import Callback


class UpdateNotifyTemplateRequest(AbstractModel):
    """
    Request entity for UpdateNotifyTemplateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, name, silence_periods=None, receivers=None, callbacks=None):
        """
        Initialize UpdateNotifyTemplateRequest request entity.

        :param id: 通知模板ID
        :type id: str (required)

        :param name: 通知模板名称
        :type name: str (required)

        :param silence_periods: 静默时间段列表
        :type silence_periods: List[SilencePeriod] (optional)

        :param receivers: 通知接收者列表
        :type receivers: List[NotifyReceiver] (optional)

        :param callbacks: 回调配置列表
        :type callbacks: List[Callback] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.silence_periods = silence_periods
        self.receivers = receivers
        self.callbacks = callbacks

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.silence_periods is not None:
            result['silencePeriods'] = [i.to_dict() for i in self.silence_periods]
        if self.receivers is not None:
            result['receivers'] = [i.to_dict() for i in self.receivers]
        if self.callbacks is not None:
            result['callbacks'] = [i.to_dict() for i in self.callbacks]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateNotifyTemplateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('silencePeriods') is not None:
            self.silence_periods = [SilencePeriod().from_dict(i) for i in m.get('silencePeriods')]
        if m.get('receivers') is not None:
            self.receivers = [NotifyReceiver().from_dict(i) for i in m.get('receivers')]
        if m.get('callbacks') is not None:
            self.callbacks = [Callback().from_dict(i) for i in m.get('callbacks')]
        return self
