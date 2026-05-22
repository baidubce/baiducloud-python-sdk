"""
Request entity for UpdateBlbAclRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateBlbAclRequest(AbstractModel):
    """
    Request entity for UpdateBlbAclRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, client_token=None, support_acl=None):
        """
        Initialize UpdateBlbAclRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param support_acl: 是否支持ACL，缺省值为true，代表支持
        :type support_acl: bool (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.support_acl = support_acl

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
        if self.support_acl is not None:
            result['supportAcl'] = self.support_acl
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateBlbAclRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('supportAcl') is not None:
            self.support_acl = m.get('supportAcl')
        return self
