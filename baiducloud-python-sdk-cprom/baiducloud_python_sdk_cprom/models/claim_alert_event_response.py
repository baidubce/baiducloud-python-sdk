"""
Request entity for ClaimAlertEventResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cprom.models.event_claim_detail import EventClaimDetail


class ClaimAlertEventResponse(BceResponse):
    """
    ClaimAlertEventResponse
    """

    def __init__(self, success_count=None, failed_count=None, details=None):
        """
        Initialize ClaimAlertEventResponse response.

        :param success_count: 成功认领数量
        :type success_count: int (optional)

        :param failed_count: 失败认领数量
        :type failed_count: int (optional)

        :param details: 认领详情
        :type details: List[EventClaimDetail] (optional)
        """
        super().__init__()
        self.success_count = success_count
        self.failed_count = failed_count
        self.details = details

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
        if self.success_count is not None:
            result['successCount'] = self.success_count
        if self.failed_count is not None:
            result['failedCount'] = self.failed_count
        if self.details is not None:
            result['details'] = [i.to_dict() for i in self.details]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClaimAlertEventResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')
        if m.get('failedCount') is not None:
            self.failed_count = m.get('failedCount')
        if m.get('details') is not None:
            self.details = [EventClaimDetail().from_dict(i) for i in m.get('details')]
        return self
