"""
Request entity for ChangeConfigurationRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.billing import Billing


class ChangeConfigurationRequest(AbstractModel):
    """
    Request entity for ChangeConfigurationRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, instance_id, client_token, billing, engine_version, node_type=None, shard_num=None, disk_flavor=None
    ):
        """
        Initialize ChangeConfigurationRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (required)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param engine_version: 引擎版本。例如redis 3.2/4.0/5.0/6.0 等
        :type engine_version: str (required)

        :param node_type: node_type parameter
        :type node_type: str (optional)

        :param shard_num: 分片个数
        :type shard_num: int (optional)

        :param disk_flavor: 存储空间
        :type disk_flavor: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.client_token = client_token
        self.billing = billing
        self.engine_version = engine_version
        self.node_type = node_type
        self.shard_num = shard_num
        self.disk_flavor = disk_flavor

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
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.shard_num is not None:
            result['shardNum'] = self.shard_num
        if self.disk_flavor is not None:
            result['diskFlavor'] = self.disk_flavor
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ChangeConfigurationRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('shardNum') is not None:
            self.shard_num = m.get('shardNum')
        if m.get('diskFlavor') is not None:
            self.disk_flavor = m.get('diskFlavor')
        return self
