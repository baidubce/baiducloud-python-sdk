"""
HaVipBindedInstance information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HaVipBindedInstance(AbstractModel):
    """
    HaVipBindedInstance
    """

    def __init__(self, instance_id=None, instance_type=None, master=None):
        """
        Initialize HaVipBindedInstance instance.

        :param instance_id: 绑定的实例ID
        :type instance_id: str (optional)

        :param instance_type: 绑定的实例类型，\"SERVER\"表示云服务器（BCC/BBC/DCC），\"ENI\"表示弹性网卡
        :type instance_type: str (optional)

        :param master: 主备标识，true表示主，false表示备
        :type master: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.master = master

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
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.master is not None:
            result['master'] = self.master
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HaVipBindedInstance

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('master') is not None:
            self.master = m.get('master')
        return self
