"""
ContainerSecurityContext information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bci.models.capabilities import Capabilities


class ContainerSecurityContext(AbstractModel):
    """
    ContainerSecurityContext
    """

    def __init__(
        self,
        capabilities=None,
        run_as_user=None,
        run_as_group=None,
        run_as_non_root=None,
        read_only_root_filesystem=None,
    ):
        """
        Initialize ContainerSecurityContext instance.

        :param capabilities: capabilities attribute
        :type capabilities: Capabilities (optional)

        :param run_as_user: 运行容器的用户ID
        :type run_as_user: int (optional)

        :param run_as_group: 运行容器进程入口点的GID
        :type run_as_group: int (optional)

        :param run_as_non_root: 是否必须以非root用户运行
        :type run_as_non_root: bool (optional)

        :param read_only_root_filesystem: 根文件系统是否只读，默认false
        :type read_only_root_filesystem: bool (optional)
        """
        super().__init__()
        self.capabilities = capabilities
        self.run_as_user = run_as_user
        self.run_as_group = run_as_group
        self.run_as_non_root = run_as_non_root
        self.read_only_root_filesystem = read_only_root_filesystem

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
        if self.capabilities is not None:
            result['capabilities'] = self.capabilities.to_dict()
        if self.run_as_user is not None:
            result['runAsUser'] = self.run_as_user
        if self.run_as_group is not None:
            result['runAsGroup'] = self.run_as_group
        if self.run_as_non_root is not None:
            result['runAsNonRoot'] = self.run_as_non_root
        if self.read_only_root_filesystem is not None:
            result['readOnlyRootFilesystem'] = self.read_only_root_filesystem
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ContainerSecurityContext

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('capabilities') is not None:
            self.capabilities = Capabilities().from_dict(m.get('capabilities'))
        if m.get('runAsUser') is not None:
            self.run_as_user = m.get('runAsUser')
        if m.get('runAsGroup') is not None:
            self.run_as_group = m.get('runAsGroup')
        if m.get('runAsNonRoot') is not None:
            self.run_as_non_root = m.get('runAsNonRoot')
        if m.get('readOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('readOnlyRootFilesystem')
        return self
