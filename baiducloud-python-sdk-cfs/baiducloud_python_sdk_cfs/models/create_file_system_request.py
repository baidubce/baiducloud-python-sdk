"""
Request entity for CreateFileSystemRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cfs.models.tag import Tag


class CreateFileSystemRequest(AbstractModel):
    """
    Request entity for CreateFileSystemRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, fs_name, zone, type=None, protocol=None, tags=None, capacity_quota=None):
        """
        Initialize CreateFileSystemRequest request entity.

        :param fs_name: FileSystem的名称，方便记忆。长度1~65个字节，字母开头，可包含字母数字-_/.字符。
        :type fs_name: str (required)

        :param zone: FileSystem所在可用区，例如zoneB。
        :type zone: str (required)

        :param type: 文件系统类型：1.cap(容量型) 2.ssd(性能型) 当前默认是容量型
        :type type: str (optional)

        :param protocol: 协议类型：1.nfs 2.smb，默认nfs协议。
        :type protocol: str (optional)

        :param tags: 文件系统标签
        :type tags: List[Tag] (optional)

        :param capacity_quota: capacity_quota parameter
        :type capacity_quota: int (optional)
        """
        super().__init__()
        self.fs_name = fs_name
        self.zone = zone
        self.type = type
        self.protocol = protocol
        self.tags = tags
        self.capacity_quota = capacity_quota

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
        if self.fs_name is not None:
            result['fsName'] = self.fs_name
        if self.zone is not None:
            result['zone'] = self.zone
        if self.type is not None:
            result['type'] = self.type
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.capacity_quota is not None:
            result['capacityQuota'] = self.capacity_quota
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateFileSystemRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fsName') is not None:
            self.fs_name = m.get('fsName')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('capacityQuota') is not None:
            self.capacity_quota = m.get('capacityQuota')
        return self
