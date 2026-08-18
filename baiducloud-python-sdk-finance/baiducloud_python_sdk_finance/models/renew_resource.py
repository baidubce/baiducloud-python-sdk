"""
RenewResource information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RenewResource(AbstractModel):
    """
    RenewResource
    """

    def __init__(
        self,
        service_type=None,
        region=None,
        short_id=None,
        account_id=None,
        instance_id=None,
        expire_time=None,
        alone_renew_enable=None,
        already_renew_set=None,
        renew_time_unit=None,
        renew_time=None,
    ):
        """
        Initialize RenewResource instance.

        :param service_type: 产品类型，例：BCC，BOS等
        :type service_type: str (optional)

        :param region: 区域，例如：bj
        :type region: str (optional)

        :param short_id: 资源短ID
        :type short_id: str (optional)

        :param account_id: 订单所有者账户ID
        :type account_id: str (optional)

        :param instance_id: 资源长ID
        :type instance_id: str (optional)

        :param expire_time: 预付费资源当前到期时间，UTC格式参考yyyy-MM-ddTHH:mm:ssZ
        :type expire_time: str (optional)

        :param alone_renew_enable: 是否可以单独开通自动续费，当前仅CDS的系统盘不支持单独开通自动续费
        :type alone_renew_enable: bool (optional)

        :param already_renew_set: 该预付费资源实例是否已经开通了自动续费
        :type already_renew_set: bool (optional)

        :param renew_time_unit: 自动续费时长单位，只有两种，month&year，分别表示月和年
        :type renew_time_unit: str (optional)

        :param renew_time: 自动续费时长，renewTimeUnit为month表示月数，renewTimeUnit为年标志年数
        :type renew_time: str (optional)
        """
        super().__init__()
        self.service_type = service_type
        self.region = region
        self.short_id = short_id
        self.account_id = account_id
        self.instance_id = instance_id
        self.expire_time = expire_time
        self.alone_renew_enable = alone_renew_enable
        self.already_renew_set = already_renew_set
        self.renew_time_unit = renew_time_unit
        self.renew_time = renew_time

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
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.region is not None:
            result['region'] = self.region
        if self.short_id is not None:
            result['shortId'] = self.short_id
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.alone_renew_enable is not None:
            result['aloneRenewEnable'] = self.alone_renew_enable
        if self.already_renew_set is not None:
            result['alreadyRenewSet'] = self.already_renew_set
        if self.renew_time_unit is not None:
            result['renewTimeUnit'] = self.renew_time_unit
        if self.renew_time is not None:
            result['renewTime'] = self.renew_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RenewResource

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('shortId') is not None:
            self.short_id = m.get('shortId')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('aloneRenewEnable') is not None:
            self.alone_renew_enable = m.get('aloneRenewEnable')
        if m.get('alreadyRenewSet') is not None:
            self.already_renew_set = m.get('alreadyRenewSet')
        if m.get('renewTimeUnit') is not None:
            self.renew_time_unit = m.get('renewTimeUnit')
        if m.get('renewTime') is not None:
            self.renew_time = m.get('renewTime')
        return self
