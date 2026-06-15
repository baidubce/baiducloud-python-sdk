"""
Request entity for CheckBeforeAddCacheNodesResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.err_info import ErrInfo


class CheckBeforeAddCacheNodesResponse(BceResponse):
    """
    CheckBeforeAddCacheNodesResponse
    """

    def __init__(self, rapidfs_pass=None, err_infos=None):
        """
        Initialize CheckBeforeAddCacheNodesResponse response.

        :param rapidfs_pass: 检查是否通过
        :type rapidfs_pass: bool (optional)

        :param err_infos: 错误列表，见附录 ErrInfo，pass 为 false 时返回
        :type err_infos: List[ErrInfo] (optional)
        """
        super().__init__()
        self.rapidfs_pass = rapidfs_pass
        self.err_infos = err_infos

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
        if self.rapidfs_pass is not None:
            result['pass'] = self.rapidfs_pass
        if self.err_infos is not None:
            result['errInfos'] = [i.to_dict() for i in self.err_infos]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CheckBeforeAddCacheNodesResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pass') is not None:
            self.rapidfs_pass = m.get('pass')
        if m.get('errInfos') is not None:
            self.err_infos = [ErrInfo().from_dict(i) for i in m.get('errInfos')]
        return self
