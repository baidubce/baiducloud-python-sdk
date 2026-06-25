"""
ClaimedInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ClaimedInfo(AbstractModel):
    """
    ClaimedInfo
    """

    def __init__(self, is_claimed=None, user_name=None, claim_time=None, claim_reason=None):
        """
        Initialize ClaimedInfo instance.

        :param is_claimed: 是否认领
        :type is_claimed: bool (optional)

        :param user_name: 认领人用户名
        :type user_name: str (optional)

        :param claim_time: 认领时间（Unix 时间戳，秒）
        :type claim_time: int (optional)

        :param claim_reason: 认领原因
        :type claim_reason: str (optional)
        """
        super().__init__()
        self.is_claimed = is_claimed
        self.user_name = user_name
        self.claim_time = claim_time
        self.claim_reason = claim_reason

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
        if self.is_claimed is not None:
            result['isClaimed'] = self.is_claimed
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.claim_time is not None:
            result['claimTime'] = self.claim_time
        if self.claim_reason is not None:
            result['claimReason'] = self.claim_reason
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClaimedInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('isClaimed') is not None:
            self.is_claimed = m.get('isClaimed')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('claimTime') is not None:
            self.claim_time = m.get('claimTime')
        if m.get('claimReason') is not None:
            self.claim_reason = m.get('claimReason')
        return self
