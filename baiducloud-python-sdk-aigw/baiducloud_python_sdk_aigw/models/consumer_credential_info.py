"""
ConsumerCredentialInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ConsumerCredentialInfo(AbstractModel):
    """
    ConsumerCredentialInfo
    """

    def __init__(
        self,
        identity_id=None,
        name=None,
        value=None,
        masked_value=None,
        generate_mode=None,
        in_header=None,
        in_query=None,
    ):
        """
        Initialize ConsumerCredentialInfo instance.

        :param identity_id: 身份 ID
        :type identity_id: int (optional)

        :param name: 凭证名称
        :type name: str (optional)

        :param value: 凭证值
        :type value: str (optional)

        :param masked_value: 脱敏凭证值
        :type masked_value: str (optional)

        :param generate_mode: 生成模式
        :type generate_mode: str (optional)

        :param in_header: 是否放入请求头
        :type in_header: bool (optional)

        :param in_query: 是否放入查询参数
        :type in_query: bool (optional)
        """
        super().__init__()
        self.identity_id = identity_id
        self.name = name
        self.value = value
        self.masked_value = masked_value
        self.generate_mode = generate_mode
        self.in_header = in_header
        self.in_query = in_query

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
        if self.identity_id is not None:
            result['identityId'] = self.identity_id
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        if self.masked_value is not None:
            result['maskedValue'] = self.masked_value
        if self.generate_mode is not None:
            result['generateMode'] = self.generate_mode
        if self.in_header is not None:
            result['inHeader'] = self.in_header
        if self.in_query is not None:
            result['inQuery'] = self.in_query
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ConsumerCredentialInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('identityId') is not None:
            self.identity_id = m.get('identityId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('maskedValue') is not None:
            self.masked_value = m.get('maskedValue')
        if m.get('generateMode') is not None:
            self.generate_mode = m.get('generateMode')
        if m.get('inHeader') is not None:
            self.in_header = m.get('inHeader')
        if m.get('inQuery') is not None:
            self.in_query = m.get('inQuery')
        return self
