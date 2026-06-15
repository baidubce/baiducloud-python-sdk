"""
VolumeModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.tag_model import TagModel

from baiducloud_python_sdk_bcc.models.group_info import GroupInfo

from baiducloud_python_sdk_bcc.models.auto_snapshot_policy_model import AutoSnapshotPolicyModel

from baiducloud_python_sdk_bcc.models.auto_snapshot_policy_info import AutoSnapshotPolicyInfo

from baiducloud_python_sdk_bcc.models.volume_attachment_model import VolumeAttachmentModel

from baiducloud_python_sdk_bcc.models.volume_multi_attach_info import VolumeMultiAttachInfo


class VolumeModel(AbstractModel):
    """
    VolumeModel
    """

    def __init__(
        self,
        id=None,
        disk_category=None,
        product_category=None,
        name=None,
        disk_size_in_gb=None,
        cds_extra_io=None,
        failure_status=None,
        create_time=None,
        expire_time=None,
        status=None,
        share_snapshot_id=None,
        enable_delete_protection=None,
        ebc_disk_size=None,
        enable_auto_renew=None,
        auto_renew_time=None,
        tags=None,
        type=None,
        storage_type=None,
        is_system_volume=None,
        description=None,
        desc=None,
        payment_timing=None,
        zone_name=None,
        region_id=None,
        source_snapshot_id=None,
        snapshot_num=None,
        cluster_id=None,
        res_group_infos=None,
        auto_snapshot_policy=None,
        auto_snapshot_policy_infos=None,
        encrypt_key=None,
        encrypt_key_spec=None,
        encrypted=None,
        delete_with_instance=None,
        delete_auto_snapshot=None,
        attachments=None,
        multi_attach_infos=None,
        multi_attach=None,
        volume_id=None,
    ):
        """
        Initialize VolumeModel instance.

        :param id: 磁盘ID（查询磁盘列表、查询磁盘详情返回）
        :type id: str (optional)

        :param disk_category: disk_category attribute
        :type disk_category: str (optional)

        :param product_category: 挂载的实例服务类别，可选值包含BCC/HPAS（查询磁盘列表、查询磁盘详情返回）
        :type product_category: str (optional)

        :param name: 磁盘名称（查询磁盘列表、查询磁盘详情返回）
        :type name: str (optional)

        :param disk_size_in_gb: 磁盘大小，单位是GB（查询磁盘列表、查询磁盘详情返回、查询实例列表、查询指定实例详情）
        :type disk_size_in_gb: int (optional)

        :param cds_extra_io: 额外性能（查询磁盘列表、查询磁盘详情返回）
        :type cds_extra_io: int (optional)

        :param failure_status: 失败状态信息（查询磁盘列表、查询磁盘详情返回）
        :type failure_status: str (optional)

        :param create_time: 创建日期，符合BCE日期规范（查询磁盘列表、查询磁盘详情返回）
        :type create_time: str (optional)

        :param expire_time: 过期时间（查询磁盘列表、查询磁盘详情返回）
        :type expire_time: str (optional)

        :param status: 磁盘状态（查询磁盘列表、查询磁盘详情返回）
        :type status: str (optional)

        :param share_snapshot_id: share_snapshot_id attribute
        :type share_snapshot_id: str (optional)

        :param enable_delete_protection: 是否开启磁盘释放保护（查询磁盘列表、查询磁盘详情返回）
        :type enable_delete_protection: bool (optional)

        :param ebc_disk_size: EBC磁盘大小（查询磁盘列表返回）
        :type ebc_disk_size: int (optional)

        :param enable_auto_renew: 是否自动续费（查询磁盘列表、查询磁盘详情返回）
        :type enable_auto_renew: bool (optional)

        :param auto_renew_time: 自动续费时间（查询磁盘列表、查询磁盘详情返回）
        :type auto_renew_time: int (optional)

        :param tags: 磁盘当前配置的标签（查询磁盘列表、查询磁盘详情返回）
        :type tags: List[TagModel] (optional)

        :param type: 磁盘类型（查询磁盘列表、查询磁盘详情返回）
        :type type: str (optional)

        :param storage_type: storage_type attribute
        :type storage_type: str (optional)

        :param is_system_volume: 是否为系统盘（查询磁盘列表、查询磁盘详情返回、查询实例列表、查询指定实例详情）
        :type is_system_volume: bool (optional)

        :param description: 描述信息（查询磁盘列表返回）
        :type description: str (optional)

        :param desc: 描述信息（查询磁盘详情返回）
        :type desc: str (optional)

        :param payment_timing: 付费方式，包括Postpaid(按量付费)，Prepaid(包年包月)两种。（查询磁盘列表、查询磁盘详情返回）
        :type payment_timing: str (optional)

        :param zone_name: 可用区信息（查询磁盘列表、查询磁盘详情返回）
        :type zone_name: str (optional)

        :param region_id: 所在region（查询磁盘详情返回）
        :type region_id: str (optional)

        :param source_snapshot_id: 创建磁盘所用的快照id（查询磁盘详情返回）
        :type source_snapshot_id: str (optional)

        :param snapshot_num: 磁盘当前具有的快照数量（查询磁盘详情返回）
        :type snapshot_num: str (optional)

        :param cluster_id: CDS专属集群ID（查询磁盘列表、查询磁盘详情返回）
        :type cluster_id: str (optional)

        :param res_group_infos: 磁盘当前绑定的资源组（查询磁盘详情返回）
        :type res_group_infos: List[GroupInfo] (optional)

        :param auto_snapshot_policy: auto_snapshot_policy attribute
        :type auto_snapshot_policy: AutoSnapshotPolicyModel (optional)

        :param auto_snapshot_policy_infos: 快照策略信息列表（查询磁盘详情返回）
        :type auto_snapshot_policy_infos: List[AutoSnapshotPolicyInfo] (optional)

        :param encrypt_key: 加密密钥（查询磁盘详情返回）
        :type encrypt_key: str (optional)

        :param encrypt_key_spec: 加密密钥规格（查询磁盘详情返回）
        :type encrypt_key_spec: str (optional)

        :param encrypted: 是否加密（查询磁盘列表、查询磁盘详情返回）
        :type encrypted: bool (optional)

        :param delete_with_instance: 磁盘随实例删除，仅后付费类型的数据盘返回（查询磁盘列表、查询磁盘详情返回）
        :type delete_with_instance: bool (optional)

        :param delete_auto_snapshot: 自动快照随磁盘删除，任何类型的磁盘都会返回（查询磁盘列表、查询磁盘详情返回）
        :type delete_auto_snapshot: bool (optional)

        :param attachments: 挂载设备信息列表，磁盘未挂载时该值为空。（查询磁盘列表、查询磁盘详情返回）
        :type attachments: List[VolumeAttachmentModel] (optional)

        :param multi_attach_infos: 多挂载信息列表（查询磁盘列表、查询磁盘详情返回）
        :type multi_attach_infos: List[VolumeMultiAttachInfo] (optional)

        :param multi_attach: 是否支持多挂载（查询指定实例详情）
        :type multi_attach: bool (optional)

        :param volume_id: 磁盘ID（查询实例列表、查询指定实例详情）
        :type volume_id: str (optional)
        """
        super().__init__()
        self.id = id
        self.disk_category = disk_category
        self.product_category = product_category
        self.name = name
        self.disk_size_in_gb = disk_size_in_gb
        self.cds_extra_io = cds_extra_io
        self.failure_status = failure_status
        self.create_time = create_time
        self.expire_time = expire_time
        self.status = status
        self.share_snapshot_id = share_snapshot_id
        self.enable_delete_protection = enable_delete_protection
        self.ebc_disk_size = ebc_disk_size
        self.enable_auto_renew = enable_auto_renew
        self.auto_renew_time = auto_renew_time
        self.tags = tags
        self.type = type
        self.storage_type = storage_type
        self.is_system_volume = is_system_volume
        self.description = description
        self.desc = desc
        self.payment_timing = payment_timing
        self.zone_name = zone_name
        self.region_id = region_id
        self.source_snapshot_id = source_snapshot_id
        self.snapshot_num = snapshot_num
        self.cluster_id = cluster_id
        self.res_group_infos = res_group_infos
        self.auto_snapshot_policy = auto_snapshot_policy
        self.auto_snapshot_policy_infos = auto_snapshot_policy_infos
        self.encrypt_key = encrypt_key
        self.encrypt_key_spec = encrypt_key_spec
        self.encrypted = encrypted
        self.delete_with_instance = delete_with_instance
        self.delete_auto_snapshot = delete_auto_snapshot
        self.attachments = attachments
        self.multi_attach_infos = multi_attach_infos
        self.multi_attach = multi_attach
        self.volume_id = volume_id

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
        if self.id is not None:
            result['id'] = self.id
        if self.disk_category is not None:
            result['diskCategory'] = self.disk_category
        if self.product_category is not None:
            result['productCategory'] = self.product_category
        if self.name is not None:
            result['name'] = self.name
        if self.disk_size_in_gb is not None:
            result['diskSizeInGB'] = self.disk_size_in_gb
        if self.cds_extra_io is not None:
            result['cdsExtraIo'] = self.cds_extra_io
        if self.failure_status is not None:
            result['failureStatus'] = self.failure_status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.status is not None:
            result['status'] = self.status
        if self.share_snapshot_id is not None:
            result['shareSnapshotId'] = self.share_snapshot_id
        if self.enable_delete_protection is not None:
            result['enableDeleteProtection'] = self.enable_delete_protection
        if self.ebc_disk_size is not None:
            result['ebcDiskSize'] = self.ebc_disk_size
        if self.enable_auto_renew is not None:
            result['enableAutoRenew'] = self.enable_auto_renew
        if self.auto_renew_time is not None:
            result['autoRenewTime'] = self.auto_renew_time
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.type is not None:
            result['type'] = self.type
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.is_system_volume is not None:
            result['isSystemVolume'] = self.is_system_volume
        if self.description is not None:
            result['description'] = self.description
        if self.desc is not None:
            result['desc'] = self.desc
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.source_snapshot_id is not None:
            result['sourceSnapshotId'] = self.source_snapshot_id
        if self.snapshot_num is not None:
            result['snapshotNum'] = self.snapshot_num
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.res_group_infos is not None:
            result['resGroupInfos'] = [i.to_dict() for i in self.res_group_infos]
        if self.auto_snapshot_policy is not None:
            result['autoSnapshotPolicy'] = self.auto_snapshot_policy.to_dict()
        if self.auto_snapshot_policy_infos is not None:
            result['autoSnapshotPolicyInfos'] = [i.to_dict() for i in self.auto_snapshot_policy_infos]
        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key
        if self.encrypt_key_spec is not None:
            result['encryptKeySpec'] = self.encrypt_key_spec
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.delete_with_instance is not None:
            result['deleteWithInstance'] = self.delete_with_instance
        if self.delete_auto_snapshot is not None:
            result['deleteAutoSnapshot'] = self.delete_auto_snapshot
        if self.attachments is not None:
            result['attachments'] = [i.to_dict() for i in self.attachments]
        if self.multi_attach_infos is not None:
            result['multiAttachInfos'] = [i.to_dict() for i in self.multi_attach_infos]
        if self.multi_attach is not None:
            result['multiAttach'] = self.multi_attach
        if self.volume_id is not None:
            result['volumeId'] = self.volume_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VolumeModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('diskCategory') is not None:
            self.disk_category = m.get('diskCategory')
        if m.get('productCategory') is not None:
            self.product_category = m.get('productCategory')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('diskSizeInGB') is not None:
            self.disk_size_in_gb = m.get('diskSizeInGB')
        if m.get('cdsExtraIo') is not None:
            self.cds_extra_io = m.get('cdsExtraIo')
        if m.get('failureStatus') is not None:
            self.failure_status = m.get('failureStatus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('shareSnapshotId') is not None:
            self.share_snapshot_id = m.get('shareSnapshotId')
        if m.get('enableDeleteProtection') is not None:
            self.enable_delete_protection = m.get('enableDeleteProtection')
        if m.get('ebcDiskSize') is not None:
            self.ebc_disk_size = m.get('ebcDiskSize')
        if m.get('enableAutoRenew') is not None:
            self.enable_auto_renew = m.get('enableAutoRenew')
        if m.get('autoRenewTime') is not None:
            self.auto_renew_time = m.get('autoRenewTime')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('isSystemVolume') is not None:
            self.is_system_volume = m.get('isSystemVolume')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sourceSnapshotId') is not None:
            self.source_snapshot_id = m.get('sourceSnapshotId')
        if m.get('snapshotNum') is not None:
            self.snapshot_num = m.get('snapshotNum')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('resGroupInfos') is not None:
            self.res_group_infos = [GroupInfo().from_dict(i) for i in m.get('resGroupInfos')]
        if m.get('autoSnapshotPolicy') is not None:
            self.auto_snapshot_policy = AutoSnapshotPolicyModel().from_dict(m.get('autoSnapshotPolicy'))
        if m.get('autoSnapshotPolicyInfos') is not None:
            self.auto_snapshot_policy_infos = [
                AutoSnapshotPolicyInfo().from_dict(i) for i in m.get('autoSnapshotPolicyInfos')
            ]
        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')
        if m.get('encryptKeySpec') is not None:
            self.encrypt_key_spec = m.get('encryptKeySpec')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('deleteWithInstance') is not None:
            self.delete_with_instance = m.get('deleteWithInstance')
        if m.get('deleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('deleteAutoSnapshot')
        if m.get('attachments') is not None:
            self.attachments = [VolumeAttachmentModel().from_dict(i) for i in m.get('attachments')]
        if m.get('multiAttachInfos') is not None:
            self.multi_attach_infos = [VolumeMultiAttachInfo().from_dict(i) for i in m.get('multiAttachInfos')]
        if m.get('multiAttach') is not None:
            self.multi_attach = m.get('multiAttach')
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        return self
