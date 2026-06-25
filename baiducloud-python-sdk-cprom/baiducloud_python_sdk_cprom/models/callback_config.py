"""
CallbackConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cprom.models.webhook_detail import WebhookDetail


class CallbackConfig(AbstractModel):
    """
    CallbackConfig
    """

    def __init__(self, webhook_type=None, webhook_list=None):
        """
        Initialize CallbackConfig instance.

        :param webhook_type: 回调类型，weCom:企业微信，dingTalk:钉钉，lark:飞书，custom:自定义webhook
        :type webhook_type: str (optional)

        :param webhook_list: webhook配置详情列表
        :type webhook_list: List[WebhookDetail] (optional)
        """
        super().__init__()
        self.webhook_type = webhook_type
        self.webhook_list = webhook_list

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
        if self.webhook_type is not None:
            result['webhookType'] = self.webhook_type
        if self.webhook_list is not None:
            result['webhookList'] = [i.to_dict() for i in self.webhook_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CallbackConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('webhookType') is not None:
            self.webhook_type = m.get('webhookType')
        if m.get('webhookList') is not None:
            self.webhook_list = [WebhookDetail().from_dict(i) for i in m.get('webhookList')]
        return self
