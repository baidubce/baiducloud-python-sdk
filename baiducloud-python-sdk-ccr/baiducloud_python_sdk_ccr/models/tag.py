"""
Tag information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ccr.models.tag_scan_overview import TagScanOverview


class Tag(AbstractModel):
    """
    Tag
    """

    def __init__(
        self,
        architecture=None,
        author=None,
        digest=None,
        os=None,
        project_id=None,
        pull_time=None,
        push_time=None,
        repository_id=None,
        scan_overview=None,
        size=None,
        tag_name=None,
        type=None,
    ):
        """
        Initialize Tag instance.

        :param architecture: 镜像仓库（repository）架构
        :type architecture: str (optional)

        :param author: 发布者
        :type author: str (optional)

        :param digest: 制品 Hash 值
        :type digest: str (optional)

        :param os: 操作系统类型
        :type os: str (optional)

        :param project_id: 制品所属命名空间 ID
        :type project_id: int (optional)

        :param pull_time: Tag 最新拉取时间，格式为 `date-time`
        :type pull_time: str (optional)

        :param push_time: Tag 推送时间，格式为 `date-time`
        :type push_time: str (optional)

        :param repository_id: 制品所属镜像仓库 ID
        :type repository_id: int (optional)

        :param scan_overview: scan_overview attribute
        :type scan_overview: TagScanOverview (optional)

        :param size: 制品大小
        :type size: int (optional)

        :param tag_name: Tag 名称
        :type tag_name: str (optional)

        :param type: 制品类别，可选值：`image`、`chart`
        :type type: str (optional)
        """
        super().__init__()
        self.architecture = architecture
        self.author = author
        self.digest = digest
        self.os = os
        self.project_id = project_id
        self.pull_time = pull_time
        self.push_time = push_time
        self.repository_id = repository_id
        self.scan_overview = scan_overview
        self.size = size
        self.tag_name = tag_name
        self.type = type

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
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.author is not None:
            result['author'] = self.author
        if self.digest is not None:
            result['digest'] = self.digest
        if self.os is not None:
            result['os'] = self.os
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.pull_time is not None:
            result['pullTime'] = self.pull_time
        if self.push_time is not None:
            result['pushTime'] = self.push_time
        if self.repository_id is not None:
            result['repositoryId'] = self.repository_id
        if self.scan_overview is not None:
            result['scanOverview'] = self.scan_overview.to_dict()
        if self.size is not None:
            result['size'] = self.size
        if self.tag_name is not None:
            result['tagName'] = self.tag_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Tag

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('author') is not None:
            self.author = m.get('author')
        if m.get('digest') is not None:
            self.digest = m.get('digest')
        if m.get('os') is not None:
            self.os = m.get('os')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('pullTime') is not None:
            self.pull_time = m.get('pullTime')
        if m.get('pushTime') is not None:
            self.push_time = m.get('pushTime')
        if m.get('repositoryId') is not None:
            self.repository_id = m.get('repositoryId')
        if m.get('scanOverview') is not None:
            self.scan_overview = TagScanOverview().from_dict(m.get('scanOverview'))
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
