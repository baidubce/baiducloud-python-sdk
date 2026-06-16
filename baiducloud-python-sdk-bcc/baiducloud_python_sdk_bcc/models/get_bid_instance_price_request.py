"""
Request entity for GetBidInstancePriceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.create_cds_model import CreateCdsModel


class GetBidInstancePriceRequest(AbstractModel):
    """
    Request entity for GetBidInstancePriceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        spec,
        zone_name,
        root_disk_size_in_gb=None,
        root_disk_storage_type=None,
        create_cds_list=None,
        network_capacity_in_mbps=None,
        internet_charge_type=None,
        purchase_count=None,
    ):
        """
        Initialize GetBidInstancePriceRequest request entity.

        :param spec: 套餐规格
        :type spec: str (required)

        :param root_disk_size_in_gb: root_disk_size_in_gb parameter
        :type root_disk_size_in_gb: int (optional)

        :param root_disk_storage_type: 待创建虚拟机实例系统盘介质，默认使用SSD型云磁盘，可指定系统盘磁盘类型
        :type root_disk_storage_type: str (optional)

        :param create_cds_list: 待创建的CDS磁盘列表
        :type create_cds_list: List[CreateCdsModel] (optional)

        :param network_capacity_in_mbps: 公网带宽，单位Mbps，0~200，0表示不分配公网IP
        :type network_capacity_in_mbps: int (optional)

        :param internet_charge_type: 公网带宽计费方式
        :type internet_charge_type: str (optional)

        :param purchase_count: 批量创建（购买）的虚拟机实例个数，必须为大于0的整数，可选参数，缺省为1
        :type purchase_count: int (optional)

        :param zone_name: zone_name parameter
        :type zone_name: str (required)
        """
        super().__init__()
        self.spec = spec
        self.root_disk_size_in_gb = root_disk_size_in_gb
        self.root_disk_storage_type = root_disk_storage_type
        self.create_cds_list = create_cds_list
        self.network_capacity_in_mbps = network_capacity_in_mbps
        self.internet_charge_type = internet_charge_type
        self.purchase_count = purchase_count
        self.zone_name = zone_name

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
        if self.spec is not None:
            result['spec'] = self.spec
        if self.root_disk_size_in_gb is not None:
            result['rootDiskSizeInGb'] = self.root_disk_size_in_gb
        if self.root_disk_storage_type is not None:
            result['rootDiskStorageType'] = self.root_disk_storage_type
        if self.create_cds_list is not None:
            result['createCdsList'] = [i.to_dict() for i in self.create_cds_list]
        if self.network_capacity_in_mbps is not None:
            result['networkCapacityInMbps'] = self.network_capacity_in_mbps
        if self.internet_charge_type is not None:
            result['internetChargeType'] = self.internet_charge_type
        if self.purchase_count is not None:
            result['purchaseCount'] = self.purchase_count
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetBidInstancePriceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('rootDiskSizeInGb') is not None:
            self.root_disk_size_in_gb = m.get('rootDiskSizeInGb')
        if m.get('rootDiskStorageType') is not None:
            self.root_disk_storage_type = m.get('rootDiskStorageType')
        if m.get('createCdsList') is not None:
            self.create_cds_list = [CreateCdsModel().from_dict(i) for i in m.get('createCdsList')]
        if m.get('networkCapacityInMbps') is not None:
            self.network_capacity_in_mbps = m.get('networkCapacityInMbps')
        if m.get('internetChargeType') is not None:
            self.internet_charge_type = m.get('internetChargeType')
        if m.get('purchaseCount') is not None:
            self.purchase_count = m.get('purchaseCount')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self
