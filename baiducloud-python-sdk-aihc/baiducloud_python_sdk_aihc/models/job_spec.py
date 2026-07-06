"""
JobSpec information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_aihc.models.image_config import ImageConfig

from baiducloud_python_sdk_aihc.models.resource import Resource

from baiducloud_python_sdk_aihc.models.env import Env


class JobSpec(AbstractModel):
    """
    JobSpec
    """

    def __init__(
        self,
        image=None,
        image_config=None,
        replicas=None,
        resources=None,
        envs=None,
        enable_rdma=None,
        host_network=None,
    ):
        """
        Initialize JobSpec instance.

        :param image: 镜像地址，需要包含tag
        :type image: str (optional)

        :param image_config: image_config attribute
        :type image_config: ImageConfig (optional)

        :param replicas: worker副本数
        :type replicas: int (optional)

        :param resources: 配置资源配额
        :type resources: List[Resource] (optional)

        :param envs: envs attribute
        :type envs: List[Env] (optional)

        :param enable_rdma: enable_rdma attribute
        :type enable_rdma: bool (optional)

        :param host_network: host_network attribute
        :type host_network: bool (optional)
        """
        super().__init__()
        self.image = image
        self.image_config = image_config
        self.replicas = replicas
        self.resources = resources
        self.envs = envs
        self.enable_rdma = enable_rdma
        self.host_network = host_network

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
        if self.image is not None:
            result['image'] = self.image
        if self.image_config is not None:
            result['imageConfig'] = self.image_config.to_dict()
        if self.replicas is not None:
            result['replicas'] = self.replicas
        if self.resources is not None:
            result['resources'] = [i.to_dict() for i in self.resources]
        if self.envs is not None:
            result['envs'] = [i.to_dict() for i in self.envs]
        if self.enable_rdma is not None:
            result['enableRDMA'] = self.enable_rdma
        if self.host_network is not None:
            result['hostNetwork'] = self.host_network
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: JobSpec

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('imageConfig') is not None:
            self.image_config = ImageConfig().from_dict(m.get('imageConfig'))
        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')
        if m.get('resources') is not None:
            self.resources = [Resource().from_dict(i) for i in m.get('resources')]
        if m.get('envs') is not None:
            self.envs = [Env().from_dict(i) for i in m.get('envs')]
        if m.get('enableRDMA') is not None:
            self.enable_rdma = m.get('enableRDMA')
        if m.get('hostNetwork') is not None:
            self.host_network = m.get('hostNetwork')
        return self
