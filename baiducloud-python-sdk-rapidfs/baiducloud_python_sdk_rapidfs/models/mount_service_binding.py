"""
MountServiceBinding information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MountServiceBinding(AbstractModel):
    """
    MountServiceBinding
    """

    def __init__(
        self,
        mount_service_id=None,
        mount_service_name=None,
        data_src_id=None,
        data_src_name=None,
        logical_mount_path=None,
        status=None,
    ):
        """
        Initialize MountServiceBinding instance.

        :param mount_service_id: 挂载服务 Id。响应必返；请求可省略，省略时为默认挂载服务 MNTSVC-RAPIDFS_DEFAULT_ID
        :type mount_service_id: str (optional)

        :param mount_service_name: 挂载服务名称。响应必返；请求中为只读字段，传入会被忽略
        :type mount_service_name: str (optional)

        :param data_src_id: 数据源唯一 Id。响应必返；请求中为只读字段，以请求所属数据源为准，传入会被忽略
        :type data_src_id: str (optional)

        :param data_src_name: 数据源名称。响应必返；请求中为只读字段，传入会被忽略
        :type data_src_name: str (optional)

        :param logical_mount_path: logical_mount_path attribute
        :type logical_mount_path: str (optional)

        :param status: status attribute
        :type status: str (optional)
        """
        super().__init__()
        self.mount_service_id = mount_service_id
        self.mount_service_name = mount_service_name
        self.data_src_id = data_src_id
        self.data_src_name = data_src_name
        self.logical_mount_path = logical_mount_path
        self.status = status

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
        if self.mount_service_id is not None:
            result['mountServiceId'] = self.mount_service_id
        if self.mount_service_name is not None:
            result['mountServiceName'] = self.mount_service_name
        if self.data_src_id is not None:
            result['dataSrcId'] = self.data_src_id
        if self.data_src_name is not None:
            result['dataSrcName'] = self.data_src_name
        if self.logical_mount_path is not None:
            result['logicalMountPath'] = self.logical_mount_path
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MountServiceBinding

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('mountServiceId') is not None:
            self.mount_service_id = m.get('mountServiceId')
        if m.get('mountServiceName') is not None:
            self.mount_service_name = m.get('mountServiceName')
        if m.get('dataSrcId') is not None:
            self.data_src_id = m.get('dataSrcId')
        if m.get('dataSrcName') is not None:
            self.data_src_name = m.get('dataSrcName')
        if m.get('logicalMountPath') is not None:
            self.logical_mount_path = m.get('logicalMountPath')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
