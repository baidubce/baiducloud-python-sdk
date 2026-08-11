"""
Request entity for DeleteL3MountTargetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteL3MountTargetRequest(AbstractModel):
    """
    Request entity for DeleteL3MountTargetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, mount_target_id):
        """
        Initialize DeleteL3MountTargetRequest request entity.

        :param instance_id: PFS实例ID
        :type instance_id: str (required)

        :param mount_target_id: PFS实例的挂载点ID
        :type mount_target_id: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.mount_target_id = mount_target_id

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.mount_target_id is not None:
            result['mountTargetId'] = self.mount_target_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteL3MountTargetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('mountTargetId') is not None:
            self.mount_target_id = m.get('mountTargetId')
        return self
