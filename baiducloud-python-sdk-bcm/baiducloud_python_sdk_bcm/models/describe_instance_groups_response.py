"""
Request entity for DescribeInstanceGroupsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcm.models.instance_group_summary import InstanceGroupSummary


class DescribeInstanceGroupsResponse(BceResponse):
    """
    DescribeInstanceGroupsResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        message=None,
        instance_groups=None,
        page_no=None,
        page_size=None,
        total_count=None,
    ):
        """
        Initialize DescribeInstanceGroupsResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 响应码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param instance_groups: 实例组列表
        :type instance_groups: List[InstanceGroupSummary] (optional)

        :param page_no: 页码
        :type page_no: int (optional)

        :param page_size: 页大小
        :type page_size: int (optional)

        :param total_count: 总数量
        :type total_count: int (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.instance_groups = instance_groups
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count

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
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.instance_groups is not None:
            result['instanceGroups'] = [i.to_dict() for i in self.instance_groups]
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeInstanceGroupsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('instanceGroups') is not None:
            self.instance_groups = [InstanceGroupSummary().from_dict(i) for i in m.get('instanceGroups')]
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self
