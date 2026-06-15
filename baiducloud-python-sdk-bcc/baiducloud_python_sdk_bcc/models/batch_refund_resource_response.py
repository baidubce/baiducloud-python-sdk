"""
Request entity for BatchRefundResourceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class BatchRefundResourceResponse(BceResponse):
    """
    BatchRefundResourceResponse
    """

    def __init__(self, failed_instance_ids=None):
        """
        Initialize BatchRefundResourceResponse response.

        :param failed_instance_ids: 删除失败的实例列表
        :type failed_instance_ids: List[str] (optional)
        """
        super().__init__()
        self.failed_instance_ids = failed_instance_ids

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
        if self.failed_instance_ids is not None:
            result['failedInstanceIds'] = self.failed_instance_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchRefundResourceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('failedInstanceIds') is not None:
            self.failed_instance_ids = m.get('failedInstanceIds')
        return self
