"""
Request entity for UpdateAppBlbServerGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateAppBlbServerGroupRequest(AbstractModel):
    """
    Request entity for UpdateAppBlbServerGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, sg_id, client_token=None, name=None, desc=None, preserve_client_ip_enabled=None):
        """
        Initialize UpdateAppBlbServerGroupRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param sg_id: 要更新的服务器组的id
        :type sg_id: str (required)

        :param name: 服务器组的名称，方便记忆。长度1~65个字节，字母开头，可包含字母数字-\\_/.字符。若不传该参数，会自动生成
        :type name: str (optional)

        :param desc: 服务器组的描述，便于用户添加更详细的描述信息。长度0~450个字节，支持中文。默认为空
        :type desc: str (optional)

        :param preserve_client_ip_enabled: 是否开启客户端地址保持功能，注意：仅应用型实例支持，应用型IPv6不支持该功能
        :type preserve_client_ip_enabled: bool (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.sg_id = sg_id
        self.name = name
        self.desc = desc
        self.preserve_client_ip_enabled = preserve_client_ip_enabled

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
        if self.sg_id is not None:
            result['sgId'] = self.sg_id
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.preserve_client_ip_enabled is not None:
            result['preserveClientIpEnabled'] = self.preserve_client_ip_enabled
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAppBlbServerGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('sgId') is not None:
            self.sg_id = m.get('sgId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('preserveClientIpEnabled') is not None:
            self.preserve_client_ip_enabled = m.get('preserveClientIpEnabled')
        return self
