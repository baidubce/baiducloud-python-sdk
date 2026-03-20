"""
ResourceIp information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResourceIp(AbstractModel):
    """
    ResourceIp
    """

    def __init__(self, ip=None, resource_type=None):
        """
        Initialize ResourceIp instance.

        :param ip: VPC内网IP
        :type ip: str (optional)

        :param resource_type: VPC内网IP所属产品
        :type resource_type: str (optional)
        """
        super().__init__()
        self.ip = ip
        self.resource_type = resource_type

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
        if self.ip is not None:
            result['ip'] = self.ip
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResourceIp

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self
