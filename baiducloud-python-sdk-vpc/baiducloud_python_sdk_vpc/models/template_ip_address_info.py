"""
TemplateIpAddressInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TemplateIpAddressInfo(AbstractModel):
    """
    TemplateIpAddressInfo
    """

    def __init__(self, ip_address=None, description=None):
        """
        Initialize TemplateIpAddressInfo instance.

        :param ip_address: 参数模板IP地址，可为具体IP地址或者CIDR块
        :type ip_address: str (optional)

        :param description: 参数模板IP地址，具体描述
        :type description: str (optional)
        """
        super().__init__()
        self.ip_address = ip_address
        self.description = description

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
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TemplateIpAddressInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
