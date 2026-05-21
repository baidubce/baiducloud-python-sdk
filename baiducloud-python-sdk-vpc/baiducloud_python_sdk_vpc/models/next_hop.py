"""
NextHop information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class NextHop(AbstractModel):
    """
    NextHop
    """

    def __init__(self, nexthop_id=None, nexthop_type=None, path_type=None):
        """
        Initialize NextHop instance.

        :param nexthop_id: 下一跳ID
        :type nexthop_id: str (optional)

        :param nexthop_type: 路由类型。目前只支持专线网关类型：\"dcGateway\"
        :type nexthop_type: str (optional)

        :param path_type: 多线模式。负载均衡取值为ecmp；主备模式取值ha:active、ha:standby，分别表示主、备路由
        :type path_type: str (optional)
        """
        super().__init__()
        self.nexthop_id = nexthop_id
        self.nexthop_type = nexthop_type
        self.path_type = path_type

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
        if self.nexthop_id is not None:
            result['nexthopId'] = self.nexthop_id
        if self.nexthop_type is not None:
            result['nexthopType'] = self.nexthop_type
        if self.path_type is not None:
            result['pathType'] = self.path_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NextHop

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('nexthopId') is not None:
            self.nexthop_id = m.get('nexthopId')
        if m.get('nexthopType') is not None:
            self.nexthop_type = m.get('nexthopType')
        if m.get('pathType') is not None:
            self.path_type = m.get('pathType')
        return self
