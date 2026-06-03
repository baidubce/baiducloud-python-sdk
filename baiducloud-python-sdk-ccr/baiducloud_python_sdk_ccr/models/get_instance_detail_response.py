"""
Request entity for GetInstanceDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.instance import Instance
from baiducloud_python_sdk_ccr.models.instance_statistic import InstanceStatistic
from baiducloud_python_sdk_ccr.models.instance_quota import InstanceQuota


class GetInstanceDetailResponse(BceResponse):
    """
    GetInstanceDetailResponse
    """

    def __init__(self, bucket=None, region=None, info=None, statistic=None, quota=None):
        """
        Initialize GetInstanceDetailResponse response.

        :param bucket: bos bucket
        :type bucket: str (optional)

        :param region: 地域
        :type region: str (optional)

        :param info: info field
        :type info: Instance (optional)

        :param statistic: statistic field
        :type statistic: InstanceStatistic (optional)

        :param quota: quota field
        :type quota: InstanceQuota (optional)
        """
        super().__init__()
        self.bucket = bucket
        self.region = region
        self.info = info
        self.statistic = statistic
        self.quota = quota

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
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.region is not None:
            result['region'] = self.region
        if self.info is not None:
            result['info'] = self.info.to_dict()
        if self.statistic is not None:
            result['statistic'] = self.statistic.to_dict()
        if self.quota is not None:
            result['quota'] = self.quota.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetInstanceDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('info') is not None:
            self.info = Instance().from_dict(m.get('info'))
        if m.get('statistic') is not None:
            self.statistic = InstanceStatistic().from_dict(m.get('statistic'))
        if m.get('quota') is not None:
            self.quota = InstanceQuota().from_dict(m.get('quota'))
        return self
