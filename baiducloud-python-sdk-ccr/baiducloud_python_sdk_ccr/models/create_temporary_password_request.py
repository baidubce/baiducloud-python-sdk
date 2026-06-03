"""
Request entity for CreateTemporaryPasswordRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateTemporaryPasswordRequest(AbstractModel):
    """
    Request entity for CreateTemporaryPasswordRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, duration):
        """
        Initialize CreateTemporaryPasswordRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param duration: 临时密码有效时间，单位：小时
        :type duration: int (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.duration = duration

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateTemporaryPasswordRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        return self
