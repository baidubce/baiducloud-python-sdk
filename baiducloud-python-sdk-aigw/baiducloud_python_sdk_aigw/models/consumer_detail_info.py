"""
ConsumerDetailInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aigw.models.tag import Tag

from baiducloud_python_sdk_aigw.models.consumer_credential_info import ConsumerCredentialInfo

from baiducloud_python_sdk_aigw.models.iam_credential_spec import IAMCredentialSpec


class ConsumerDetailInfo(AbstractModel):
    """
    ConsumerDetailInfo
    """

    def __init__(
        self,
        consumer_id=None,
        consumer_name=None,
        description=None,
        auth_type=None,
        credential_type=None,
        route_names=None,
        tags=None,
        credentials=None,
        iam_credential=None,
    ):
        """
        Initialize ConsumerDetailInfo instance.

        :param consumer_id: 消费者 ID
        :type consumer_id: str (optional)

        :param consumer_name: 消费者名称
        :type consumer_name: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param auth_type: 认证类型
        :type auth_type: str (optional)

        :param credential_type: 凭证类型
        :type credential_type: str (optional)

        :param route_names: 路由名称列表
        :type route_names: List[str] (optional)

        :param tags: 标签列表
        :type tags: List[Tag] (optional)

        :param credentials: 凭证详情
        :type credentials: List[ConsumerCredentialInfo] (optional)

        :param iam_credential: iam_credential attribute
        :type iam_credential: IAMCredentialSpec (optional)
        """
        super().__init__()
        self.consumer_id = consumer_id
        self.consumer_name = consumer_name
        self.description = description
        self.auth_type = auth_type
        self.credential_type = credential_type
        self.route_names = route_names
        self.tags = tags
        self.credentials = credentials
        self.iam_credential = iam_credential

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
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id
        if self.consumer_name is not None:
            result['consumerName'] = self.consumer_name
        if self.description is not None:
            result['description'] = self.description
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.credential_type is not None:
            result['credentialType'] = self.credential_type
        if self.route_names is not None:
            result['routeNames'] = self.route_names
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.credentials is not None:
            result['credentials'] = [i.to_dict() for i in self.credentials]
        if self.iam_credential is not None:
            result['iamCredential'] = self.iam_credential.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ConsumerDetailInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')
        if m.get('consumerName') is not None:
            self.consumer_name = m.get('consumerName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('credentialType') is not None:
            self.credential_type = m.get('credentialType')
        if m.get('routeNames') is not None:
            self.route_names = m.get('routeNames')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('credentials') is not None:
            self.credentials = [ConsumerCredentialInfo().from_dict(i) for i in m.get('credentials')]
        if m.get('iamCredential') is not None:
            self.iam_credential = IAMCredentialSpec().from_dict(m.get('iamCredential'))
        return self
