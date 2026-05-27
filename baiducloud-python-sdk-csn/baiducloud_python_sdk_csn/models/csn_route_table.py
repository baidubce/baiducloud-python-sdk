"""
CsnRouteTable information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CsnRouteTable(AbstractModel):
    """
    CsnRouteTable
    """

    def __init__(self, csn_rt_id=None, name=None, description=None, type=None):
        """
        Initialize CsnRouteTable instance.

        :param csn_rt_id: 路由表ID
        :type csn_rt_id: str (optional)

        :param name: 路由表名称
        :type name: str (optional)

        :param description: 路由表描述信息
        :type description: str (optional)

        :param type: 路由表类型，取值 [ default \\| custom ]，分别表示默认路由表、自定义路由表
        :type type: str (optional)
        """
        super().__init__()
        self.csn_rt_id = csn_rt_id
        self.name = name
        self.description = description
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
        if self.csn_rt_id is not None:
            result['csnRtId'] = self.csn_rt_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
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
        :rtype: CsnRouteTable

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnRtId') is not None:
            self.csn_rt_id = m.get('csnRtId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
