"""
Request entity for DelIpv6Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DelIpv6Request(AbstractModel):
    """
    Request entity for DelIpv6Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, ipv6_address=None, reboot=None):
        """
        Initialize DelIpv6Request request entity.

        :param instance_id: 实例id
        :type instance_id: str (required)

        :param ipv6_address: 需要释放的ipv6地址
        :type ipv6_address: str (optional)

        :param reboot: 是否重启，true表示重启，为空表示不重启。默认不重启false。
        :type reboot: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.ipv6_address = ipv6_address
        self.reboot = reboot

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.ipv6_address is not None:
            result['ipv6Address'] = self.ipv6_address
        if self.reboot is not None:
            result['reboot'] = self.reboot
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DelIpv6Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('ipv6Address') is not None:
            self.ipv6_address = m.get('ipv6Address')
        if m.get('reboot') is not None:
            self.reboot = m.get('reboot')
        return self
