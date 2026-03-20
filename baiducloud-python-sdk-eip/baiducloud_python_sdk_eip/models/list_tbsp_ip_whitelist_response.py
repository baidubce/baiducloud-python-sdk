"""
Request entity for ListTbspIpWhitelistResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_eip.models.tbsp_ip_whitelist_model import TbspIpWhitelistModel


class ListTbspIpWhitelistResponse(BceResponse):
    """
    ListTbspIpWhitelistResponse
    """

    def __init__(self, ip_whitelist_list=None, marker=None, is_truncated=None, next_marker=None, max_keys=None):
        """
        Initialize ListTbspIpWhitelistResponse response.

        :param ip_whitelist_list: 包含查询结果的列表
        :type ip_whitelist_list: List[TbspIpWhitelistModel] (optional)

        :param marker: 标记查询的起始位置，若结果列表为空，此项不存在
        :type marker: str (optional)

        :param is_truncated: true表示后面还有数据，false表示已经是最后一页
        :type is_truncated: bool (optional)

        :param next_marker: 获取下一页所需要传递的marker值。当isTruncated为false时，该域不出现
        :type next_marker: str (optional)

        :param max_keys: 每页包含的最大数量
        :type max_keys: int (optional)
        """
        super().__init__()
        self.ip_whitelist_list = ip_whitelist_list
        self.marker = marker
        self.is_truncated = is_truncated
        self.next_marker = next_marker
        self.max_keys = max_keys

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
            result['metadata'] = self.metadata
        if self.ip_whitelist_list is not None:
            result['ipWhitelistList'] = [i.to_dict() for i in self.ip_whitelist_list]
        if self.marker is not None:
            result['marker'] = self.marker
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListTbspIpWhitelistResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ipWhitelistList') is not None:
            self.ip_whitelist_list = [TbspIpWhitelistModel().from_dict(i) for i in m.get('ipWhitelistList')]
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        return self
