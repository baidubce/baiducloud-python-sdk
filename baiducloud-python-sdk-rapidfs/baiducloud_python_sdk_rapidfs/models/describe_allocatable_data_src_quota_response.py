"""
Request entity for DescribeAllocatableDataSrcQuotaResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.data_src_quota_info import DataSrcQuotaInfo


class DescribeAllocatableDataSrcQuotaResponse(BceResponse):
    """
    DescribeAllocatableDataSrcQuotaResponse
    """

    def __init__(self, data_src_quota_info=None):
        """
        Initialize DescribeAllocatableDataSrcQuotaResponse response.

        :param data_src_quota_info: data_src_quota_info field
        :type data_src_quota_info: DataSrcQuotaInfo (optional)
        """
        super().__init__()
        self.data_src_quota_info = data_src_quota_info

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
        if self.data_src_quota_info is not None:
            result['dataSrcQuotaInfo'] = self.data_src_quota_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAllocatableDataSrcQuotaResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('dataSrcQuotaInfo') is not None:
            self.data_src_quota_info = DataSrcQuotaInfo().from_dict(m.get('dataSrcQuotaInfo'))
        return self
