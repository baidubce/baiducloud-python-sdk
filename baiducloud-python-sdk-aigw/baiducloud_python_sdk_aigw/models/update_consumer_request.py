"""
Request entity for UpdateConsumerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_aigw.models.tag import Tag
from baiducloud_python_sdk_aigw.models.credential_op import CredentialOp
from baiducloud_python_sdk_aigw.models.consumer_credential_location import ConsumerCredentialLocation
from baiducloud_python_sdk_aigw.models.iam_credential_spec import IAMCredentialSpec


class UpdateConsumerRequest(AbstractModel):
    """
    Request entity for UpdateConsumerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        consumer_id,
        x_region,
        key_type=None,
        description=None,
        route_names=None,
        tags=None,
        credential_op=None,
        credential_location=None,
        iam_credential=None,
    ):
        """
        Initialize UpdateConsumerRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param consumer_id: consumer_id parameter
        :type consumer_id: str (required)

        :param key_type: key_type parameter
        :type key_type: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param route_names: 关联路由列表
        :type route_names: List[str] (optional)

        :param tags: 标签列表
        :type tags: List[Tag] (optional)

        :param credential_op: credential_op parameter
        :type credential_op: CredentialOp (optional)

        :param credential_location: credential_location parameter
        :type credential_location: ConsumerCredentialLocation (optional)

        :param iam_credential: iam_credential parameter
        :type iam_credential: IAMCredentialSpec (optional)

        :param x_region: x_region parameter
        :type x_region: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.consumer_id = consumer_id
        self.key_type = key_type
        self.description = description
        self.route_names = route_names
        self.tags = tags
        self.credential_op = credential_op
        self.credential_location = credential_location
        self.iam_credential = iam_credential
        self.x_region = x_region

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
        if self.description is not None:
            result['description'] = self.description
        if self.route_names is not None:
            result['routeNames'] = self.route_names
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.credential_op is not None:
            result['credentialOp'] = self.credential_op.to_dict()
        if self.credential_location is not None:
            result['credentialLocation'] = self.credential_location.to_dict()
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
        :rtype: UpdateConsumerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')
        if m.get('keyType') is not None:
            self.key_type = m.get('keyType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('routeNames') is not None:
            self.route_names = m.get('routeNames')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('credentialOp') is not None:
            self.credential_op = CredentialOp().from_dict(m.get('credentialOp'))
        if m.get('credentialLocation') is not None:
            self.credential_location = ConsumerCredentialLocation().from_dict(m.get('credentialLocation'))
        if m.get('iamCredential') is not None:
            self.iam_credential = IAMCredentialSpec().from_dict(m.get('iamCredential'))
        if m.get('X-Region') is not None:
            self.x_region = m.get('X-Region')
        return self
