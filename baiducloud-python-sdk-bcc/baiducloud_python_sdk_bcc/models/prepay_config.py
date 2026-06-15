"""
PrepayConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PrepayConfig(AbstractModel):
    """
    PrepayConfig
    """

    def __init__(
        self, instance_id=None, auto_renew=None, auto_renew_period=None, duration=None, cds_list=None, auto_pay=None
    ):
        """
        Initialize PrepayConfig instance.

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param auto_renew: 实例到期后是否自动续费，取值：true：自动续费，false：不自动续费，默认值：false。
        :type auto_renew: bool (optional)

        :param auto_renew_period: auto_renew_period attribute
        :type auto_renew_period: int (optional)

        :param duration: 购买时长（单位：月）
        :type duration: int (optional)

        :param cds_list: cds_list attribute
        :type cds_list: List[str] (optional)

        :param auto_pay: 是否自动支付，默认true，表示自动支付
        :type auto_pay: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.duration = duration
        self.cds_list = cds_list
        self.auto_pay = auto_pay

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period
        if self.duration is not None:
            result['duration'] = self.duration
        if self.cds_list is not None:
            result['cdsList'] = self.cds_list
        if self.auto_pay is not None:
            result['autoPay'] = self.auto_pay
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PrepayConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('cdsList') is not None:
            self.cds_list = m.get('cdsList')
        if m.get('autoPay') is not None:
            self.auto_pay = m.get('autoPay')
        return self
