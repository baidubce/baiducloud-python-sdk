"""
Request entity for CreateInstanceUsingPOSTRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vdb.models.milvus_component import MilvusComponent
from baiducloud_python_sdk_vdb.models.instance_param import InstanceParam


class CreateInstanceUsingPOSTRequest(AbstractModel):
    """
    Request entity for CreateInstanceUsingPOSTRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        engine_type=None,
        auto_renew=None,
        auto_renew_time=None,
        auto_renew_time_unit=None,
        components=None,
        duration=None,
        env=None,
        instance_param=None,
        product_type=None,
        time_unit=None,
    ):
        """
        Initialize CreateInstanceUsingPOSTRequest request entity.

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)

        :param auto_renew: 是否自动续费
        :type auto_renew: bool (optional)

        :param auto_renew_time: 自动续费时长
        :type auto_renew_time: int (optional)

        :param auto_renew_time_unit: 自动续费时长单位
        :type auto_renew_time_unit: str (optional)

        :param components: 组件配置
        :type components: List[MilvusComponent] (optional)

        :param duration: 购买时长
        :type duration: int (optional)

        :param env: 环境
        :type env: str (optional)

        :param instance_param: instance_param parameter
        :type instance_param: InstanceParam (optional)

        :param product_type: 计费类型（prepay：预付费，postpay：后付费）
        :type product_type: str (optional)

        :param time_unit: 购买时长单位
        :type time_unit: str (optional)
        """
        super().__init__()
        self.engine_type = engine_type
        self.auto_renew = auto_renew
        self.auto_renew_time = auto_renew_time
        self.auto_renew_time_unit = auto_renew_time_unit
        self.components = components
        self.duration = duration
        self.env = env
        self.instance_param = instance_param
        self.product_type = product_type
        self.time_unit = time_unit

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
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        if self.auto_renew_time_unit is not None:
            result['autoRenewTimeUnit'] = self.auto_renew_time_unit
        if self.components is not None:
            result['components'] = [i.to_dict() for i in self.components]
        if self.duration is not None:
            result['duration'] = self.duration
        if self.env is not None:
            result['env'] = self.env
        if self.instance_param is not None:
            result['instanceParam'] = self.instance_param.to_dict()
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateInstanceUsingPOSTRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        if m.get('autoRenewTimeUnit') is not None:
            self.auto_renew_time_unit = m.get('autoRenewTimeUnit')
        if m.get('components') is not None:
            self.components = [MilvusComponent().from_dict(i) for i in m.get('components')]
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('env') is not None:
            self.env = m.get('env')
        if m.get('instanceParam') is not None:
            self.instance_param = InstanceParam().from_dict(m.get('instanceParam'))
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')
        return self
