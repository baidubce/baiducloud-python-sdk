"""
Request entity for StartStopMysqlInstanceFlowLimitingTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class StartStopMysqlInstanceFlowLimitingTaskRequest(AbstractModel):
    """
    Request entity for StartStopMysqlInstanceFlowLimitingTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, filter_id, action, app_id, node_id):
        """
        Initialize StartStopMysqlInstanceFlowLimitingTaskRequest request entity.

        :param filter_id: 指定了限流规则ID
        :type filter_id: int (required)

        :param action: Action 指定操作类型：ON：开启SQL限流OFF：停止SQL限流
        :type action: str (required)

        :param app_id: 集群ID
        :type app_id: str (required)

        :param node_id: 节点ID
        :type node_id: str (required)
        """
        super().__init__()
        self.filter_id = filter_id
        self.action = action
        self.app_id = app_id
        self.node_id = node_id

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
        if self.filter_id is not None:
            result['filterId'] = self.filter_id
        if self.action is not None:
            result['action'] = self.action
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: StartStopMysqlInstanceFlowLimitingTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('filterId') is not None:
            self.filter_id = m.get('filterId')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        return self
