"""
ReservedInstance information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReservedInstance(AbstractModel):
    """
    ReservedInstance
    """

    def __init__(self, reserved_instance_id=None, zone_name=None, reserved_instance_name=None, ehc_cluster_id=None):
        """
        Initialize ReservedInstance instance.

        :param reserved_instance_id: 要调整的预留实例券id
        :type reserved_instance_id: str (optional)

        :param zone_name: 要调整的目标可用区，例如cn-bj-b。不支持同时修改reservedInstanceName
        :type zone_name: str (optional)

        :param reserved_instance_name: reserved_instance_name attribute
        :type reserved_instance_name: str (optional)

        :param ehc_cluster_id: 变更roce预留实例券时可选参数，若为空则使用默认EHC集群
        :type ehc_cluster_id: str (optional)
        """
        super().__init__()
        self.reserved_instance_id = reserved_instance_id
        self.zone_name = zone_name
        self.reserved_instance_name = reserved_instance_name
        self.ehc_cluster_id = ehc_cluster_id

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
        if self.reserved_instance_id is not None:
            result['reservedInstanceId'] = self.reserved_instance_id
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.reserved_instance_name is not None:
            result['reservedInstanceName'] = self.reserved_instance_name
        if self.ehc_cluster_id is not None:
            result['ehcClusterId'] = self.ehc_cluster_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReservedInstance

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservedInstanceId') is not None:
            self.reserved_instance_id = m.get('reservedInstanceId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('reservedInstanceName') is not None:
            self.reserved_instance_name = m.get('reservedInstanceName')
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        return self
