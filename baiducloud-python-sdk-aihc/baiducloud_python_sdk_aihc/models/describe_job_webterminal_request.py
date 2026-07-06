"""
Request entity for DescribeJobWebterminalRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeJobWebterminalRequest(AbstractModel):
    """
    Request entity for DescribeJobWebterminalRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, resource_pool_id, queue_id, job_id, pod_name, handshake_timeout_second=None, ping_timeout_second=None
    ):
        """
        Initialize DescribeJobWebterminalRequest request entity.

        :param resource_pool_id: resource_pool_id parameter
        :type resource_pool_id: str (required)

        :param queue_id: queue_id parameter
        :type queue_id: str (required)

        :param job_id: 训练任务ID
        :type job_id: str (required)

        :param pod_name: 训练任务节点名称
        :type pod_name: str (required)

        :param handshake_timeout_second: 连接超时参数，仅在建立连接时使用，单位秒，默认值30，最小值1
        :type handshake_timeout_second: str (optional)

        :param ping_timeout_second: 心跳超时参数，单位秒，默认值900，最小值1，最大值3600
        :type ping_timeout_second: str (optional)
        """
        super().__init__()
        self.resource_pool_id = resource_pool_id
        self.queue_id = queue_id
        self.job_id = job_id
        self.pod_name = pod_name
        self.handshake_timeout_second = handshake_timeout_second
        self.ping_timeout_second = ping_timeout_second

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
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.pod_name is not None:
            result['podName'] = self.pod_name
        if self.handshake_timeout_second is not None:
            result['handshakeTimeoutSecond'] = self.handshake_timeout_second
        if self.ping_timeout_second is not None:
            result['pingTimeoutSecond'] = self.ping_timeout_second
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeJobWebterminalRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resourcePoolId') is not None:
            self.resource_pool_id = m.get('resourcePoolId')
        if m.get('queueID') is not None:
            self.queue_id = m.get('queueID')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('podName') is not None:
            self.pod_name = m.get('podName')
        if m.get('handshakeTimeoutSecond') is not None:
            self.handshake_timeout_second = m.get('handshakeTimeoutSecond')
        if m.get('pingTimeoutSecond') is not None:
            self.ping_timeout_second = m.get('pingTimeoutSecond')
        return self
