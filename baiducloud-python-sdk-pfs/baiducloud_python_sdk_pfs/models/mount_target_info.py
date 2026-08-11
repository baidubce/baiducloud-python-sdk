"""
MountTargetInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MountTargetInfo(AbstractModel):
    """
    MountTargetInfo
    """

    def __init__(self, domain=None, mount_target_id=None, ovip=None, vpc_id=None, subnet_id=None):
        """
        Initialize MountTargetInfo instance.

        :param domain: 挂载地址
        :type domain: str (optional)

        :param mount_target_id: 挂载点ID
        :type mount_target_id: str (optional)

        :param ovip: 挂载点IP
        :type ovip: str (optional)

        :param vpc_id: 挂载点所在VPCID
        :type vpc_id: str (optional)

        :param subnet_id: 挂载点所在子网ID
        :type subnet_id: str (optional)
        """
        super().__init__()
        self.domain = domain
        self.mount_target_id = mount_target_id
        self.ovip = ovip
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.mount_target_id is not None:
            result['mountTargetId'] = self.mount_target_id
        if self.ovip is not None:
            result['ovip'] = self.ovip
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MountTargetInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('mountTargetId') is not None:
            self.mount_target_id = m.get('mountTargetId')
        if m.get('ovip') is not None:
            self.ovip = m.get('ovip')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        return self
