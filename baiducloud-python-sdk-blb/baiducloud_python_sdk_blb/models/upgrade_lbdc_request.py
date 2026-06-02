"""
Request entity for UpgradeLbdcRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpgradeLbdcRequest(AbstractModel):
    """
    Request entity for UpgradeLbdcRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, ccu_count, client_token=None):
        """
        Initialize UpgradeLbdcRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param ccu_count: 集群性能容量单位CCU（Cluster Capacity Unit）是用来衡量BLB集群处理流量时涉及的各个指标。
        :type ccu_count: int (required)
        """
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.ccu_count = ccu_count

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
        if self.ccu_count is not None:
            result['ccuCount'] = self.ccu_count
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpgradeLbdcRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('ccuCount') is not None:
            self.ccu_count = m.get('ccuCount')
        return self
