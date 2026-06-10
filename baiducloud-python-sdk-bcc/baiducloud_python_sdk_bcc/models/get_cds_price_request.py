"""
Request entity for GetCdsPriceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetCdsPriceRequest(AbstractModel):
    """
    Request entity for GetCdsPriceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        storage_type,
        cds_size_in_gb,
        payment_timing,
        zone_name,
        purchase_count=None,
        purchase_length=None,
        cds_extra_io=None,
    ):
        """
        Initialize GetCdsPriceRequest request entity.

        :param storage_type: storage_type parameter
        :type storage_type: str (required)

        :param cds_size_in_gb: CDS磁盘容量
        :type cds_size_in_gb: int (required)

        :param payment_timing: 付费方式，包括Postpaid（后付费），Prepaid（预付费）两种
        :type payment_timing: str (required)

        :param zone_name: 可用区名称
        :type zone_name: str (required)

        :param purchase_count: 任意数量CDS的总价格，必须为大于0的整数，可选参数，缺省为1
        :type purchase_count: int (optional)

        :param purchase_length: 时长，可选值[1,2,3,4,5,6,7,8,9,12,24,36]，单位：月
        :type purchase_length: int (optional)

        :param cds_extra_io: 增强型SSD_PL1、增强型SSD_PL2、增强型SSD_PL3，支持购买额外IO性能
        :type cds_extra_io: int (optional)
        """
        super().__init__()
        self.storage_type = storage_type
        self.cds_size_in_gb = cds_size_in_gb
        self.payment_timing = payment_timing
        self.zone_name = zone_name
        self.purchase_count = purchase_count
        self.purchase_length = purchase_length
        self.cds_extra_io = cds_extra_io

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
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.cds_size_in_gb is not None:
            result['cdsSizeInGB'] = self.cds_size_in_gb
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.purchase_count is not None:
            result['purchaseCount'] = self.purchase_count
        if self.purchase_length is not None:
            result['purchaseLength'] = self.purchase_length
        if self.cds_extra_io is not None:
            result['cdsExtraIo'] = self.cds_extra_io
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetCdsPriceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('cdsSizeInGB') is not None:
            self.cds_size_in_gb = m.get('cdsSizeInGB')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('purchaseCount') is not None:
            self.purchase_count = m.get('purchaseCount')
        if m.get('purchaseLength') is not None:
            self.purchase_length = m.get('purchaseLength')
        if m.get('cdsExtraIo') is not None:
            self.cds_extra_io = m.get('cdsExtraIo')
        return self
