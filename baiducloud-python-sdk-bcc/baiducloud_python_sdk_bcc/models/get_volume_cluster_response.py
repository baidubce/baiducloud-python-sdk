"""
Request entity for GetVolumeClusterResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class GetVolumeClusterResponse(BceResponse):
    """
    GetVolumeClusterResponse
    """

    def __init__(
        self,
        cluster_id=None,
        cluster_name=None,
        created_time=None,
        expired_time=None,
        status=None,
        logical_zone=None,
        product_type=None,
        cluster_type=None,
        total_capacity=None,
        used_capacity=None,
        available_capacity=None,
        expanding_capacity=None,
        created_volume_num=None,
        affiliated_cds_number=None,
        enable_auto_renew=None,
        tags=None,
    ):
        """
        Initialize GetVolumeClusterResponse response.

        :param cluster_id: 专属集群ID
        :type cluster_id: str (optional)

        :param cluster_name: 专属集群名称,支持大小写字母、数字、中文以及-_ /.特殊字符，必须以字母开头，长度1-65
        :type cluster_name: str (optional)

        :param created_time: 创建日期，符合BCE日期规范
        :type created_time: str (optional)

        :param expired_time: 过期时间，符合BCE日期规范。
        :type expired_time: str (optional)

        :param status: 专属集群状态
        :type status: str (optional)

        :param logical_zone: 可用区
        :type logical_zone: str (optional)

        :param product_type: 专属集群付费类型
        :type product_type: str (optional)

        :param cluster_type: 专属集群类型
        :type cluster_type: str (optional)

        :param total_capacity: 专属集群总容量
        :type total_capacity: int (optional)

        :param used_capacity: 专属集群已使用容量
        :type used_capacity: int (optional)

        :param available_capacity: 专属集群可用容量
        :type available_capacity: int (optional)

        :param expanding_capacity: 专属集群扩展容量
        :type expanding_capacity: int (optional)

        :param created_volume_num: 由专属集群创建的CDS数量
        :type created_volume_num: int (optional)

        :param affiliated_cds_number: 由专属集群创建的CDS列表
        :type affiliated_cds_number: List[str] (optional)

        :param enable_auto_renew: 是否开启自动续费
        :type enable_auto_renew: bool (optional)

        :param tags: 绑定的标签
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.created_time = created_time
        self.expired_time = expired_time
        self.status = status
        self.logical_zone = logical_zone
        self.product_type = product_type
        self.cluster_type = cluster_type
        self.total_capacity = total_capacity
        self.used_capacity = used_capacity
        self.available_capacity = available_capacity
        self.expanding_capacity = expanding_capacity
        self.created_volume_num = created_volume_num
        self.affiliated_cds_number = affiliated_cds_number
        self.enable_auto_renew = enable_auto_renew
        self.tags = tags

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.status is not None:
            result['status'] = self.status
        if self.logical_zone is not None:
            result['logicalZone'] = self.logical_zone
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.total_capacity is not None:
            result['totalCapacity'] = self.total_capacity
        if self.used_capacity is not None:
            result['usedCapacity'] = self.used_capacity
        if self.available_capacity is not None:
            result['availableCapacity'] = self.available_capacity
        if self.expanding_capacity is not None:
            result['expandingCapacity'] = self.expanding_capacity
        if self.created_volume_num is not None:
            result['createdVolumeNum'] = self.created_volume_num
        if self.affiliated_cds_number is not None:
            result['affiliatedCDSNumber'] = self.affiliated_cds_number
        if self.enable_auto_renew is not None:
            result['enableAutoRenew'] = self.enable_auto_renew
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetVolumeClusterResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('logicalZone') is not None:
            self.logical_zone = m.get('logicalZone')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('totalCapacity') is not None:
            self.total_capacity = m.get('totalCapacity')
        if m.get('usedCapacity') is not None:
            self.used_capacity = m.get('usedCapacity')
        if m.get('availableCapacity') is not None:
            self.available_capacity = m.get('availableCapacity')
        if m.get('expandingCapacity') is not None:
            self.expanding_capacity = m.get('expandingCapacity')
        if m.get('createdVolumeNum') is not None:
            self.created_volume_num = m.get('createdVolumeNum')
        if m.get('affiliatedCDSNumber') is not None:
            self.affiliated_cds_number = m.get('affiliatedCDSNumber')
        if m.get('enableAutoRenew') is not None:
            self.enable_auto_renew = m.get('enableAutoRenew')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
