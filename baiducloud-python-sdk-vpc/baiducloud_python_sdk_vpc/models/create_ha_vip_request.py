"""
Request entity for CreateHaVipRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateHaVipRequest(AbstractModel):
    """
    Request entity for CreateHaVipRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, subnet_id, private_ip_address, client_token=None, description=None):
        """
        Initialize CreateHaVipRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 高可用虚拟IP的名称，限制：大小写字母、数字、中文以及-_/.特殊字符，必须以字母或者中文开头，长度1-65
        :type name: str (required)

        :param subnet_id: 高可用虚拟IP所属的子网ID
        :type subnet_id: str (required)

        :param private_ip_address: 指定的IP地址，为\"\"表示自动分配IP地址
        :type private_ip_address: str (required)

        :param description: 高可用虚拟IP描述
        :type description: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.subnet_id = subnet_id
        self.private_ip_address = private_ip_address
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
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
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
        :rtype: CreateHaVipRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
