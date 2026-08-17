"""
IAMCredentialSpec information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IAMCredentialSpec(AbstractModel):
    """
    IAMCredentialSpec
    """

    def __init__(
        self,
        name=None,
        iam_api_key_id=None,
        iam_token_id_masked=None,
        iam_user_id=None,
        iam_domain_id=None,
        resource_ids=None,
        in_header=None,
        in_query=None,
        key_names=None,
        status=None,
    ):
        """
        Initialize IAMCredentialSpec instance.

        :param name: 凭证名称
        :type name: str (optional)

        :param iam_api_key_id: IAM APIKey ID
        :type iam_api_key_id: str (optional)

        :param iam_token_id_masked: 脱敏 Token ID
        :type iam_token_id_masked: str (optional)

        :param iam_user_id: IAM 用户 ID
        :type iam_user_id: str (optional)

        :param iam_domain_id: IAM 域 ID
        :type iam_domain_id: str (optional)

        :param resource_ids: 授权资源 ID
        :type resource_ids: List[str] (optional)

        :param in_header: 是否放入请求头
        :type in_header: bool (optional)

        :param in_query: 是否放入查询参数
        :type in_query: bool (optional)

        :param key_names: 凭证键名
        :type key_names: List[str] (optional)

        :param status: 凭证状态
        :type status: str (optional)
        """
        super().__init__()
        self.name = name
        self.iam_api_key_id = iam_api_key_id
        self.iam_token_id_masked = iam_token_id_masked
        self.iam_user_id = iam_user_id
        self.iam_domain_id = iam_domain_id
        self.resource_ids = resource_ids
        self.in_header = in_header
        self.in_query = in_query
        self.key_names = key_names
        self.status = status

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
        if self.name is not None:
            result['name'] = self.name
        if self.iam_api_key_id is not None:
            result['iamApiKeyId'] = self.iam_api_key_id
        if self.iam_token_id_masked is not None:
            result['iamTokenIdMasked'] = self.iam_token_id_masked
        if self.iam_user_id is not None:
            result['iamUserId'] = self.iam_user_id
        if self.iam_domain_id is not None:
            result['iamDomainId'] = self.iam_domain_id
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.in_header is not None:
            result['inHeader'] = self.in_header
        if self.in_query is not None:
            result['inQuery'] = self.in_query
        if self.key_names is not None:
            result['keyNames'] = self.key_names
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IAMCredentialSpec

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('iamApiKeyId') is not None:
            self.iam_api_key_id = m.get('iamApiKeyId')
        if m.get('iamTokenIdMasked') is not None:
            self.iam_token_id_masked = m.get('iamTokenIdMasked')
        if m.get('iamUserId') is not None:
            self.iam_user_id = m.get('iamUserId')
        if m.get('iamDomainId') is not None:
            self.iam_domain_id = m.get('iamDomainId')
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('inHeader') is not None:
            self.in_header = m.get('inHeader')
        if m.get('inQuery') is not None:
            self.in_query = m.get('inQuery')
        if m.get('keyNames') is not None:
            self.key_names = m.get('keyNames')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
