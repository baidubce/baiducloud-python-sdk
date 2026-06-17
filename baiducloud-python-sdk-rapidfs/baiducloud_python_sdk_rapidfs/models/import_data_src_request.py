"""
Request entity for ImportDataSrcRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ImportDataSrcRequest(AbstractModel):
    """
    Request entity for ImportDataSrcRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        data_src_name,
        bucket,
        client_token=None,
        other_account=None,
        bucket_ak=None,
        bucket_sk=None,
        bucket_sts_token=None,
        dir_prefix=None,
        keep_symlink=None,
        auth_group_id=None,
        description=None,
        quota_mi_b=None,
    ):
        """
        Initialize ImportDataSrcRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (required)

        :param data_src_name: 数据源名称
        :type data_src_name: str (required)

        :param bucket: 数据源的 BOS Bucket（当前只支持同地域的存储桶）
        :type bucket: str (required)

        :param other_account: 是否为其他账号的 bucket，若为true则需要提供导入 Bucket 带读写权限的AK/SK，默认 false
        :type other_account: bool (optional)

        :param bucket_ak: otherAccount 为 true 时必填，无需加密
        :type bucket_ak: str (optional)

        :param bucket_sk: bucket_sk parameter
        :type bucket_sk: str (optional)

        :param bucket_sts_token: otherAccount 为 true 时有效，无需加密
        :type bucket_sts_token: str (optional)

        :param dir_prefix: dir_prefix parameter
        :type dir_prefix: str (optional)

        :param keep_symlink: 是否保留 BOS 软链，保留软链会降低数据源导入效率，以及后续增量元数据同步效率，默认 false
        :type keep_symlink: bool (optional)

        :param auth_group_id: 权限组ID，默认权限组 ID 为 AG-RAPIDFS_DEFAULT_AUTHGROUP_ID
        :type auth_group_id: str (optional)

        :param description: 数据源描述信息
        :type description: str (optional)

        :param quota_mi_b: 该数据源的容量配额，表示该数据源的可用最大容量，不能超过实例的缓存总容量
        :type quota_mi_b: int (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.instance_id = instance_id
        self.data_src_name = data_src_name
        self.bucket = bucket
        self.other_account = other_account
        self.bucket_ak = bucket_ak
        self.bucket_sk = bucket_sk
        self.bucket_sts_token = bucket_sts_token
        self.dir_prefix = dir_prefix
        self.keep_symlink = keep_symlink
        self.auth_group_id = auth_group_id
        self.description = description
        self.quota_mi_b = quota_mi_b

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
        if self.data_src_name is not None:
            result['dataSrcName'] = self.data_src_name
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.other_account is not None:
            result['otherAccount'] = self.other_account
        if self.bucket_ak is not None:
            result['bucketAK'] = self.bucket_ak
        if self.bucket_sk is not None:
            result['bucketSK'] = self.bucket_sk
        if self.bucket_sts_token is not None:
            result['bucketStsToken'] = self.bucket_sts_token
        if self.dir_prefix is not None:
            result['dirPrefix'] = self.dir_prefix
        if self.keep_symlink is not None:
            result['keepSymlink'] = self.keep_symlink
        if self.auth_group_id is not None:
            result['authGroupId'] = self.auth_group_id
        if self.description is not None:
            result['description'] = self.description
        if self.quota_mi_b is not None:
            result['quotaMiB'] = self.quota_mi_b
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ImportDataSrcRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('dataSrcName') is not None:
            self.data_src_name = m.get('dataSrcName')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('otherAccount') is not None:
            self.other_account = m.get('otherAccount')
        if m.get('bucketAK') is not None:
            self.bucket_ak = m.get('bucketAK')
        if m.get('bucketSK') is not None:
            self.bucket_sk = m.get('bucketSK')
        if m.get('bucketStsToken') is not None:
            self.bucket_sts_token = m.get('bucketStsToken')
        if m.get('dirPrefix') is not None:
            self.dir_prefix = m.get('dirPrefix')
        if m.get('keepSymlink') is not None:
            self.keep_symlink = m.get('keepSymlink')
        if m.get('authGroupId') is not None:
            self.auth_group_id = m.get('authGroupId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('quotaMiB') is not None:
            self.quota_mi_b = m.get('quotaMiB')
        return self
