"""
Request entity for CreateVolumeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.tag_model import TagModel
from baiducloud_python_sdk_bcc.models.billing import Billing
from baiducloud_python_sdk_bcc.models.auto_snapshot_policy_model import AutoSnapshotPolicyModel


class CreateVolumeRequest(AbstractModel):
    """
    Request entity for CreateVolumeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        billing,
        zone_name=None,
        storage_type=None,
        cds_size_in_gb=None,
        cds_extra_io=None,
        snapshot_id=None,
        share_snapshot_id=None,
        enable_delete_protection=None,
        instance_id=None,
        encrypt_key=None,
        name=None,
        description=None,
        renew_time_unit=None,
        renew_time=None,
        relation_tag=None,
        tags=None,
        res_group_id=None,
        cluster_id=None,
        charge_type=None,
        auto_snapshot_policy=None,
        delete_with_instance=None,
        delete_auto_snapshot=None,
        purchase_count=None,
    ):
        """
        Initialize CreateVolumeRequest request entity.

        :param zone_name: 指定可用区信息，默认为空，由系统自动选择。
        :type zone_name: str (optional)

        :param storage_type: storage_type parameter
        :type storage_type: str (optional)

        :param cds_size_in_gb: 增强型SSD_PL1、增强型SSD_PL2、增强型SSD_PL3，支持购买额外IO性能
        :type cds_size_in_gb: int (optional)

        :param cds_extra_io: 磁盘的额外IO性能配置
        :type cds_extra_io: int (optional)

        :param snapshot_id: 快照ID，支持从快照创建磁盘。当此参数存在时且不为空时，cdsSizeInGB参数将被忽略，此时非必需。
        :type snapshot_id: str (optional)

        :param share_snapshot_id: 共享快照ID，支持从共享快照创建磁盘。当此参数存在时且不为空时，cdsSizeInGB参数将被忽略，此时非必需。
        :type share_snapshot_id: str (optional)

        :param enable_delete_protection: 是否开启磁盘释放保护
        :type enable_delete_protection: str (optional)

        :param instance_id: instance_id parameter
        :type instance_id: str (optional)

        :param encrypt_key: KMS密钥ID。
        :type encrypt_key: str (optional)

        :param name: 磁盘新的名称，自定义镜像名称，支持大小写字母、数字、中文以及-_ /.特殊字符，必须以字母开头，长度1-65。
        :type name: str (optional)

        :param description: description parameter
        :type description: str (optional)

        :param renew_time_unit: renew_time_unit parameter
        :type renew_time_unit: str (optional)

        :param renew_time: renew_time parameter
        :type renew_time: int (optional)

        :param relation_tag: 待创建CDS指定的标签是否需要和已有标签键进行关联，默认为false。注意值为true时要保证该标签键已存在
        :type relation_tag: bool (optional)

        :param tags: 待绑定的标签列表
        :type tags: List[TagModel] (optional)

        :param res_group_id: 资源组ID
        :type res_group_id: str (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param cluster_id: CDS专属集群ID
        :type cluster_id: str (optional)

        :param charge_type: charge_type parameter
        :type charge_type: str (optional)

        :param auto_snapshot_policy: auto_snapshot_policy parameter
        :type auto_snapshot_policy: AutoSnapshotPolicyModel (optional)

        :param delete_with_instance: delete_with_instance parameter
        :type delete_with_instance: bool (optional)

        :param delete_auto_snapshot: 是否删除已有的自动快照
        :type delete_auto_snapshot: bool (optional)

        :param purchase_count: 批量创建的CDS磁盘的个数，必须为大于0的整数，单次创建不能超过5个。可选参数，缺省为1
        :type purchase_count: int (optional)
        """
        super().__init__()
        self.zone_name = zone_name
        self.storage_type = storage_type
        self.cds_size_in_gb = cds_size_in_gb
        self.cds_extra_io = cds_extra_io
        self.snapshot_id = snapshot_id
        self.share_snapshot_id = share_snapshot_id
        self.enable_delete_protection = enable_delete_protection
        self.instance_id = instance_id
        self.encrypt_key = encrypt_key
        self.name = name
        self.description = description
        self.renew_time_unit = renew_time_unit
        self.renew_time = renew_time
        self.relation_tag = relation_tag
        self.tags = tags
        self.res_group_id = res_group_id
        self.billing = billing
        self.cluster_id = cluster_id
        self.charge_type = charge_type
        self.auto_snapshot_policy = auto_snapshot_policy
        self.delete_with_instance = delete_with_instance
        self.delete_auto_snapshot = delete_auto_snapshot
        self.purchase_count = purchase_count

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
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.cds_size_in_gb is not None:
            result['cdsSizeInGB'] = self.cds_size_in_gb
        if self.cds_extra_io is not None:
            result['cdsExtraIo'] = self.cds_extra_io
        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id
        if self.share_snapshot_id is not None:
            result['shareSnapshotId'] = self.share_snapshot_id
        if self.enable_delete_protection is not None:
            result['enableDeleteProtection'] = self.enable_delete_protection
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.renew_time_unit is not None:
            result['renewTimeUnit'] = self.renew_time_unit
        if self.renew_time is not None:
            result['renewTime'] = self.renew_time
        if self.relation_tag is not None:
            result['relationTag'] = self.relation_tag
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.res_group_id is not None:
            result['resGroupId'] = self.res_group_id
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.auto_snapshot_policy is not None:
            result['autoSnapshotPolicy'] = self.auto_snapshot_policy.to_dict()
        if self.delete_with_instance is not None:
            result['deleteWithInstance'] = self.delete_with_instance
        if self.delete_auto_snapshot is not None:
            result['deleteAutoSnapshot'] = self.delete_auto_snapshot
        if self.purchase_count is not None:
            result['purchaseCount'] = self.purchase_count
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateVolumeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('cdsSizeInGB') is not None:
            self.cds_size_in_gb = m.get('cdsSizeInGB')
        if m.get('cdsExtraIo') is not None:
            self.cds_extra_io = m.get('cdsExtraIo')
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        if m.get('shareSnapshotId') is not None:
            self.share_snapshot_id = m.get('shareSnapshotId')
        if m.get('enableDeleteProtection') is not None:
            self.enable_delete_protection = m.get('enableDeleteProtection')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('renewTimeUnit') is not None:
            self.renew_time_unit = m.get('renewTimeUnit')
        if m.get('renewTime') is not None:
            self.renew_time = m.get('renewTime')
        if m.get('relationTag') is not None:
            self.relation_tag = m.get('relationTag')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('resGroupId') is not None:
            self.res_group_id = m.get('resGroupId')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('autoSnapshotPolicy') is not None:
            self.auto_snapshot_policy = AutoSnapshotPolicyModel().from_dict(m.get('autoSnapshotPolicy'))
        if m.get('deleteWithInstance') is not None:
            self.delete_with_instance = m.get('deleteWithInstance')
        if m.get('deleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('deleteAutoSnapshot')
        if m.get('purchaseCount') is not None:
            self.purchase_count = m.get('purchaseCount')
        return self
