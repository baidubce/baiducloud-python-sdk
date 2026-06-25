"""
NotifyAction information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cprom.models.user import User

from baiducloud_python_sdk_cprom.models.user_group import UserGroup

from baiducloud_python_sdk_cprom.models.callback_config import CallbackConfig


class NotifyAction(AbstractModel):
    """
    NotifyAction
    """

    def __init__(self, channel=None, receiver_type=None, users=None, user_groups=None, webhook_config_list=None):
        """
        Initialize NotifyAction instance.

        :param channel: 通知渠道，phone:电话 , sms: 短信, email: 邮件
        :type channel: List[str] (optional)

        :param receiver_type: 接受者类型，user：用户，userGroup：用户组
        :type receiver_type: str (optional)

        :param users: 用户列表
        :type users: List[User] (optional)

        :param user_groups: 用户组列表
        :type user_groups: List[UserGroup] (optional)

        :param webhook_config_list: webhook 回调配置信息列表
        :type webhook_config_list: List[CallbackConfig] (optional)
        """
        super().__init__()
        self.channel = channel
        self.receiver_type = receiver_type
        self.users = users
        self.user_groups = user_groups
        self.webhook_config_list = webhook_config_list

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
        if self.channel is not None:
            result['channel'] = self.channel
        if self.receiver_type is not None:
            result['receiverType'] = self.receiver_type
        if self.users is not None:
            result['users'] = [i.to_dict() for i in self.users]
        if self.user_groups is not None:
            result['userGroups'] = [i.to_dict() for i in self.user_groups]
        if self.webhook_config_list is not None:
            result['webhookConfigList'] = [i.to_dict() for i in self.webhook_config_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NotifyAction

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('receiverType') is not None:
            self.receiver_type = m.get('receiverType')
        if m.get('users') is not None:
            self.users = [User().from_dict(i) for i in m.get('users')]
        if m.get('userGroups') is not None:
            self.user_groups = [UserGroup().from_dict(i) for i in m.get('userGroups')]
        if m.get('webhookConfigList') is not None:
            self.webhook_config_list = [CallbackConfig().from_dict(i) for i in m.get('webhookConfigList')]
        return self
