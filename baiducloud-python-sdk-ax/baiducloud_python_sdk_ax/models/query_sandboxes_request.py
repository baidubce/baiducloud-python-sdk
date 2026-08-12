"""
Request entity for QuerySandboxesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QuerySandboxesRequest(AbstractModel):
    """
    Request entity for QuerySandboxesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, limit=None, next_token=None, sandbox_ids=None, image_paths=None, metadata=None, state=None):
        """
        Initialize QuerySandboxesRequest request entity.

        :param limit: 单页返回数量，取值 1-100，默认 100。
        :type limit: int (optional)

        :param next_token: 上一页返回的游标，首次请求为空。
        :type next_token: str (optional)

        :param sandbox_ids: 沙箱实例 ID 列表，同组内 OR。
        :type sandbox_ids: List[str] (optional)

        :param image_paths: 实际镜像地址列表，同组内 OR。
        :type image_paths: List[str] (optional)

        :param metadata: metadata 键值过滤，条件之间 AND。
        :type metadata: Dict[str, str] (optional)

        :param state: 沙箱状态列表，可选 running、paused、killing、killed。
        :type state: List[str] (optional)
        """
        super().__init__()
        self.limit = limit
        self.next_token = next_token
        self.sandbox_ids = sandbox_ids
        self.image_paths = image_paths
        self.metadata = metadata
        self.state = state

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
        if self.limit is not None:
            result['limit'] = self.limit
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.sandbox_ids is not None:
            result['sandboxIds'] = self.sandbox_ids
        if self.image_paths is not None:
            result['imagePaths'] = self.image_paths
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QuerySandboxesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('sandboxIds') is not None:
            self.sandbox_ids = m.get('sandboxIds')
        if m.get('imagePaths') is not None:
            self.image_paths = m.get('imagePaths')
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self
