"""
Request entity for CreateConsumerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_aigw.models.tag import Tag
from baiducloud_python_sdk_aigw.models.consumer_credential_spec import ConsumerCredentialSpec
from baiducloud_python_sdk_aigw.models.iam_credential_spec import IAMCredentialSpec


class CreateConsumerRequest(AbstractModel):
    """
    Request entity for CreateConsumerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        consumer_name,
        auth_type,
        credential_type,
        description=None,
        route_names=None,
        tags=None,
        credential=None,
        iam_credential=None,
    ):
        """
        Initialize CreateConsumerRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param consumer_name: 消费者名称
        :type consumer_name: str (required)

        :param description: 描述
        :type description: str (optional)

        :param auth_type: KeyAuth 或 JWT
        :type auth_type: str (required)

        :param credential_type: LOCAL 或 IAM
        :type credential_type: str (required)

        :param route_names: 关联路由名称列表
        :type route_names: List[str] (optional)

        :param tags: 消费者标签
        :type tags: List[Tag] (optional)

        :param credential: credential parameter
        :type credential: ConsumerCredentialSpec (optional)

        :param iam_credential: iam_credential parameter
        :type iam_credential: IAMCredentialSpec (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.consumer_name = consumer_name
        self.description = description
        self.auth_type = auth_type
        self.credential_type = credential_type
        self.route_names = route_names
        self.tags = tags
        self.credential = credential
        self.iam_credential = iam_credential

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
        if self.credential is not None:
            result['credential'] = self.credential.to_dict()
        if self.iam_credential is not None:
            result['iamCredential'] = self.iam_credential.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateConsumerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
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
        if m.get('credential') is not None:
            self.credential = ConsumerCredentialSpec().from_dict(m.get('credential'))
        if m.get('iamCredential') is not None:
            self.iam_credential = IAMCredentialSpec().from_dict(m.get('iamCredential'))
        return self
