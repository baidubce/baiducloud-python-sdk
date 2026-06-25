"""
Request entity for ClaimAlertEventRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ClaimAlertEventRequest(AbstractModel):
    """
    Request entity for ClaimAlertEventRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, event_ids, claim_reason=None):
        """
        Initialize ClaimAlertEventRequest request entity.

        :param event_ids: 要认领的事件 ID 列表（1-100 个）
        :type event_ids: List[str] (required)

        :param claim_reason: 认领原因（最大 500 字符）
        :type claim_reason: str (optional)
        """
        super().__init__()
        self.event_ids = event_ids
        self.claim_reason = claim_reason

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
        if self.event_ids is not None:
            result['eventIds'] = self.event_ids
        if self.claim_reason is not None:
            result['claimReason'] = self.claim_reason
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClaimAlertEventRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eventIds') is not None:
            self.event_ids = m.get('eventIds')
        if m.get('claimReason') is not None:
            self.claim_reason = m.get('claimReason')
        return self
