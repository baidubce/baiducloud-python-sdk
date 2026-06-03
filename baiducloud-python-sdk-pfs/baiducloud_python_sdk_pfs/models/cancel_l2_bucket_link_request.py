"""
Request entity for CancelL2BucketLinkRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CancelL2BucketLinkRequest(AbstractModel):
    """
    Request entity for CancelL2BucketLinkRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, bucket_link_id, instance_id):
        """
        Initialize CancelL2BucketLinkRequest request entity.

        :param bucket_link_id: 需要取消的数据流动ID
        :type bucket_link_id: str (required)

        :param instance_id: 取消数据流动任务所属PFS实例ID
        :type instance_id: str (required)
        """
        super().__init__()
        self.bucket_link_id = bucket_link_id
        self.instance_id = instance_id

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
        if self.bucket_link_id is not None:
            result['bucketLinkId'] = self.bucket_link_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CancelL2BucketLinkRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bucketLinkId') is not None:
            self.bucket_link_id = m.get('bucketLinkId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self
