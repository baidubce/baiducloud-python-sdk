"""
EhcCluster information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EhcCluster(AbstractModel):
    """
    EhcCluster
    """

    def __init__(
        self,
        ehc_cluster_id=None,
        name=None,
        description=None,
        zone_name=None,
        created_time=None,
        instance_ids=None,
        reserved_instance_ids=None,
    ):
        """
        Initialize EhcCluster instance.

        :param ehc_cluster_id: EHC集群id（EHC集群列表接口返回）
        :type ehc_cluster_id: str (optional)

        :param name: EHC集群name（EHC集群列表接口返回）
        :type name: str (optional)

        :param description: EHC集群描述（EHC集群列表接口返回）
        :type description: str (optional)

        :param zone_name: 可用区信息（EHC集群列表接口返回）
        :type zone_name: str (optional)

        :param created_time: 创建时间（EHC集群列表接口返回）
        :type created_time: str (optional)

        :param instance_ids: 集群下实例id列表（EHC集群列表接口返回）
        :type instance_ids: List[str] (optional)

        :param reserved_instance_ids: 集群下预留实例券id列表（EHC集群列表接口返回）
        :type reserved_instance_ids: List[str] (optional)
        """
        super().__init__()
        self.ehc_cluster_id = ehc_cluster_id
        self.name = name
        self.description = description
        self.zone_name = zone_name
        self.created_time = created_time
        self.instance_ids = instance_ids
        self.reserved_instance_ids = reserved_instance_ids

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
        if self.ehc_cluster_id is not None:
            result['ehcClusterId'] = self.ehc_cluster_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.reserved_instance_ids is not None:
            result['reservedInstanceIds'] = self.reserved_instance_ids
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EhcCluster

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('reservedInstanceIds') is not None:
            self.reserved_instance_ids = m.get('reservedInstanceIds')
        return self
