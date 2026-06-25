"""
WebhookDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cprom.models.mentioned_user_config import MentionedUserConfig


class WebhookDetail(AbstractModel):
    """
    WebhookDetail
    """

    def __init__(
        self, hook_name=None, hook_method=None, hook_url=None, headers=None, params=None, mentioned_users=None
    ):
        """
        Initialize WebhookDetail instance.

        :param hook_name: 机器人名称
        :type hook_name: str (optional)

        :param hook_method: webhook请求的HTTP方法，默认post
        :type hook_method: str (optional)

        :param hook_url: 机器人地址
        :type hook_url: str (optional)

        :param headers: webhook请求的HTTP头部信息
        :type headers: Dict[str, str] (optional)

        :param params: webhook请求参数
        :type params: Dict[str, str] (optional)

        :param mentioned_users: mentioned_users attribute
        :type mentioned_users: MentionedUserConfig (optional)
        """
        super().__init__()
        self.hook_name = hook_name
        self.hook_method = hook_method
        self.hook_url = hook_url
        self.headers = headers
        self.params = params
        self.mentioned_users = mentioned_users

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
        if self.hook_name is not None:
            result['hookName'] = self.hook_name
        if self.hook_method is not None:
            result['hookMethod'] = self.hook_method
        if self.hook_url is not None:
            result['hookUrl'] = self.hook_url
        if self.headers is not None:
            result['headers'] = self.headers
        if self.params is not None:
            result['params'] = self.params
        if self.mentioned_users is not None:
            result['mentionedUsers'] = self.mentioned_users.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: WebhookDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('hookName') is not None:
            self.hook_name = m.get('hookName')
        if m.get('hookMethod') is not None:
            self.hook_method = m.get('hookMethod')
        if m.get('hookUrl') is not None:
            self.hook_url = m.get('hookUrl')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('mentionedUsers') is not None:
            self.mentioned_users = MentionedUserConfig().from_dict(m.get('mentionedUsers'))
        return self
