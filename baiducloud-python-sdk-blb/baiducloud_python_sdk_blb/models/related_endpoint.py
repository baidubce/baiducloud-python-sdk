"""
RelatedEndpoint information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RelatedEndpoint(AbstractModel):
    """
    RelatedEndpoint
    """

    def __init__(self, endpoint_id=None, uid=None, attach_time=None):
        """
        Initialize RelatedEndpoint instance.

        :param endpoint_id: 服务网卡的id
        :type endpoint_id: str (optional)

        :param uid: 服务网卡对应用户id
        :type uid: str (optional)

        :param attach_time: 关联时间
        :type attach_time: str (optional)
        """
        super().__init__()
        self.endpoint_id = endpoint_id
        self.uid = uid
        self.attach_time = attach_time

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id
        if self.uid is not None:
            result['uid'] = self.uid
        if self.attach_time is not None:
            result['attachTime'] = self.attach_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RelatedEndpoint

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('attachTime') is not None:
            self.attach_time = m.get('attachTime')
        return self
