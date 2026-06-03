"""
IDCCacheNodeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IDCCacheNodeInfo(AbstractModel):
    """
    IDCCacheNodeInfo
    """

    def __init__(self, ssh_user=None, ssh_password=None, ssh_port=None):
        """
        Initialize IDCCacheNodeInfo instance.

        :param ssh_user: SSH 用户名
        :type ssh_user: str (optional)

        :param ssh_password: ssh_password attribute
        :type ssh_password: str (optional)

        :param ssh_port: SSH 端口
        :type ssh_port: int (optional)
        """
        super().__init__()
        self.ssh_user = ssh_user
        self.ssh_password = ssh_password
        self.ssh_port = ssh_port

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
        if self.ssh_user is not None:
            result['sshUser'] = self.ssh_user
        if self.ssh_password is not None:
            result['sshPassword'] = self.ssh_password
        if self.ssh_port is not None:
            result['sshPort'] = self.ssh_port
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IDCCacheNodeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sshUser') is not None:
            self.ssh_user = m.get('sshUser')
        if m.get('sshPassword') is not None:
            self.ssh_password = m.get('sshPassword')
        if m.get('sshPort') is not None:
            self.ssh_port = m.get('sshPort')
        return self
