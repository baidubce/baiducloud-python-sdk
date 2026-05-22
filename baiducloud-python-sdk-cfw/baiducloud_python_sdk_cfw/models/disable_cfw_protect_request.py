"""
Request entity for DisableCfwProtectRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DisableCfwProtectRequest(AbstractModel):
    """
    Request entity for DisableCfwProtectRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cfw_id, instance_id, role=None, member_id=None):
        """
        Initialize DisableCfwProtectRequest request entity.

        :param cfw_id: cfw_id parameter
        :type cfw_id: str (required)

        :param instance_id: 防护实例的id
        :type instance_id: str (required)

        :param role: role parameter
        :type role: str (optional)

        :param member_id: CSN实例特有属性，CSN中网络实例id，当实例为CSN时，该值必填
        :type member_id: str (optional)
        """
        super().__init__()
        self.cfw_id = cfw_id
        self.instance_id = instance_id
        self.role = role
        self.member_id = member_id

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
        if self.role is not None:
            result['role'] = self.role
        if self.member_id is not None:
            result['memberId'] = self.member_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DisableCfwProtectRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cfwId') is not None:
            self.cfw_id = m.get('cfwId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        return self
