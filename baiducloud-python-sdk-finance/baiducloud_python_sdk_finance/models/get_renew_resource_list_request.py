"""
Request entity for GetRenewResourceListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetRenewResourceListRequest(AbstractModel):
    """
    Request entity for GetRenewResourceListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        service_type,
        query_account_id=None,
        region=None,
        expired_days=None,
        short_or_instance_ids=None,
        page_no=None,
        page_size=None,
    ):
        """
        Initialize GetRenewResourceListRequest request entity.

        :param query_account_id: query_account_id parameter
        :type query_account_id: str (optional)

        :param service_type: 产品类型，例：BCC，EIP等，注意仅允许查询支持自动续费的产品
        :type service_type: str (required)

        :param region: 区域，bj,su,gz等
        :type region: str (optional)

        :param expired_days: 查询预付费资源过期天数，可以为null，默认查询全量，不能为负，不能大于90天
        :type expired_days: int (optional)

        :param short_or_instance_ids: 资源长短ID列表，可以通过订单 或者 月账单等OPEN API查询到相关感兴趣的资源ID信息。
        :type short_or_instance_ids: List[str] (optional)

        :param page_no: 分页查询的页数，从1开始计数，缺省值为1
        :type page_no: int (optional)

        :param page_size: 每页包含的最大数量，最大数量通常不超过1000，缺省值为100。
        :type page_size: int (optional)
        """
        super().__init__()
        self.query_account_id = query_account_id
        self.service_type = service_type
        self.region = region
        self.expired_days = expired_days
        self.short_or_instance_ids = short_or_instance_ids
        self.page_no = page_no
        self.page_size = page_size

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
        if self.query_account_id is not None:
            result['queryAccountId'] = self.query_account_id
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.region is not None:
            result['region'] = self.region
        if self.expired_days is not None:
            result['expiredDays'] = self.expired_days
        if self.short_or_instance_ids is not None:
            result['shortOrInstanceIds'] = self.short_or_instance_ids
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetRenewResourceListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('queryAccountId') is not None:
            self.query_account_id = m.get('queryAccountId')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('expiredDays') is not None:
            self.expired_days = m.get('expiredDays')
        if m.get('shortOrInstanceIds') is not None:
            self.short_or_instance_ids = m.get('shortOrInstanceIds')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
