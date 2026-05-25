"""
Request entity for AddElasticNetworkCardAuxiliaryIpResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class AddElasticNetworkCardAuxiliaryIpResponse(BceResponse):
    """
    AddElasticNetworkCardAuxiliaryIpResponse
    """

    def __init__(self, private_ip_address=None):
        """
        Initialize AddElasticNetworkCardAuxiliaryIpResponse response.

        :param private_ip_address: 添加的弹性网卡的内网IP地址
        :type private_ip_address: str (optional)
        """
        super().__init__()
        self.private_ip_address = private_ip_address

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
        if self.private_ip_address is not None:
            result['privateIpAddress'] = self.private_ip_address
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddElasticNetworkCardAuxiliaryIpResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('privateIpAddress') is not None:
            self.private_ip_address = m.get('privateIpAddress')
        return self
