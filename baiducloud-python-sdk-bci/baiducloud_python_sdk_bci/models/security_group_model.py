"""
SecurityGroupModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SecurityGroupModel(AbstractModel):
    """
    SecurityGroupModel
    """

    def __init__(self, security_group_id=None, name=None, description=None, vpc_id=None):
        """
        Initialize SecurityGroupModel instance.

        :param security_group_id: 安全组ID
        :type security_group_id: str (optional)

        :param name: 安全组名称
        :type name: str (optional)

        :param description: 安全组描述
        :type description: str (optional)

        :param vpc_id: vpc Id
        :type vpc_id: str (optional)
        """
        super().__init__()
        self.security_group_id = security_group_id
        self.name = name
        self.description = description
        self.vpc_id = vpc_id

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
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SecurityGroupModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self
