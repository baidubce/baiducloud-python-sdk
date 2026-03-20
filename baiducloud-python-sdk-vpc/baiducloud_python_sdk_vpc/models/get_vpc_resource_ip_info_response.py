"""
Request entity for GetVpcResourceIpInfoResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.resource_ip import ResourceIp


class GetVpcResourceIpInfoResponse(BceResponse):
    """
    GetVpcResourceIpInfoResponse
    """

    def __init__(self, page_no=None, page_size=None, total_count=None, result=None):
        """
        Initialize GetVpcResourceIpInfoResponse response.

        :param page_no: page number
        :type page_no: int (optional)

        :param page_size: page size
        :type page_size: int (optional)

        :param total_count: 满足查询条件的结果集总数
        :type total_count: int (optional)

        :param result: VPC内产品占用IP分页信息
        :type result: List[ResourceIp] (optional)
        """
        super().__init__()
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.result = result

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
            result['metadata'] = self.metadata
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetVpcResourceIpInfoResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('result') is not None:
            self.result = [ResourceIp().from_dict(i) for i in m.get('result')]
        return self
