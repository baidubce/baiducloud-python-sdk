"""
Request entity for LstPerL2BktLnkExecLogRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LstPerL2BktLnkExecLogRequest(AbstractModel):
    """
    Request entity for LstPerL2BktLnkExecLogRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, bucket_link_id, start_time=None, end_time=None):
        """
        Initialize LstPerL2BktLnkExecLogRequest request entity.

        :param instance_id: PFS实例ID
        :type instance_id: str (required)

        :param bucket_link_id: 数据流动ID
        :type bucket_link_id: str (required)

        :param start_time: 查询日志起始时间戳(秒级)
        :type start_time: int (optional)

        :param end_time: 查询日志结束时间戳(秒级)
        :type end_time: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.bucket_link_id = bucket_link_id
        self.start_time = start_time
        self.end_time = end_time

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.bucket_link_id is not None:
            result['bucketLinkId'] = self.bucket_link_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LstPerL2BktLnkExecLogRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('bucketLinkId') is not None:
            self.bucket_link_id = m.get('bucketLinkId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self
