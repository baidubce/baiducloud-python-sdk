"""
Request entity for RebootInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RebootInstanceRequest(AbstractModel):
    """
    Request entity for RebootInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, force_stop=None):
        """
        Initialize RebootInstanceRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param force_stop: 是否强制停止实例，可选值true,false,缺省为false
        :type force_stop: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.force_stop = force_stop

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
        if self.force_stop is not None:
            result['forceStop'] = self.force_stop
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RebootInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('forceStop') is not None:
            self.force_stop = m.get('forceStop')
        return self
