"""
Request entity for SharedDataPackageInquiryRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SharedDataPackageInquiryRequest(AbstractModel):
    """
    Request entity for SharedDataPackageInquiryRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, reservation_length, capacity, client_token=None, deduct_policy=None, package_type=None):
        """
        Initialize SharedDataPackageInquiryRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param reservation_length: 共享流量包有效期（单位：月），1/6/12
        :type reservation_length: int (required)

        :param capacity: 共享流量包容量，有效期为1时，对应可选规格 \"10G\"/\"50G\"/\"100G\"/\"500G\"/\"1T\"/\"5T\"/\"10T\"/\"50T\"；
            有效期为6时，对应可选规格 \"60G\"/\"300G\"/\"600G\"/\"3T\"/\"6T\"/\"30T\"/\"60T\"/\"300T\"；
            有效期为12时，对应可选规格 \"1T\"/\"10T\"/\"50T\"/\"100T\"/\"500T\"/\"1P\"，需按照对应可选规格进行容量选择
        :type capacity: str (required)

        :param deduct_policy: 共享流量包扣费策略，包含 \"FullTimeDurationPackage\" 全时；\"TimeDurationPackage\" 闲时，默认为
            \"FullTimeDurationPackage\"
        :type deduct_policy: str (optional)

        :param package_type: 共享流量包线路类型，当前支持 \"WebOutBytes\" 动态，默认为 \"WebOutBytes\"
        :type package_type: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.reservation_length = reservation_length
        self.capacity = capacity
        self.deduct_policy = deduct_policy
        self.package_type = package_type

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
        if self.reservation_length is not None:
            result['reservationLength'] = self.reservation_length
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.deduct_policy is not None:
            result['deductPolicy'] = self.deduct_policy
        if self.package_type is not None:
            result['packageType'] = self.package_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SharedDataPackageInquiryRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('reservationLength') is not None:
            self.reservation_length = m.get('reservationLength')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('deductPolicy') is not None:
            self.deduct_policy = m.get('deductPolicy')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        return self
