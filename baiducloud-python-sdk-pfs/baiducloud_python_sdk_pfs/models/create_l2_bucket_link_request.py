"""
Request entity for CreateL2BucketLinkRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateL2BucketLinkRequest(AbstractModel):
    """
    Request entity for CreateL2BucketLinkRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        conflict_policy,
        bucket_name,
        bucket_prefix,
        throughput_limit_bytes,
        bucket_link_name,
        transfer_type,
        pfs_path,
        report_object_name=None,
        cron=None,
        bucket_belong_user_id=None,
        lcc_id=None,
        scope=None,
    ):
        """
        Initialize CreateL2BucketLinkRequest request entity.

        :param instance_id: PFS实例ID
        :type instance_id: str (required)

        :param conflict_policy: 冲突策略<br><li>1 覆盖策略<br><li>2 跳过策略<br><li>3 保留两者
        :type conflict_policy: str (required)

        :param bucket_name: 任务流动的BOS bucket name，最长长度64
        :type bucket_name: str (required)

        :param bucket_prefix: bucket_prefix parameter
        :type bucket_prefix: str (required)

        :param throughput_limit_bytes: throughput_limit_bytes parameter
        :type throughput_limit_bytes: str (required)

        :param report_object_name: 任务流动报告保存的object名字<br><li>最长长度978<br><li>路径不支持\".\" \"..\"
        :type report_object_name: str (optional)

        :param bucket_link_name: 任务流动名称，最长长度128，(中文64)
        :type bucket_link_name: str (required)

        :param transfer_type: 任务流动类型<br><li>0 导出任务(PFS -> BOS)<br><li>1 导入任务(BOS -> PFS)
        :type transfer_type: int (required)

        :param pfs_path: pfs_path parameter
        :type pfs_path: str (required)

        :param cron: cron parameter
        :type cron: str (optional)

        :param bucket_belong_user_id: 跨账号字段，标明跨账号的目标用户主账号userid
        :type bucket_belong_user_id: str (optional)

        :param lcc_id: 当跨账号启动时，如果bucket所属lcc专区，则需要额外标名对应的bucket所属的LccID信息
        :type lcc_id: str (optional)

        :param scope: 任务可见范围，1：主账号以及子账号全部可见，2：仅主账号和子账号可见
        :type scope: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.conflict_policy = conflict_policy
        self.bucket_name = bucket_name
        self.bucket_prefix = bucket_prefix
        self.throughput_limit_bytes = throughput_limit_bytes
        self.report_object_name = report_object_name
        self.bucket_link_name = bucket_link_name
        self.transfer_type = transfer_type
        self.pfs_path = pfs_path
        self.cron = cron
        self.bucket_belong_user_id = bucket_belong_user_id
        self.lcc_id = lcc_id
        self.scope = scope

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
        if self.conflict_policy is not None:
            result['conflictPolicy'] = self.conflict_policy
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.bucket_prefix is not None:
            result['bucketPrefix'] = self.bucket_prefix
        if self.throughput_limit_bytes is not None:
            result['throughputLimitBytes'] = self.throughput_limit_bytes
        if self.report_object_name is not None:
            result['reportObjectName'] = self.report_object_name
        if self.bucket_link_name is not None:
            result['bucketLinkName'] = self.bucket_link_name
        if self.transfer_type is not None:
            result['transferType'] = self.transfer_type
        if self.pfs_path is not None:
            result['pfsPath'] = self.pfs_path
        if self.cron is not None:
            result['cron'] = self.cron
        if self.bucket_belong_user_id is not None:
            result['bucketBelongUserId'] = self.bucket_belong_user_id
        if self.lcc_id is not None:
            result['lccId'] = self.lcc_id
        if self.scope is not None:
            result['scope'] = self.scope
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateL2BucketLinkRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('conflictPolicy') is not None:
            self.conflict_policy = m.get('conflictPolicy')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('bucketPrefix') is not None:
            self.bucket_prefix = m.get('bucketPrefix')
        if m.get('throughputLimitBytes') is not None:
            self.throughput_limit_bytes = m.get('throughputLimitBytes')
        if m.get('reportObjectName') is not None:
            self.report_object_name = m.get('reportObjectName')
        if m.get('bucketLinkName') is not None:
            self.bucket_link_name = m.get('bucketLinkName')
        if m.get('transferType') is not None:
            self.transfer_type = m.get('transferType')
        if m.get('pfsPath') is not None:
            self.pfs_path = m.get('pfsPath')
        if m.get('cron') is not None:
            self.cron = m.get('cron')
        if m.get('bucketBelongUserId') is not None:
            self.bucket_belong_user_id = m.get('bucketBelongUserId')
        if m.get('lccId') is not None:
            self.lcc_id = m.get('lccId')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        return self
