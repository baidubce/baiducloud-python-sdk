"""
Request entity for CreateIpSetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateIpSetRequest(AbstractModel):
    """
    Request entity for CreateIpSetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, ip_version, ip_set_ids, client_token=None, description=None):
        """
        Initialize CreateIpSetRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: IP地址族的名称，限制：大小写字母、数字、中文以及-_/.特殊字符，必须以字母或者中文开头，长度1-65
        :type name: str (required)

        :param ip_version: ipVersion，取值IPv4或IPv6
        :type ip_version: str (required)

        :param ip_set_ids: 关联的IP地址组ID，其ipVersion需与本次创建的IP地址族一致，单次最多指定5个
        :type ip_set_ids: List[str] (required)

        :param description: IP地址族描述，长度不超过255
        :type description: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.ip_version = ip_version
        self.ip_set_ids = ip_set_ids
        self.description = description

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
        if self.name is not None:
            result['name'] = self.name
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.ip_set_ids is not None:
            result['ipSetIds'] = self.ip_set_ids
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateIpSetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('ipSetIds') is not None:
            self.ip_set_ids = m.get('ipSetIds')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
