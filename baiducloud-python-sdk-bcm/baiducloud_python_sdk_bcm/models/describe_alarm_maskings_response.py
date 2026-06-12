"""
Request entity for DescribeAlarmMaskingsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcm.models.alarm_masking_model import AlarmMaskingModel


class DescribeAlarmMaskingsResponse(BceResponse):
    """
    DescribeAlarmMaskingsResponse
    """

    def __init__(self, maskings=None, page_no=None, page_size=None, total_size=None):
        """
        Initialize DescribeAlarmMaskingsResponse response.

        :param maskings: 屏蔽规则列表
        :type maskings: List[AlarmMaskingModel] (optional)

        :param page_no: 页码
        :type page_no: int (optional)

        :param page_size: 每页条数
        :type page_size: int (optional)

        :param total_size: 总条数
        :type total_size: int (optional)
        """
        super().__init__()
        self.maskings = maskings
        self.page_no = page_no
        self.page_size = page_size
        self.total_size = total_size

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
        if self.maskings is not None:
            result['maskings'] = [i.to_dict() for i in self.maskings]
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAlarmMaskingsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('maskings') is not None:
            self.maskings = [AlarmMaskingModel().from_dict(i) for i in m.get('maskings')]
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self
