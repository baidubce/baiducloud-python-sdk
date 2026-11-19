"""
MountTargetBindConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MountTargetBindConfig(AbstractModel):
    """
    MountTargetBindConfig
    """

    def __init__(self, mount_target_id=None, mount_path=None):
        """
        Initialize MountTargetBindConfig instance.

        :param mount_target_id: 挂载服务 ID
        :type mount_target_id: str (optional)

        :param mount_path: 挂载路径
        :type mount_path: str (optional)
        """
        super().__init__()
        self.mount_target_id = mount_target_id
        self.mount_path = mount_path

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
        # The server declares mountPath as required and generates "/pfs/<instanceId>" when it is empty,
        # so an unset value is sent as an empty string.
        result['mountPath'] = self.mount_path if self.mount_path is not None else ''
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MountTargetBindConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('mountTargetId') is not None:
            self.mount_target_id = m.get('mountTargetId')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        return self
