"""
Request entity for CreateVolumeClusterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.billing import Billing
from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class CreateVolumeClusterRequest(AbstractModel):
    """
    Request entity for CreateVolumeClusterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, cluster_name, cluster_size_in_gb, storage_type, billing, zone_name=None, purchase_count=None, tags=None
    ):
        """
        Initialize CreateVolumeClusterRequest request entity.

        :param zone_name: 指定可用区信息，默认为空，由系统自动选择。
        :type zone_name: str (optional)

        :param cluster_name: 创建CDS专属集群的名字。
        :type cluster_name: str (required)

        :param cluster_size_in_gb: 集群总容量单位GB，最小容量85TB，最大容量1015TB，购买步长10TB。
        :type cluster_size_in_gb: int (required)

        :param storage_type: storage_type parameter
        :type storage_type: str (required)

        :param purchase_count: 创建CDS专属集群的数量，必须大于0的证书，缺省值为1
        :type purchase_count: int (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param tags: 待创建的标签列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.zone_name = zone_name
        self.cluster_name = cluster_name
        self.cluster_size_in_gb = cluster_size_in_gb
        self.storage_type = storage_type
        self.purchase_count = purchase_count
        self.billing = billing
        self.tags = tags

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
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.cluster_size_in_gb is not None:
            result['clusterSizeInGB'] = self.cluster_size_in_gb
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.purchase_count is not None:
            result['purchaseCount'] = self.purchase_count
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateVolumeClusterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('clusterSizeInGB') is not None:
            self.cluster_size_in_gb = m.get('clusterSizeInGB')
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('purchaseCount') is not None:
            self.purchase_count = m.get('purchaseCount')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
