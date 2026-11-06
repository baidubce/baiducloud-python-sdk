"""
Request entity for UpdateWhitelistRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateWhitelistRequest(AbstractModel):
    """
    Request entity for UpdateWhitelistRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, security_ips, action=None, tag=None):
        """
        Initialize UpdateWhitelistRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param action: action parameter
        :type action: str (optional)

        :param security_ips: 白名单IP列表
        :type security_ips: List[str] (required)

        :param tag: 指定的白名单分组名称，当 version 取值为2时，必填
        :type tag: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.action = action
        self.security_ips = security_ips
        self.tag = tag

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
        if self.security_ips is not None:
            result['securityIps'] = self.security_ips
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateWhitelistRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('securityIps') is not None:
            self.security_ips = m.get('securityIps')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self
