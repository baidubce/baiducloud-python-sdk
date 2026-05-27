"""
CsnRtRule information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CsnRtRule(AbstractModel):
    """
    CsnRtRule
    """

    def __init__(
        self,
        rule_id=None,
        route_type=None,
        csn_id=None,
        csn_rt_id=None,
        description=None,
        from_attach_id=None,
        status=None,
        source_address=None,
        dest_address=None,
        next_hop_id=None,
        next_hop_name=None,
        next_hop_region=None,
        next_hop_type=None,
        as_path=None,
        community=None,
        black_hole=None,
    ):
        """
        Initialize CsnRtRule instance.

        :param rule_id: 路由条目的ID
        :type rule_id: str (optional)

        :param route_type: 路由条目的类型
        :type route_type: str (optional)

        :param csn_id: 云智能网的ID
        :type csn_id: str (optional)

        :param csn_rt_id: 路由表的ID
        :type csn_rt_id: str (optional)

        :param description: 路由条目的描述
        :type description: str (optional)

        :param from_attach_id: 路由条目来源网络实例在云智能网中的身份ID
        :type from_attach_id: str (optional)

        :param status: 路由条目的状态，取值 [ active \\| conflicted ]，分别表示可用、冲突
        :type status: str (optional)

        :param source_address: 源地址
        :type source_address: str (optional)

        :param dest_address: 目的地址
        :type dest_address: str (optional)

        :param next_hop_id: 下一跳网络实例的ID
        :type next_hop_id: str (optional)

        :param next_hop_name: 下一跳网络实例的名称
        :type next_hop_name: str (optional)

        :param next_hop_region: 下一跳网络实例的region信息
        :type next_hop_region: str (optional)

        :param next_hop_type: 下一跳网络实例的类型
        :type next_hop_type: str (optional)

        :param as_path: as-path
        :type as_path: str (optional)

        :param community: community
        :type community: str (optional)

        :param black_hole: 是否黑洞路由
        :type black_hole: bool (optional)
        """
        super().__init__()
        self.rule_id = rule_id
        self.route_type = route_type
        self.csn_id = csn_id
        self.csn_rt_id = csn_rt_id
        self.description = description
        self.from_attach_id = from_attach_id
        self.status = status
        self.source_address = source_address
        self.dest_address = dest_address
        self.next_hop_id = next_hop_id
        self.next_hop_name = next_hop_name
        self.next_hop_region = next_hop_region
        self.next_hop_type = next_hop_type
        self.as_path = as_path
        self.community = community
        self.black_hole = black_hole

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
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.csn_id is not None:
            result['csnId'] = self.csn_id
        if self.csn_rt_id is not None:
            result['csnRtId'] = self.csn_rt_id
        if self.description is not None:
            result['description'] = self.description
        if self.from_attach_id is not None:
            result['fromAttachId'] = self.from_attach_id
        if self.status is not None:
            result['status'] = self.status
        if self.source_address is not None:
            result['sourceAddress'] = self.source_address
        if self.dest_address is not None:
            result['destAddress'] = self.dest_address
        if self.next_hop_id is not None:
            result['nextHopId'] = self.next_hop_id
        if self.next_hop_name is not None:
            result['nextHopName'] = self.next_hop_name
        if self.next_hop_region is not None:
            result['nextHopRegion'] = self.next_hop_region
        if self.next_hop_type is not None:
            result['nextHopType'] = self.next_hop_type
        if self.as_path is not None:
            result['asPath'] = self.as_path
        if self.community is not None:
            result['community'] = self.community
        if self.black_hole is not None:
            result['blackHole'] = self.black_hole
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CsnRtRule

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('csnId') is not None:
            self.csn_id = m.get('csnId')
        if m.get('csnRtId') is not None:
            self.csn_rt_id = m.get('csnRtId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('fromAttachId') is not None:
            self.from_attach_id = m.get('fromAttachId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sourceAddress') is not None:
            self.source_address = m.get('sourceAddress')
        if m.get('destAddress') is not None:
            self.dest_address = m.get('destAddress')
        if m.get('nextHopId') is not None:
            self.next_hop_id = m.get('nextHopId')
        if m.get('nextHopName') is not None:
            self.next_hop_name = m.get('nextHopName')
        if m.get('nextHopRegion') is not None:
            self.next_hop_region = m.get('nextHopRegion')
        if m.get('nextHopType') is not None:
            self.next_hop_type = m.get('nextHopType')
        if m.get('asPath') is not None:
            self.as_path = m.get('asPath')
        if m.get('community') is not None:
            self.community = m.get('community')
        if m.get('blackHole') is not None:
            self.black_hole = m.get('blackHole')
        return self
