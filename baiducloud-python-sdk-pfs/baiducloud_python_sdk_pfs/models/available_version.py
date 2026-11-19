"""
AvailableVersion information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_pfs.models.available_mount_service_info import AvailableMountServiceInfo


class AvailableVersion(AbstractModel):
    """
    AvailableVersion
    """

    def __init__(self, version_number=None, mount_service_infos=None):
        """
        Initialize AvailableVersion instance.

        :param version_number: 版本号
        :type version_number: str (optional)

        :param mount_service_infos: 该版本下可用的挂载服务信息列表
        :type mount_service_infos: List[AvailableMountServiceInfo] (optional)
        """
        super().__init__()
        self.version_number = version_number
        self.mount_service_infos = mount_service_infos

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
        if self.version_number is not None:
            result['versionNumber'] = self.version_number
        if self.mount_service_infos is not None:
            result['mountServiceInfos'] = [i.to_dict() for i in self.mount_service_infos]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AvailableVersion

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('versionNumber') is not None:
            self.version_number = m.get('versionNumber')
        if m.get('mountServiceInfos') is not None:
            self.mount_service_infos = [AvailableMountServiceInfo().from_dict(i) for i in m.get('mountServiceInfos')]
        return self
