"""
NotifyReceiver information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class NotifyReceiver(AbstractModel):
    """
    NotifyReceiver
    """

    def __init__(self, id=None, name=None, receiver_type=None, channels=None):
        """
        Initialize NotifyReceiver instance.

        :param id: 通知接收方ID，用户/用户组ID
        :type id: str (optional)

        :param name: 接收通知方名称
        :type name: str (optional)

        :param receiver_type: 接收通知的用户类型，可选值：USER / USER_GROUP
        :type receiver_type: str (optional)

        :param channels: 通知渠道列表，可选值：SMS / EMAIL / PHONE
        :type channels: List[str] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.receiver_type = receiver_type
        self.channels = channels

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
        if self.receiver_type is not None:
            result['receiverType'] = self.receiver_type
        if self.channels is not None:
            result['channels'] = self.channels
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NotifyReceiver

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('receiverType') is not None:
            self.receiver_type = m.get('receiverType')
        if m.get('channels') is not None:
            self.channels = m.get('channels')
        return self
