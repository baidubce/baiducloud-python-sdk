"""
Request entity for ModifyTbspIpProtectLevelRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyTbspIpProtectLevelRequest(AbstractModel):
    """
    Request entity for ModifyTbspIpProtectLevelRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, client_token=None, ip=None, protect_level=None):
        """
        Initialize ModifyTbspIpProtectLevelRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ip: DDoS增强防护包防护对象IP地址
        :type ip: str (optional)

        :param protect_level: 防护等级，可为1（宽松）、2（适中）、3（严格）
        :type protect_level: int (optional)
        """
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.ip = ip
        self.protect_level = protect_level

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
        if self.ip is not None:
            result['ip'] = self.ip
        if self.protect_level is not None:
            result['protectLevel'] = self.protect_level
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyTbspIpProtectLevelRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('protectLevel') is not None:
            self.protect_level = m.get('protectLevel')
        return self
