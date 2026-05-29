"""
Request entity for UpdateFileSystemRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateFileSystemRequest(AbstractModel):
    """
    Request entity for UpdateFileSystemRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, fs_id, fs_name=None, capacity_quota=None):
        """
        Initialize UpdateFileSystemRequest request entity.

        :param fs_id: fs_id parameter
        :type fs_id: str (required)

        :param fs_name: FileSystem的名称，方便记忆。长度1~65个字节，字母开头，可包含字母数字-_/.字符。
        :type fs_name: str (optional)

        :param capacity_quota: capacity_quota parameter
        :type capacity_quota: int (optional)
        """
        super().__init__()
        self.fs_id = fs_id
        self.fs_name = fs_name
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
        :rtype: UpdateFileSystemRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fsId') is not None:
            self.fs_id = m.get('fsId')
        if m.get('fsName') is not None:
            self.fs_name = m.get('fsName')
        if m.get('capacityQuota') is not None:
            self.capacity_quota = m.get('capacityQuota')
        return self
