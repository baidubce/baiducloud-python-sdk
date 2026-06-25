"""
Request entity for GetNotificationPolicyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cprom.models.user import User
from baiducloud_python_sdk_cprom.models.user_group import UserGroup
from baiducloud_python_sdk_cprom.models.callback_config import CallbackConfig
from baiducloud_python_sdk_cprom.models.escalate_param import EscalateParam


class GetNotificationPolicyResponse(BceResponse):
    """
    GetNotificationPolicyResponse
    """

    def __init__(
        self,
        notify_rule_id=None,
        notify_rule_name=None,
        start_time=None,
        end_time=None,
        channel=None,
        receiver_type=None,
        users=None,
        user_groups=None,
        webhook_config_list=None,
        escalate_config_list=None,
        repeat_notify_config=None,
        update_time=None,
    ):
        """
        Initialize GetNotificationPolicyResponse response.

        :param notify_rule_id: 通知策略ID
        :type notify_rule_id: str (optional)

        :param notify_rule_name: 通知策略名称
        :type notify_rule_name: str (optional)

        :param start_time: 通知开始时间，时间格式 00：00：00
        :type start_time: str (optional)

        :param end_time: 通知结束时间，时间格式 23：59：59
        :type end_time: str (optional)

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

        :param escalate_config_list: 通知策略升级参数列表
        :type escalate_config_list: List[EscalateParam] (optional)

        :param repeat_notify_config: 重复通知配置
        :type repeat_notify_config: object (optional)

        :param update_time: 更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.notify_rule_id = notify_rule_id
        self.notify_rule_name = notify_rule_name
        self.start_time = start_time
        self.end_time = end_time
        self.channel = channel
        self.receiver_type = receiver_type
        self.users = users
        self.user_groups = user_groups
        self.webhook_config_list = webhook_config_list
        self.escalate_config_list = escalate_config_list
        self.repeat_notify_config = repeat_notify_config
        self.update_time = update_time

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
        if self.notify_rule_id is not None:
            result['notifyRuleId'] = self.notify_rule_id
        if self.notify_rule_name is not None:
            result['notifyRuleName'] = self.notify_rule_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
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
        if self.escalate_config_list is not None:
            result['escalateConfigList'] = [i.to_dict() for i in self.escalate_config_list]
        if self.repeat_notify_config is not None:
            result['repeatNotifyConfig'] = self.repeat_notify_config
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetNotificationPolicyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('notifyRuleId') is not None:
            self.notify_rule_id = m.get('notifyRuleId')
        if m.get('notifyRuleName') is not None:
            self.notify_rule_name = m.get('notifyRuleName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
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
        if m.get('escalateConfigList') is not None:
            self.escalate_config_list = [EscalateParam().from_dict(i) for i in m.get('escalateConfigList')]
        if m.get('repeatNotifyConfig') is not None:
            self.repeat_notify_config = m.get('repeatNotifyConfig')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
