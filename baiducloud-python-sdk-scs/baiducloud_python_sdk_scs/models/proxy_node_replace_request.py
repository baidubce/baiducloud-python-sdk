"""
Request entity for ProxyNodeReplaceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ProxyNodeReplaceRequest(AbstractModel):
    """
    Request entity for ProxyNodeReplaceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, proxy_list, defer=None):
        """
        Initialize ProxyNodeReplaceRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param proxy_list: 待替换的代理节点列表。支持单选、批量选择。
        :type proxy_list: List[str] (required)

        :param defer: 是否维护时间内执行。`false` 表示立即执行；`true` 表示创建维护窗口任务。默认值为 `false`。
        :type defer: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.proxy_list = proxy_list
        self.defer = defer

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
        if self.proxy_list is not None:
            result['proxyList'] = self.proxy_list
        if self.defer is not None:
            result['defer'] = self.defer
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ProxyNodeReplaceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('proxyList') is not None:
            self.proxy_list = m.get('proxyList')
        if m.get('defer') is not None:
            self.defer = m.get('defer')
        return self
