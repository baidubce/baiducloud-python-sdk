"""
Request entity for GetAspResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.auto_snapshot_policy_model import AutoSnapshotPolicyModel


class GetAspResponse(BceResponse):
    """
    GetAspResponse
    """

    def __init__(self, auto_snapshot_policy=None):
        """
        Initialize GetAspResponse response.

        :param auto_snapshot_policy: auto_snapshot_policy field
        :type auto_snapshot_policy: AutoSnapshotPolicyModel (optional)
        """
        super().__init__()
        self.auto_snapshot_policy = auto_snapshot_policy

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.auto_snapshot_policy is not None:
            result['autoSnapshotPolicy'] = self.auto_snapshot_policy.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetAspResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('autoSnapshotPolicy') is not None:
            self.auto_snapshot_policy = AutoSnapshotPolicyModel().from_dict(m.get('autoSnapshotPolicy'))
        return self
