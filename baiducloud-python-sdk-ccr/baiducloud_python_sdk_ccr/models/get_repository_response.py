"""
Request entity for GetRepositoryResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetRepositoryResponse(BceResponse):
    """
    GetRepositoryResponse
    """

    def __init__(
        self,
        project_name=None,
        repository_name=None,
        description=None,
        repository_path=None,
        private_repository_path=None,
        tag_count=None,
        pull_count=None,
        creation_time=None,
        update_time=None,
    ):
        """
        Initialize GetRepositoryResponse response.

        :param project_name: 命名空间名称
        :type project_name: str (optional)

        :param repository_name: 镜像仓库名称
        :type repository_name: str (optional)

        :param description: 镜像仓库描述
        :type description: str (optional)

        :param repository_path: 公网访问镜像路径
        :type repository_path: str (optional)

        :param private_repository_path: vpc 内访问镜像路径
        :type private_repository_path: str (optional)

        :param tag_count: 镜像的Tag个数
        :type tag_count: int (optional)

        :param pull_count: 镜像拉取次数
        :type pull_count: int (optional)

        :param creation_time: 创建时间
        :type creation_time: str (optional)

        :param update_time: 更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.project_name = project_name
        self.repository_name = repository_name
        self.description = description
        self.repository_path = repository_path
        self.private_repository_path = private_repository_path
        self.tag_count = tag_count
        self.pull_count = pull_count
        self.creation_time = creation_time
        self.update_time = update_time

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.repository_name is not None:
            result['repositoryName'] = self.repository_name
        if self.description is not None:
            result['description'] = self.description
        if self.repository_path is not None:
            result['repositoryPath'] = self.repository_path
        if self.private_repository_path is not None:
            result['privateRepositoryPath'] = self.private_repository_path
        if self.tag_count is not None:
            result['tagCount'] = self.tag_count
        if self.pull_count is not None:
            result['pullCount'] = self.pull_count
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetRepositoryResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('repositoryName') is not None:
            self.repository_name = m.get('repositoryName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('repositoryPath') is not None:
            self.repository_path = m.get('repositoryPath')
        if m.get('privateRepositoryPath') is not None:
            self.private_repository_path = m.get('privateRepositoryPath')
        if m.get('tagCount') is not None:
            self.tag_count = m.get('tagCount')
        if m.get('pullCount') is not None:
            self.pull_count = m.get('pullCount')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
