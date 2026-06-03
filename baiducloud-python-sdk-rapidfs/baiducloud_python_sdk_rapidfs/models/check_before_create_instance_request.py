"""
Request entity for CheckBeforeCreateInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CheckBeforeCreateInstanceRequest(AbstractModel):
    """
    Request entity for CheckBeforeCreateInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        zone,
        vpc_id,
        subnet_id,
        managed_mode=None,
        meta_spec=None,
        data_spec=None,
        type=None,
        capacity_ti_b=None,
        cce_cluster_id=None,
        aihc_resource_pool_id=None,
        k8s_controller_id=None,
        k8s_controller_token=None,
    ):
        """
        Initialize CheckBeforeCreateInstanceRequest request entity.

        :param zone: 可用区，ZoneA，ZoneB ……
        :type zone: str (required)

        :param vpc_id: RapidFS 实例所在 vpc，短 ID
        :type vpc_id: str (required)

        :param subnet_id: RapidFS 实例所在子网，短 ID
        :type subnet_id: str (required)

        :param managed_mode: managed_mode parameter
        :type managed_mode: str (optional)

        :param meta_spec: meta_spec parameter
        :type meta_spec: str (optional)

        :param data_spec: data_spec parameter
        :type data_spec: str (optional)

        :param type: type parameter
        :type type: str (optional)

        :param capacity_ti_b: capacity_ti_b parameter
        :type capacity_ti_b: int (optional)

        :param cce_cluster_id: cce_cluster_id parameter
        :type cce_cluster_id: str (optional)

        :param aihc_resource_pool_id: aihc_resource_pool_id parameter
        :type aihc_resource_pool_id: str (optional)

        :param k8s_controller_id: k8s_controller_id parameter
        :type k8s_controller_id: str (optional)

        :param k8s_controller_token: k8s_controller_token parameter
        :type k8s_controller_token: str (optional)
        """
        super().__init__()
        self.zone = zone
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.managed_mode = managed_mode
        self.meta_spec = meta_spec
        self.data_spec = data_spec
        self.type = type
        self.capacity_ti_b = capacity_ti_b
        self.cce_cluster_id = cce_cluster_id
        self.aihc_resource_pool_id = aihc_resource_pool_id
        self.k8s_controller_id = k8s_controller_id
        self.k8s_controller_token = k8s_controller_token

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
        if self.zone is not None:
            result['zone'] = self.zone
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.managed_mode is not None:
            result['managedMode'] = self.managed_mode
        if self.meta_spec is not None:
            result['metaSpec'] = self.meta_spec
        if self.data_spec is not None:
            result['dataSpec'] = self.data_spec
        if self.type is not None:
            result['type'] = self.type
        if self.capacity_ti_b is not None:
            result['capacityTiB'] = self.capacity_ti_b
        if self.cce_cluster_id is not None:
            result['cceClusterId'] = self.cce_cluster_id
        if self.aihc_resource_pool_id is not None:
            result['aihcResourcePoolId'] = self.aihc_resource_pool_id
        if self.k8s_controller_id is not None:
            result['k8sControllerId'] = self.k8s_controller_id
        if self.k8s_controller_token is not None:
            result['k8sControllerToken'] = self.k8s_controller_token
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CheckBeforeCreateInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('managedMode') is not None:
            self.managed_mode = m.get('managedMode')
        if m.get('metaSpec') is not None:
            self.meta_spec = m.get('metaSpec')
        if m.get('dataSpec') is not None:
            self.data_spec = m.get('dataSpec')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('capacityTiB') is not None:
            self.capacity_ti_b = m.get('capacityTiB')
        if m.get('cceClusterId') is not None:
            self.cce_cluster_id = m.get('cceClusterId')
        if m.get('aihcResourcePoolId') is not None:
            self.aihc_resource_pool_id = m.get('aihcResourcePoolId')
        if m.get('k8sControllerId') is not None:
            self.k8s_controller_id = m.get('k8sControllerId')
        if m.get('k8sControllerToken') is not None:
            self.k8s_controller_token = m.get('k8sControllerToken')
        return self
