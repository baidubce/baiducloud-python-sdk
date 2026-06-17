"""
SnapshotModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.tag import Tag


class SnapshotModel(AbstractModel):
    """
    SnapshotModel
    """

    def __init__(
        self,
        id=None,
        name=None,
        size_in_gb=None,
        create_time=None,
        status=None,
        create_method=None,
        volume_id=None,
        desc=None,
        expire_time=None,
        insnap_id=None,
        package=None,
        template_id=None,
        encrypted=None,
        progress=None,
        tags=None,
    ):
        """
        Initialize SnapshotModel instance.

        :param id: 快照ID（查询快照列表、查询快照详情）
        :type id: str (optional)

        :param name: 快照名称（查询快照列表、查询快照详情）
        :type name: str (optional)

        :param size_in_gb: 快照大小，单位GB（查询快照列表、查询快照详情）
        :type size_in_gb: int (optional)

        :param create_time: 快照创建时间（查询快照列表、查询快照详情）
        :type create_time: str (optional)

        :param status: 快照状态（查询快照列表、查询快照详情）
        :type status: str (optional)

        :param create_method: 快照创建方式，取值：MANUAL/MIGRATION/auto（查询快照列表、查询快照详情）
        :type create_method: str (optional)

        :param volume_id: 快照所属磁盘ID（查询快照列表、查询快照详情）
        :type volume_id: str (optional)

        :param desc: 快照描述（查询快照列表、查询快照详情）
        :type desc: str (optional)

        :param expire_time: 快照过期时间（查询快照列表、查询快照详情）
        :type expire_time: str (optional)

        :param insnap_id: 内部快照ID（查询快照列表、查询快照详情）
        :type insnap_id: str (optional)

        :param package: 是否为大镜像快照（查询快照列表、查询快照详情）
        :type package: bool (optional)

        :param template_id: 关联的镜像ID（查询快照列表、查询快照详情）
        :type template_id: str (optional)

        :param encrypted: 快照是否加密（查询快照列表、查询快照详情）
        :type encrypted: bool (optional)

        :param progress: 快照进度（查询快照详情）
        :type progress: str (optional)

        :param tags: 标签列表（查询快照详情）
        :type tags: List[Tag] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.size_in_gb = size_in_gb
        self.create_time = create_time
        self.status = status
        self.create_method = create_method
        self.volume_id = volume_id
        self.desc = desc
        self.expire_time = expire_time
        self.insnap_id = insnap_id
        self.package = package
        self.template_id = template_id
        self.encrypted = encrypted
        self.progress = progress
        self.tags = tags

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
        if self.name is not None:
            result['name'] = self.name
        if self.size_in_gb is not None:
            result['sizeInGB'] = self.size_in_gb
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.status is not None:
            result['status'] = self.status
        if self.create_method is not None:
            result['createMethod'] = self.create_method
        if self.volume_id is not None:
            result['volumeId'] = self.volume_id
        if self.desc is not None:
            result['desc'] = self.desc
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.insnap_id is not None:
            result['insnapId'] = self.insnap_id
        if self.package is not None:
            result['package'] = self.package
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.progress is not None:
            result['progress'] = self.progress
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SnapshotModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sizeInGB') is not None:
            self.size_in_gb = m.get('sizeInGB')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createMethod') is not None:
            self.create_method = m.get('createMethod')
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('insnapId') is not None:
            self.insnap_id = m.get('insnapId')
        if m.get('package') is not None:
            self.package = m.get('package')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
