"""
CreateCdsModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateCdsModel(AbstractModel):
    """
    CreateCdsModel
    """

    def __init__(
        self,
        storage_type=None,
        cds_size_in_gb=None,
        cds_num=None,
        cds_extra_io=None,
        snapshot_id=None,
        encrypt_key=None,
        enable_delete_protection=None,
        delete_with_instance=None,
        delete_auto_snapshot=None,
        name=None,
    ):
        """
        Initialize CreateCdsModel instance.

        :param storage_type: CDS磁盘存储类型，默认是hp1(高性能云磁盘)。（创建实例、创建抢占实例、查询抢占实例市场价）
        :type storage_type: str (optional)

        :param cds_size_in_gb: CDS磁盘容量，必须为大于0的整数，单位为GB，大小为0~5120G（创建实例、创建抢占实例、查询抢占实例市场价）
        :type cds_size_in_gb: int (optional)

        :param cds_num: 磁盘数量（创建实例）
        :type cds_num: int (optional)

        :param cds_extra_io: 额外 IO 性能（创建实例）
        :type cds_extra_io: int (optional)

        :param snapshot_id: 快照ID，当通过快照创建磁盘时，此属性有效，不能小于快照大小（创建实例、创建抢占实例、查询抢占实例市场价）
        :type snapshot_id: str (optional)

        :param encrypt_key: 加密密钥（创建实例）
        :type encrypt_key: str (optional)

        :param enable_delete_protection: 磁盘删除保护（创建实例）
        :type enable_delete_protection: str (optional)

        :param delete_with_instance: delete_with_instance attribute
        :type delete_with_instance: bool (optional)

        :param delete_auto_snapshot: 释放时是否删除自动快照（创建实例）
        :type delete_auto_snapshot: bool (optional)

        :param name: 磁盘名称（创建实例）
        :type name: str (optional)
        """
        super().__init__()
        self.storage_type = storage_type
        self.cds_size_in_gb = cds_size_in_gb
        self.cds_num = cds_num
        self.cds_extra_io = cds_extra_io
        self.snapshot_id = snapshot_id
        self.encrypt_key = encrypt_key
        self.enable_delete_protection = enable_delete_protection
        self.delete_with_instance = delete_with_instance
        self.delete_auto_snapshot = delete_auto_snapshot
        self.name = name

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
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.cds_size_in_gb is not None:
            result['cdsSizeInGB'] = self.cds_size_in_gb
        if self.cds_num is not None:
            result['cdsNum'] = self.cds_num
        if self.cds_extra_io is not None:
            result['cdsExtraIo'] = self.cds_extra_io
        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id
        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key
        if self.enable_delete_protection is not None:
            result['enableDeleteProtection'] = self.enable_delete_protection
        if self.delete_with_instance is not None:
            result['deleteWithInstance'] = self.delete_with_instance
        if self.delete_auto_snapshot is not None:
            result['deleteAutoSnapshot'] = self.delete_auto_snapshot
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateCdsModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('cdsSizeInGB') is not None:
            self.cds_size_in_gb = m.get('cdsSizeInGB')
        if m.get('cdsNum') is not None:
            self.cds_num = m.get('cdsNum')
        if m.get('cdsExtraIo') is not None:
            self.cds_extra_io = m.get('cdsExtraIo')
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')
        if m.get('enableDeleteProtection') is not None:
            self.enable_delete_protection = m.get('enableDeleteProtection')
        if m.get('deleteWithInstance') is not None:
            self.delete_with_instance = m.get('deleteWithInstance')
        if m.get('deleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('deleteAutoSnapshot')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
