"""
Request entity for RefreshRobotAccountKeyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RefreshRobotAccountKeyRequest(AbstractModel):
    """
    Request entity for RefreshRobotAccountKeyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, robot_id, secret=None):
        """
        Initialize RefreshRobotAccountKeyRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param robot_id: robot_id parameter
        :type robot_id: str (required)

        :param secret: secret parameter
        :type secret: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.robot_id = robot_id
        self.secret = secret

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
        if self.secret is not None:
            result['secret'] = self.secret
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RefreshRobotAccountKeyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('robotID') is not None:
            self.robot_id = m.get('robotID')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        return self
