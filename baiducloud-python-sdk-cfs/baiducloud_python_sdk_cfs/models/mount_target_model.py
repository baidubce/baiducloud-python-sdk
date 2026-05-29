"""
MountTargetModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MountTargetModel(AbstractModel):
    """
    MountTargetModel
    """

    def __init__(self, access_group_name=None, domain=None, mount_id=None, ovip=None, subnet_id=None, vpc_id=None):
        """
        Initialize MountTargetModel instance.

        :param access_group_name: 访问组名称
        :type access_group_name: str (optional)

        :param domain: 挂载域名
        :type domain: str (optional)

        :param mount_id: MountTarget ID
        :type mount_id: str (optional)

        :param ovip: 挂载IP地址
        :type ovip: str (optional)

        :param subnet_id: 子网ID
        :type subnet_id: str (optional)

        :param vpc_id: VPC ID
        :type vpc_id: str (optional)
        """
        super().__init__()
        self.access_group_name = access_group_name
        self.domain = domain
        self.mount_id = mount_id
        self.ovip = ovip
        self.subnet_id = subnet_id
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
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        if self.domain is not None:
            result['domain'] = self.domain
        if self.mount_id is not None:
            result['mountId'] = self.mount_id
        if self.ovip is not None:
            result['ovip'] = self.ovip
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
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
        :rtype: MountTargetModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('mountId') is not None:
            self.mount_id = m.get('mountId')
        if m.get('ovip') is not None:
            self.ovip = m.get('ovip')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self
