"""
QueryApikeyDetailsPermanentlyValidResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_iam.models.acl import ACL


class QueryApikeyDetailsPermanentlyValidResponse(BceResponse):
    """
    QueryApikeyDetailsPermanentlyValidResponse
    """

    def __init__(
        self,
        id=None,
        token_id=None,
        name=None,
        user_id=None,
        services=None,
        create_time=None,
        update_time=None,
        domain_id=None,
        acl=None,
    ):
        """
        Initialize QueryApikeyDetailsPermanentlyValidResponse instance.

        :param id: API Key在的标识
        :type id: str (optional)

        :param token_id: API Key本身
        :type token_id: str (optional)

        :param name: API Key名称
        :type name: str (optional)

        :param user_id: API Key 归属的子用户
        :type user_id: str (optional)

        :param services: API Key 授权的服务列表
        :type services: List[str] (optional)

        :param create_time: API Key 创建时间
        :type create_time: str (optional)

        :param update_time: API Key 更新时间
        :type update_time: str (optional)

        :param domain_id: API Key 归属的账户
        :type domain_id: str (optional)

        :param acl: acl attribute
        :type acl: ACL (optional)
        """
        super().__init__()
        self.id = id
        self.token_id = token_id
        self.name = name
        self.user_id = user_id
        self.services = services
        self.create_time = create_time
        self.update_time = update_time
        self.domain_id = domain_id
        self.acl = acl

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.id is not None:
            result['id'] = self.id
        if self.token_id is not None:
            result['tokenId'] = self.token_id
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.services is not None:
            result['services'] = self.services
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.acl is not None:
            result['acl'] = self.acl.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryApikeyDetailsPermanentlyValidResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('services') is not None:
            self.services = m.get('services')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('acl') is not None:
            self.acl = ACL().from_dict(m.get('acl'))
        return self
