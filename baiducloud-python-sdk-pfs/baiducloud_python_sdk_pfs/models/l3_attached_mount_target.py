"""
L3AttachedMountTarget information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class L3AttachedMountTarget(AbstractModel):
    """
    L3AttachedMountTarget
    """

    def __init__(
        self,
        mount_target_id=None,
        mount_target_name=None,
        instance_id=None,
        instance_name=None,
    ):
        """
        Initialize L3AttachedMountTarget instance.

        :param mount_target_id: 挂载点 ID
        :type mount_target_id: str (optional)

        :param mount_target_name: 挂载点名称
        :type mount_target_name: str (optional)

        :param instance_id: PFS实例ID
        :type instance_id: str (optional)

        :param instance_name: PFS实例名称
        :type instance_name: str (optional)
        """
        super().__init__()
        self.mount_target_id = mount_target_id
        self.mount_target_name = mount_target_name
        self.instance_id = instance_id
        self.instance_name = instance_name

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
        if self.mount_target_id is not None:
            result['mountTargetId'] = self.mount_target_id
        if self.mount_target_name is not None:
            result['mountTargetName'] = self.mount_target_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: L3AttachedMountTarget

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('mountTargetId') is not None:
            self.mount_target_id = m.get('mountTargetId')
        if m.get('mountTargetName') is not None:
            self.mount_target_name = m.get('mountTargetName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        return self
