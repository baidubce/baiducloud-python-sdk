"""
Request entity for ModifyInstanceHostnameRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyInstanceHostnameRequest(AbstractModel):
    """
    Request entity for ModifyInstanceHostnameRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, instance_id, hostname, reboot=None, is_open_hostname_domain=None, is_allow_hostname_repeat=None
    ):
        """
        Initialize ModifyInstanceHostnameRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param reboot: 是否自动重启，默认false
        :type reboot: bool (optional)

        :param is_open_hostname_domain: 是否开启hostname domain true:是 false:否，默认false
        :type is_open_hostname_domain: bool (optional)

        :param hostname: 实例主机名
        :type hostname: str (required)

        :param is_allow_hostname_repeat: 是否允许hostname重复 true:是 false:否，默认false
        :type is_allow_hostname_repeat: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.reboot = reboot
        self.is_open_hostname_domain = is_open_hostname_domain
        self.hostname = hostname
        self.is_allow_hostname_repeat = is_allow_hostname_repeat

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
        if self.reboot is not None:
            result['reboot'] = self.reboot
        if self.is_open_hostname_domain is not None:
            result['isOpenHostnameDomain'] = self.is_open_hostname_domain
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.is_allow_hostname_repeat is not None:
            result['isAllowHostnameRepeat'] = self.is_allow_hostname_repeat
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyInstanceHostnameRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('reboot') is not None:
            self.reboot = m.get('reboot')
        if m.get('isOpenHostnameDomain') is not None:
            self.is_open_hostname_domain = m.get('isOpenHostnameDomain')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('isAllowHostnameRepeat') is not None:
            self.is_allow_hostname_repeat = m.get('isAllowHostnameRepeat')
        return self
