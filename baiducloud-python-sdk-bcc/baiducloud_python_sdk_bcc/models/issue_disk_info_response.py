"""
IssueDiskInfoResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class IssueDiskInfoResponse(BceResponse):
    """
    IssueDiskInfoResponse
    """

    def __init__(self, issue_disk_sn=None):
        """
        Initialize IssueDiskInfoResponse instance.

        :param issue_disk_sn: 故障磁盘sn
        :type issue_disk_sn: str (optional)
        """
        super().__init__()
        self.issue_disk_sn = issue_disk_sn

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.issue_disk_sn is not None:
            result['issueDiskSn'] = self.issue_disk_sn
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IssueDiskInfoResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('issueDiskSn') is not None:
            self.issue_disk_sn = m.get('issueDiskSn')
        return self
