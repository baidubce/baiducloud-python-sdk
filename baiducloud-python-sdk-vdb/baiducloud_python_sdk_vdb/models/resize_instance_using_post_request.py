"""
Request entity for ResizeInstanceUsingPOSTRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vdb.models.milvus_component import MilvusComponent


class ResizeInstanceUsingPOSTRequest(AbstractModel):
    """
    Request entity for ResizeInstanceUsingPOSTRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        engine_type=None,
        components=None,
        data_node_num=None,
        disk_flavor=None,
        disk_type=None,
        env=None,
        instance_id=None,
        master_node_spec=None,
        master_num=None,
        node_spec=None,
        node_type=None,
        order_id=None,
        proxy_node_spec=None,
        proxy_num=None,
    ):
        """
        Initialize ResizeInstanceUsingPOSTRequest request entity.

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)

        :param components: components parameter
        :type components: List[MilvusComponent] (optional)

        :param data_node_num: data_node_num parameter
        :type data_node_num: int (optional)

        :param disk_flavor: disk_flavor parameter
        :type disk_flavor: int (optional)

        :param disk_type: disk_type parameter
        :type disk_type: str (optional)

        :param env: env parameter
        :type env: str (optional)

        :param instance_id: instance_id parameter
        :type instance_id: str (optional)

        :param master_node_spec: master_node_spec parameter
        :type master_node_spec: str (optional)

        :param master_num: master_num parameter
        :type master_num: int (optional)

        :param node_spec: node_spec parameter
        :type node_spec: str (optional)

        :param node_type: node_type parameter
        :type node_type: str (optional)

        :param order_id: order_id parameter
        :type order_id: str (optional)

        :param proxy_node_spec: proxy_node_spec parameter
        :type proxy_node_spec: str (optional)

        :param proxy_num: proxy_num parameter
        :type proxy_num: int (optional)
        """
        super().__init__()
        self.engine_type = engine_type
        self.components = components
        self.data_node_num = data_node_num
        self.disk_flavor = disk_flavor
        self.disk_type = disk_type
        self.env = env
        self.instance_id = instance_id
        self.master_node_spec = master_node_spec
        self.master_num = master_num
        self.node_spec = node_spec
        self.node_type = node_type
        self.order_id = order_id
        self.proxy_node_spec = proxy_node_spec
        self.proxy_num = proxy_num

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
        if self.components is not None:
            result['components'] = [i.to_dict() for i in self.components]
        if self.data_node_num is not None:
            result['dataNodeNum'] = self.data_node_num
        if self.disk_flavor is not None:
            result['diskFlavor'] = self.disk_flavor
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.env is not None:
            result['env'] = self.env
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.master_node_spec is not None:
            result['masterNodeSpec'] = self.master_node_spec
        if self.master_num is not None:
            result['masterNum'] = self.master_num
        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.proxy_node_spec is not None:
            result['proxyNodeSpec'] = self.proxy_node_spec
        if self.proxy_num is not None:
            result['proxyNum'] = self.proxy_num
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResizeInstanceUsingPOSTRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('components') is not None:
            self.components = [MilvusComponent().from_dict(i) for i in m.get('components')]
        if m.get('dataNodeNum') is not None:
            self.data_node_num = m.get('dataNodeNum')
        if m.get('diskFlavor') is not None:
            self.disk_flavor = m.get('diskFlavor')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('env') is not None:
            self.env = m.get('env')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('masterNodeSpec') is not None:
            self.master_node_spec = m.get('masterNodeSpec')
        if m.get('masterNum') is not None:
            self.master_num = m.get('masterNum')
        if m.get('nodeSpec') is not None:
            self.node_spec = m.get('nodeSpec')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('proxyNodeSpec') is not None:
            self.proxy_node_spec = m.get('proxyNodeSpec')
        if m.get('proxyNum') is not None:
            self.proxy_num = m.get('proxyNum')
        return self
