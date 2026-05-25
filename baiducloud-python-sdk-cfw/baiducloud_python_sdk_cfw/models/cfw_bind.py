"""
CfwBind information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CfwBind(AbstractModel):
    """
    CfwBind
    """

    def __init__(self, region=None, instance_id=None, role=None, member_id=None):
        """
        Initialize CfwBind instance.

        :param region: region attribute
        :type region: str (optional)

        :param instance_id: 关联的实例的id
        :type instance_id: str (optional)

        :param role: role attribute
        :type role: str (optional)

        :param member_id: CSN实例特有属性，CSN中网络实例id，当绑定、解绑实例为CSN时，该值必填
        :type member_id: str (optional)
        """
        super().__init__()
        self.region = region
        self.instance_id = instance_id
        self.role = role
        self.member_id = member_id

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
        if self.region is not None:
            result['region'] = self.region
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.role is not None:
            result['role'] = self.role
        if self.member_id is not None:
            result['memberId'] = self.member_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CfwBind

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        return self
