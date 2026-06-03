"""
Project information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Project(AbstractModel):
    """
    Project
    """

    def __init__(
        self,
        auto_scan=None,
        chart_count=None,
        creation_time=None,
        project_id=None,
        project_name=None,
        public=None,
        repo_count=None,
        update_time=None,
    ):
        """
        Initialize Project instance.

        :param auto_scan: 推送时是否自动扫描镜像，有效值为 `true`、`false`
        :type auto_scan: str (optional)

        :param chart_count: 命名空间下的 Chart 数量
        :type chart_count: int (optional)

        :param creation_time: 命名空间创建时间，格式为 `date-time`
        :type creation_time: str (optional)

        :param project_id: 命名空间 ID
        :type project_id: int (optional)

        :param project_name: 命名空间名称
        :type project_name: str (optional)

        :param public: 命名空间类型，有两种类型：`true` 表示公有，`false` 表示私有
        :type public: str (optional)

        :param repo_count: 命名空间下镜像仓库数量
        :type repo_count: int (optional)

        :param update_time: 命名空间更新时间，格式为 `date-time`
        :type update_time: str (optional)
        """
        super().__init__()
        self.auto_scan = auto_scan
        self.chart_count = chart_count
        self.creation_time = creation_time
        self.project_id = project_id
        self.project_name = project_name
        self.public = public
        self.repo_count = repo_count
        self.update_time = update_time

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
        if self.auto_scan is not None:
            result['autoScan'] = self.auto_scan
        if self.chart_count is not None:
            result['chartCount'] = self.chart_count
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.public is not None:
            result['public'] = self.public
        if self.repo_count is not None:
            result['repoCount'] = self.repo_count
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Project

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('autoScan') is not None:
            self.auto_scan = m.get('autoScan')
        if m.get('chartCount') is not None:
            self.chart_count = m.get('chartCount')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('repoCount') is not None:
            self.repo_count = m.get('repoCount')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
