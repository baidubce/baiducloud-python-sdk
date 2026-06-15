"""
Request entity for AutoReleaseInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AutoReleaseInstanceRequest(AbstractModel):
    """
    Request entity for AutoReleaseInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, is_eip_auto_related_delete=None, release_time=None):
        """
        Initialize AutoReleaseInstanceRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param is_eip_auto_related_delete: is_eip_auto_related_delete parameter
        :type is_eip_auto_related_delete: bool (optional)

        :param release_time: 释放时间，格式yyyy-MM-dd'T'HH:mm:ss'Z'，不传表示取消定时释放
        :type release_time: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.is_eip_auto_related_delete = is_eip_auto_related_delete
        self.release_time = release_time

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
        if self.is_eip_auto_related_delete is not None:
            result['isEipAutoRelatedDelete'] = self.is_eip_auto_related_delete
        if self.release_time is not None:
            result['releaseTime'] = self.release_time
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AutoReleaseInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isEipAutoRelatedDelete') is not None:
            self.is_eip_auto_related_delete = m.get('isEipAutoRelatedDelete')
        if m.get('releaseTime') is not None:
            self.release_time = m.get('releaseTime')
        return self
