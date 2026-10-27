"""
DataSrcInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rapidfs.models.mount_service_binding import MountServiceBinding


from baiducloud_python_sdk_core.annotation import host


class DataSrcInfo(AbstractModel):
    """
    DataSrcInfo
    """

    def __init__(
        self,
        data_src_name=None,
        data_src_id=None,
        instance_id=None,
        instance_name=None,
        mount_target=None,
        status=None,
        description=None,
        bucket=None,
        other_account=None,
        storage_type=None,
        bucket_endpoint=None,
        dir_prefix=None,
        sync_meta_on_import=None,
        keep_symlink=None,
        auth_group_id=None,
        auth_group_name=None,
        quota_mi_b=None,
        used_mi_b=None,
        mount_service_bindings=None,
    ):
        """
        Initialize DataSrcInfo instance.

        :param data_src_name: 数据源名称
        :type data_src_name: str (optional)

        :param data_src_id: 数据源唯一Id
        :type data_src_id: str (optional)

        :param instance_id: 所属的 RapidFS 实例唯一 Id
        :type instance_id: str (optional)

        :param instance_name: 所属的 RapidFS 实例名称
        :type instance_name: str (optional)

        :param mount_target: 用户客户端挂载该数据源的地址
        :type mount_target: str (optional)

        :param status: 数据源状态，见 DataSrcStatus
        :type status: str (optional)

        :param description: 描述信息
        :type description: str (optional)

        :param bucket: 数据源的 BOS bucket
        :type bucket: str (optional)

        :param other_account: 是否为其他账号的 bucket，非 BOS 数据源固定为true
        :type other_account: bool (optional)

        :param storage_type: 对象存储类型，BOS / OSS
        :type storage_type: str (optional)

        :param bucket_endpoint: 数据源实际使用的 endpoint，BOS 数据源导入且未显式传入时为后端推导值
        :type bucket_endpoint: str (optional)

        :param dir_prefix: 数据源的目录前缀
        :type dir_prefix: str (optional)

        :param sync_meta_on_import: 数据源导入时是否立即同步元数据， 默认 ture
        :type sync_meta_on_import: bool (optional)

        :param keep_symlink: 是否保留软链
        :type keep_symlink: bool (optional)

        :param auth_group_id: 权限组Id
        :type auth_group_id: str (optional)

        :param auth_group_name: 权限组名称
        :type auth_group_name: str (optional)

        :param quota_mi_b: 数据源的容量配额，-1 表示未设置
        :type quota_mi_b: int (optional)

        :param used_mi_b: 数据源已使用容量
        :type used_mi_b: int (optional)

        :param mount_service_bindings: 该数据源的绑定列表，见数据类型 MountServiceBinding
        :type mount_service_bindings: List[MountServiceBinding] (optional)
        """
        super().__init__()
        self.data_src_name = data_src_name
        self.data_src_id = data_src_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.mount_target = mount_target
        self.status = status
        self.description = description
        self._bucket = bucket
        self.other_account = other_account
        self.storage_type = storage_type
        self.bucket_endpoint = bucket_endpoint
        self.dir_prefix = dir_prefix
        self.sync_meta_on_import = sync_meta_on_import
        self.keep_symlink = keep_symlink
        self.auth_group_id = auth_group_id
        self.auth_group_name = auth_group_name
        self.quota_mi_b = quota_mi_b
        self.used_mi_b = used_mi_b
        self.mount_service_bindings = mount_service_bindings

    @property
    @host
    def bucket(self):
        """数据源的 BOS bucket"""
        return self._bucket

    @bucket.setter
    def bucket(self, value):
        """Set bucket value"""
        self._bucket = value

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
        if self.data_src_name is not None:
            result['dataSrcName'] = self.data_src_name
        if self.data_src_id is not None:
            result['dataSrcId'] = self.data_src_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.mount_target is not None:
            result['mountTarget'] = self.mount_target
        if self.status is not None:
            result['status'] = self.status
        if self.description is not None:
            result['description'] = self.description
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.other_account is not None:
            result['otherAccount'] = self.other_account
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.bucket_endpoint is not None:
            result['bucketEndpoint'] = self.bucket_endpoint
        if self.dir_prefix is not None:
            result['dirPrefix'] = self.dir_prefix
        if self.sync_meta_on_import is not None:
            result['syncMetaOnImport'] = self.sync_meta_on_import
        if self.keep_symlink is not None:
            result['keepSymlink'] = self.keep_symlink
        if self.auth_group_id is not None:
            result['authGroupId'] = self.auth_group_id
        if self.auth_group_name is not None:
            result['authGroupName'] = self.auth_group_name
        if self.quota_mi_b is not None:
            result['quotaMiB'] = self.quota_mi_b
        if self.used_mi_b is not None:
            result['usedMiB'] = self.used_mi_b
        if self.mount_service_bindings is not None:
            result['mountServiceBindings'] = [i.to_dict() for i in self.mount_service_bindings]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DataSrcInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('dataSrcName') is not None:
            self.data_src_name = m.get('dataSrcName')
        if m.get('dataSrcId') is not None:
            self.data_src_id = m.get('dataSrcId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('mountTarget') is not None:
            self.mount_target = m.get('mountTarget')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('otherAccount') is not None:
            self.other_account = m.get('otherAccount')
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('bucketEndpoint') is not None:
            self.bucket_endpoint = m.get('bucketEndpoint')
        if m.get('dirPrefix') is not None:
            self.dir_prefix = m.get('dirPrefix')
        if m.get('syncMetaOnImport') is not None:
            self.sync_meta_on_import = m.get('syncMetaOnImport')
        if m.get('keepSymlink') is not None:
            self.keep_symlink = m.get('keepSymlink')
        if m.get('authGroupId') is not None:
            self.auth_group_id = m.get('authGroupId')
        if m.get('authGroupName') is not None:
            self.auth_group_name = m.get('authGroupName')
        if m.get('quotaMiB') is not None:
            self.quota_mi_b = m.get('quotaMiB')
        if m.get('usedMiB') is not None:
            self.used_mi_b = m.get('usedMiB')
        if m.get('mountServiceBindings') is not None:
            self.mount_service_bindings = [MountServiceBinding().from_dict(i) for i in m.get('mountServiceBindings')]
        return self
