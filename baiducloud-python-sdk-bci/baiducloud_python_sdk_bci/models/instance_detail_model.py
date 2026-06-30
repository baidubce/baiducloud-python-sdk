"""
InstanceDetailModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bci.models.volume import Volume

from baiducloud_python_sdk_bci.models.container_detail_model import ContainerDetailModel

from baiducloud_python_sdk_bci.models.container_detail_model import ContainerDetailModel

from baiducloud_python_sdk_bci.models.security_group_model import SecurityGroupModel

from baiducloud_python_sdk_bci.models.vpc_model import VpcModel

from baiducloud_python_sdk_bci.models.subnet_model import SubnetModel


class InstanceDetailModel(AbstractModel):
    """
    InstanceDetailModel
    """

    def __init__(
        self, volume=None, containers=None, init_containers=None, security_groups=None, vpc=None, subnet=None
    ):
        """
        Initialize InstanceDetailModel instance.

        :param volume: volume attribute
        :type volume: Volume (optional)

        :param containers: 业务容器
        :type containers: List[ContainerDetailModel] (optional)

        :param init_containers: init容器
        :type init_containers: List[ContainerDetailModel] (optional)

        :param security_groups: 安全组信息
        :type security_groups: List[SecurityGroupModel] (optional)

        :param vpc: vpc attribute
        :type vpc: VpcModel (optional)

        :param subnet: subnet attribute
        :type subnet: SubnetModel (optional)
        """
        super().__init__()
        self.volume = volume
        self.containers = containers
        self.init_containers = init_containers
        self.security_groups = security_groups
        self.vpc = vpc
        self.subnet = subnet

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
        if self.volume is not None:
            result['volume'] = self.volume.to_dict()
        if self.containers is not None:
            result['containers'] = [i.to_dict() for i in self.containers]
        if self.init_containers is not None:
            result['initContainers'] = [i.to_dict() for i in self.init_containers]
        if self.security_groups is not None:
            result['securityGroups'] = [i.to_dict() for i in self.security_groups]
        if self.vpc is not None:
            result['vpc'] = self.vpc.to_dict()
        if self.subnet is not None:
            result['subnet'] = self.subnet.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceDetailModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volume') is not None:
            self.volume = Volume().from_dict(m.get('volume'))
        if m.get('containers') is not None:
            self.containers = [ContainerDetailModel().from_dict(i) for i in m.get('containers')]
        if m.get('initContainers') is not None:
            self.init_containers = [ContainerDetailModel().from_dict(i) for i in m.get('initContainers')]
        if m.get('securityGroups') is not None:
            self.security_groups = [SecurityGroupModel().from_dict(i) for i in m.get('securityGroups')]
        if m.get('vpc') is not None:
            self.vpc = VpcModel().from_dict(m.get('vpc'))
        if m.get('subnet') is not None:
            self.subnet = SubnetModel().from_dict(m.get('subnet'))
        return self
