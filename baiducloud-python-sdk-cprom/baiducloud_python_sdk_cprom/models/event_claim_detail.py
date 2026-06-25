"""
EventClaimDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EventClaimDetail(AbstractModel):
    """
    EventClaimDetail
    """

    def __init__(self, event_id=None, success=None, message=None):
        """
        Initialize EventClaimDetail instance.

        :param event_id: 事件 ID
        :type event_id: str (optional)

        :param success: 是否成功
        :type success: bool (optional)

        :param message: 错误信息（失败时有值）
        :type message: str (optional)
        """
        super().__init__()
        self.event_id = event_id
        self.success = success
        self.message = message

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
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.success is not None:
            result['success'] = self.success
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EventClaimDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self
