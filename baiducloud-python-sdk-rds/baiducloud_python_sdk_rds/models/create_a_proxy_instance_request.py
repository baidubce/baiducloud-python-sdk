"""
Request entity for CreateAProxyInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rds.models.billing import Billing
from baiducloud_python_sdk_rds.models.subnet_map import SubnetMap


class CreateAProxyInstanceRequest(AbstractModel):
    """
    Request entity for CreateAProxyInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        billing,
        source_instance_id,
        node_amount,
        client_token=None,
        instance_name=None,
        zone_names=None,
        vpc_id=None,
        is_direct_pay=None,
        subnets=None,
        ovip=None,
        entry_port=None,
        resource_group_id=None,
    ):
        """
        Initialize CreateAProxyInstanceRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param source_instance_id: 主实例ID
        :type source_instance_id: str (required)

        :param instance_name: 用户自定义实例名，要求： 1）允许小写字母、数字； 2）长度限制为1~32； 默认为rdsproxy
        :type instance_name: str (optional)

        :param node_amount: 代理实例节点数。取值范围2，4，6，8，16。
        :type node_amount: int (required)

        :param zone_names: zone_names parameter
        :type zone_names: List[str] (optional)

        :param vpc_id: 与主实例vpcId相同。
        :type vpc_id: str (optional)

        :param is_direct_pay: 是否进行直接支付，默认false，设置为直接支付的变配订单会直接扣款，不需要在走支付逻辑。
        :type is_direct_pay: bool (optional)

        :param subnets: subnets parameter
        :type subnets: List[SubnetMap] (optional)

        :param ovip: ovip parameter
        :type ovip: str (optional)

        :param entry_port: entry_port parameter
        :type entry_port: int (optional)

        :param resource_group_id: 资源分组Id，例如：RESG-bKMxbExtnoG。
        :type resource_group_id: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.billing = billing
        self.source_instance_id = source_instance_id
        self.instance_name = instance_name
        self.node_amount = node_amount
        self.zone_names = zone_names
        self.vpc_id = vpc_id
        self.is_direct_pay = is_direct_pay
        self.subnets = subnets
        self.ovip = ovip
        self.entry_port = entry_port
        self.resource_group_id = resource_group_id

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
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.source_instance_id is not None:
            result['sourceInstanceId'] = self.source_instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount
        if self.zone_names is not None:
            result['zoneNames'] = self.zone_names
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.is_direct_pay is not None:
            result['isDirectPay'] = self.is_direct_pay
        if self.subnets is not None:
            result['subnets'] = [i.to_dict() for i in self.subnets]
        if self.ovip is not None:
            result['ovip'] = self.ovip
        if self.entry_port is not None:
            result['entryPort'] = self.entry_port
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAProxyInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('sourceInstanceId') is not None:
            self.source_instance_id = m.get('sourceInstanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')
        if m.get('zoneNames') is not None:
            self.zone_names = m.get('zoneNames')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('isDirectPay') is not None:
            self.is_direct_pay = m.get('isDirectPay')
        if m.get('subnets') is not None:
            self.subnets = [SubnetMap().from_dict(i) for i in m.get('subnets')]
        if m.get('ovip') is not None:
            self.ovip = m.get('ovip')
        if m.get('entryPort') is not None:
            self.entry_port = m.get('entryPort')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self
