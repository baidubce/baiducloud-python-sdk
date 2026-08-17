"""
Request entity for CreateConsumerResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_aigw.models.consumer_credential_info import ConsumerCredentialInfo


class CreateConsumerResponse(BceResponse):
    """
    CreateConsumerResponse
    """

    def __init__(
        self, success=None, status=None, consumer_id=None, credential=None, credentials=None, credential_type=None
    ):
        """
        Initialize CreateConsumerResponse response.

        :param success: 是否成功
        :type success: bool (optional)

        :param status: HTTP 状态码
        :type status: int (optional)

        :param consumer_id: 消费者 ID
        :type consumer_id: str (optional)

        :param credential: 创建后的凭证（敏感值）
        :type credential: str (optional)

        :param credentials: 多凭证详情
        :type credentials: List[ConsumerCredentialInfo] (optional)

        :param credential_type: 凭证类型
        :type credential_type: str (optional)
        """
        super().__init__()
        self.success = success
        self.status = status
        self.consumer_id = consumer_id
        self.credential = credential
        self.credentials = credentials
        self.credential_type = credential_type

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
        if self.success is not None:
            result['success'] = self.success
        if self.status is not None:
            result['status'] = self.status
        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id
        if self.credential is not None:
            result['credential'] = self.credential
        if self.credentials is not None:
            result['credentials'] = [i.to_dict() for i in self.credentials]
        if self.credential_type is not None:
            result['credentialType'] = self.credential_type
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateConsumerResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')
        if m.get('credential') is not None:
            self.credential = m.get('credential')
        if m.get('credentials') is not None:
            self.credentials = [ConsumerCredentialInfo().from_dict(i) for i in m.get('credentials')]
        if m.get('credentialType') is not None:
            self.credential_type = m.get('credentialType')
        return self
