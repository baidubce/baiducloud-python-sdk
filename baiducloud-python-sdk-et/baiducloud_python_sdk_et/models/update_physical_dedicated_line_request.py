"""
Request entity for UpdatePhysicalDedicatedLineRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdatePhysicalDedicatedLineRequest(AbstractModel):
    """
    Request entity for UpdatePhysicalDedicatedLineRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        dcphy_id,
        client_token=None,
        name=None,
        description=None,
        user_name=None,
        user_phone=None,
        user_email=None,
        link_delay=None,
    ):
        """
        Initialize UpdatePhysicalDedicatedLineRequest request entity.

        :param dcphy_id: dcphy_id parameter
        :type dcphy_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 专线名称，大小写字母、数字以及-_ /.特殊字符，必须以字母开头，长度1-65
        :type name: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param user_name: 用户名称
        :type user_name: str (optional)

        :param user_phone: 用户手机号码
        :type user_phone: str (optional)

        :param user_email: 邮箱
        :type user_email: str (optional)

        :param link_delay: 端口延迟down时间，单位ms
        :type link_delay: int (optional)
        """
        super().__init__()
        self.dcphy_id = dcphy_id
        self.client_token = client_token
        self.name = name
        self.description = description
        self.user_name = user_name
        self.user_phone = user_phone
        self.user_email = user_email
        self.link_delay = link_delay

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
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.user_phone is not None:
            result['userPhone'] = self.user_phone
        if self.user_email is not None:
            result['userEmail'] = self.user_email
        if self.link_delay is not None:
            result['linkDelay'] = self.link_delay
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdatePhysicalDedicatedLineRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('dcphyId') is not None:
            self.dcphy_id = m.get('dcphyId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('userPhone') is not None:
            self.user_phone = m.get('userPhone')
        if m.get('userEmail') is not None:
            self.user_email = m.get('userEmail')
        if m.get('linkDelay') is not None:
            self.link_delay = m.get('linkDelay')
        return self
