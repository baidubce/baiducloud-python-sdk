"""
EipConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.eip_group_increase import EipGroupIncrease

from baiducloud_python_sdk_as.models.eip_group_decrease import EipGroupDecrease

from baiducloud_python_sdk_as.models.eip_group_bandwidth import EipGroupBandwidth


class EipConfig(AbstractModel):
    """
    EipConfig
    """

    def __init__(
        self,
        eip_group_bind_strategy=None,
        eip_group_unbind_strategy=None,
        eip_group_id_list=None,
        increase=None,
        decrease=None,
        bandwidth=None,
    ):
        """
        Initialize EipConfig instance.

        :param eip_group_bind_strategy: 共享带宽扩容时与BCC绑定策略
        :type eip_group_bind_strategy: str (optional)

        :param eip_group_unbind_strategy: 共享带宽缩容时策略
        :type eip_group_unbind_strategy: str (optional)

        :param eip_group_id_list: 共享带宽组id列表
        :type eip_group_id_list: List[str] (optional)

        :param increase: increase attribute
        :type increase: EipGroupIncrease (optional)

        :param decrease: decrease attribute
        :type decrease: EipGroupDecrease (optional)

        :param bandwidth: bandwidth attribute
        :type bandwidth: EipGroupBandwidth (optional)
        """
        super().__init__()
        self.eip_group_bind_strategy = eip_group_bind_strategy
        self.eip_group_unbind_strategy = eip_group_unbind_strategy
        self.eip_group_id_list = eip_group_id_list
        self.increase = increase
        self.decrease = decrease
        self.bandwidth = bandwidth

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
        if self.eip_group_bind_strategy is not None:
            result['eipGroupBindStrategy'] = self.eip_group_bind_strategy
        if self.eip_group_unbind_strategy is not None:
            result['eipGroupUnbindStrategy'] = self.eip_group_unbind_strategy
        if self.eip_group_id_list is not None:
            result['eipGroupIdList'] = self.eip_group_id_list
        if self.increase is not None:
            result['increase'] = self.increase.to_dict()
        if self.decrease is not None:
            result['decrease'] = self.decrease.to_dict()
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EipConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eipGroupBindStrategy') is not None:
            self.eip_group_bind_strategy = m.get('eipGroupBindStrategy')
        if m.get('eipGroupUnbindStrategy') is not None:
            self.eip_group_unbind_strategy = m.get('eipGroupUnbindStrategy')
        if m.get('eipGroupIdList') is not None:
            self.eip_group_id_list = m.get('eipGroupIdList')
        if m.get('increase') is not None:
            self.increase = EipGroupIncrease().from_dict(m.get('increase'))
        if m.get('decrease') is not None:
            self.decrease = EipGroupDecrease().from_dict(m.get('decrease'))
        if m.get('bandwidth') is not None:
            self.bandwidth = EipGroupBandwidth().from_dict(m.get('bandwidth'))
        return self
