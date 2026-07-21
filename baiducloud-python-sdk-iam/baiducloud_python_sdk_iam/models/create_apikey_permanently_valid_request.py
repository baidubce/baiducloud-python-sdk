"""
Request entity for CreateApikeyPermanentlyValidRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_iam.models.acl import ACL


class CreateApikeyPermanentlyValidRequest(AbstractModel):
    """
    Request entity for CreateApikeyPermanentlyValidRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, acl, user_id=None, name=None):
        """
        Initialize CreateApikeyPermanentlyValidRequest request entity.

        :param user_id: 子用户Id；不传就是当前用户
        :type user_id: str (optional)

        :param acl: acl parameter
        :type acl: ACL (required)

        :param name: APIKey名称；不传会默认生成
        :type name: str (optional)
        """
        super().__init__()
        self.user_id = user_id
        self.acl = acl
        self.name = name

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
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.acl is not None:
            result['acl'] = self.acl.to_dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateApikeyPermanentlyValidRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('acl') is not None:
            self.acl = ACL().from_dict(m.get('acl'))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
