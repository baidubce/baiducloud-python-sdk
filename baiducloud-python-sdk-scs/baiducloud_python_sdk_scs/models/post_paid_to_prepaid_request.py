"""
Request entity for PostPaidToPrepaidRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PostPaidToPrepaidRequest(AbstractModel):
    """
    Request entity for PostPaidToPrepaidRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, duration, instance_ids):
        """
        Initialize PostPaidToPrepaidRequest request entity.

        :param duration: 转预付费的时长，单位月。最小值1。
        :type duration: int (required)

        :param instance_ids: 集群ID列表。
        :type instance_ids: List[str] (required)
        """
        super().__init__()
        self.duration = duration
        self.instance_ids = instance_ids

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
        if self.duration is not None:
            result['duration'] = self.duration
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PostPaidToPrepaidRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        return self
