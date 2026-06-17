"""
Request entity for ChangeToPrepaidRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ChangeToPrepaidRequest(AbstractModel):
    """
    Request entity for ChangeToPrepaidRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, duration, auto_renew=None, auto_renew_period=None, relation_cds=None):
        """
        Initialize ChangeToPrepaidRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param duration: 购买时长（单位：月）
        :type duration: int (required)

        :param auto_renew: 实例到期后是否自动续费，取值：true：自动续费，false：不自动续费，默认值：false。
        :type auto_renew: bool (optional)

        :param auto_renew_period: auto_renew_period parameter
        :type auto_renew_period: int (optional)

        :param relation_cds: 变更关联的数据盘，已废弃，关联的按量付费（后付费）CDS需同BCC一起变更为包年包月（预付费）。
        :type relation_cds: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.duration = duration
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.relation_cds = relation_cds

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
        if self.duration is not None:
            result['duration'] = self.duration
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period
        if self.relation_cds is not None:
            result['relationCds'] = self.relation_cds
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ChangeToPrepaidRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')
        if m.get('relationCds') is not None:
            self.relation_cds = m.get('relationCds')
        return self
