"""
Request entity for BatchDeleteInstancesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchDeleteInstancesRequest(AbstractModel):
    """
    Request entity for BatchDeleteInstancesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_ids, related_release_flag=None):
        """
        Initialize BatchDeleteInstancesRequest request entity.

        :param instance_ids: 待删除的BCI实例ID列表
        :type instance_ids: List[str] (required)

        :param related_release_flag: 释放关联资源（目前只有EIP资源），默认值：false
        :type related_release_flag: bool (optional)
        """
        super().__init__()
        self.instance_ids = instance_ids
        self.related_release_flag = related_release_flag

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
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.related_release_flag is not None:
            result['relatedReleaseFlag'] = self.related_release_flag
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchDeleteInstancesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('relatedReleaseFlag') is not None:
            self.related_release_flag = m.get('relatedReleaseFlag')
        return self
