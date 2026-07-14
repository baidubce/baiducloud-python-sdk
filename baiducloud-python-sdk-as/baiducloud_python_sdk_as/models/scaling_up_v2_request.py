"""
Request entity for ScalingUpV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ScalingUpV2Request(AbstractModel):
    """
    Request entity for ScalingUpV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, scaling_up, zone, node_count=None, expansion_strategy=None):
        """
        Initialize ScalingUpV2Request request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param scaling_up: scaling_up parameter
        :type scaling_up: str (required)

        :param node_count: 节点数量
        :type node_count: int (optional)

        :param zone: 区域信息
        :type zone: List[str] (required)

        :param expansion_strategy: 扩容策略 ( Priority - 以单独可用区进行创建 ; Balanced - 在选定可用区中均衡创建)
        :type expansion_strategy: str (optional)
        """
        super().__init__()
        self.group_id = group_id
        self.scaling_up = scaling_up
        self.node_count = node_count
        self.zone = zone
        self.expansion_strategy = expansion_strategy

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
        if self.node_count is not None:
            result['nodeCount'] = self.node_count
        if self.zone is not None:
            result['zone'] = self.zone
        if self.expansion_strategy is not None:
            result['expansionStrategy'] = self.expansion_strategy
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ScalingUpV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('scalingUp') is not None:
            self.scaling_up = m.get('scalingUp')
        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('expansionStrategy') is not None:
            self.expansion_strategy = m.get('expansionStrategy')
        return self
