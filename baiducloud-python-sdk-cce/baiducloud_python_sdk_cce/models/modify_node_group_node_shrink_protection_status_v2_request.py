"""
Request entity for ModifyNodeGroupNodeShrinkProtectionStatusV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyNodeGroupNodeShrinkProtectionStatusV2Request(AbstractModel):
    """
    Request entity for ModifyNodeGroupNodeShrinkProtectionStatusV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cluster_id, instance_ids, scale_down_disabled):
        """
        Initialize ModifyNodeGroupNodeShrinkProtectionStatusV2Request request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param instance_ids: 需要修改缩容保护状态的节点 ID 列表（CCEInstanceID）
        :type instance_ids: List[str] (required)

        :param scale_down_disabled: 是否开启缩容保护：true 开启（禁止被缩容），false 关闭
        :type scale_down_disabled: bool (required)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.instance_ids = instance_ids
        self.scale_down_disabled = scale_down_disabled

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
        if self.instance_ids is not None:
            result['instanceIDs'] = self.instance_ids
        if self.scale_down_disabled is not None:
            result['scaleDownDisabled'] = self.scale_down_disabled
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyNodeGroupNodeShrinkProtectionStatusV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('instanceIDs') is not None:
            self.instance_ids = m.get('instanceIDs')
        if m.get('scaleDownDisabled') is not None:
            self.scale_down_disabled = m.get('scaleDownDisabled')
        return self
