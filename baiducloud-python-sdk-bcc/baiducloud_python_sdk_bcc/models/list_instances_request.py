"""
Request entity for ListInstancesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListInstancesRequest(AbstractModel):
    """
    Request entity for ListInstancesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        marker=None,
        max_keys=None,
        internal_ip=None,
        dedicated_host_id=None,
        zone_name=None,
        show_rdma_topo=None,
        instance_ids=None,
        instance_names=None,
        fuzzy_instance_name=None,
        volume_ids=None,
        deploy_set_ids=None,
        security_group_ids=None,
        payment_timing=None,
        status=None,
        tags=None,
        vpc_id=None,
        private_ips=None,
        ehc_cluster_id=None,
    ):
        """
        Initialize ListInstancesRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param internal_ip: internal_ip parameter
        :type internal_ip: str (optional)

        :param dedicated_host_id: dedicated_host_id parameter
        :type dedicated_host_id: str (optional)

        :param zone_name: zone_name parameter
        :type zone_name: str (optional)

        :param show_rdma_topo: show_rdma_topo parameter
        :type show_rdma_topo: str (optional)

        :param instance_ids: instance_ids parameter
        :type instance_ids: str (optional)

        :param instance_names: instance_names parameter
        :type instance_names: str (optional)

        :param fuzzy_instance_name: fuzzy_instance_name parameter
        :type fuzzy_instance_name: str (optional)

        :param volume_ids: volume_ids parameter
        :type volume_ids: str (optional)

        :param deploy_set_ids: deploy_set_ids parameter
        :type deploy_set_ids: str (optional)

        :param security_group_ids: security_group_ids parameter
        :type security_group_ids: str (optional)

        :param payment_timing: payment_timing parameter
        :type payment_timing: str (optional)

        :param status: status parameter
        :type status: str (optional)

        :param tags: tags parameter
        :type tags: str (optional)

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (optional)

        :param private_ips: private_ips parameter
        :type private_ips: str (optional)

        :param ehc_cluster_id: ehc_cluster_id parameter
        :type ehc_cluster_id: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.internal_ip = internal_ip
        self.dedicated_host_id = dedicated_host_id
        self.zone_name = zone_name
        self.show_rdma_topo = show_rdma_topo
        self.instance_ids = instance_ids
        self.instance_names = instance_names
        self.fuzzy_instance_name = fuzzy_instance_name
        self.volume_ids = volume_ids
        self.deploy_set_ids = deploy_set_ids
        self.security_group_ids = security_group_ids
        self.payment_timing = payment_timing
        self.status = status
        self.tags = tags
        self.vpc_id = vpc_id
        self.private_ips = private_ips
        self.ehc_cluster_id = ehc_cluster_id

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListInstancesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('internalIp') is not None:
            self.internal_ip = m.get('internalIp')
        if m.get('dedicatedHostId') is not None:
            self.dedicated_host_id = m.get('dedicatedHostId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('showRdmaTopo') is not None:
            self.show_rdma_topo = m.get('showRdmaTopo')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('instanceNames') is not None:
            self.instance_names = m.get('instanceNames')
        if m.get('fuzzyInstanceName') is not None:
            self.fuzzy_instance_name = m.get('fuzzyInstanceName')
        if m.get('volumeIds') is not None:
            self.volume_ids = m.get('volumeIds')
        if m.get('deploySetIds') is not None:
            self.deploy_set_ids = m.get('deploySetIds')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('privateIps') is not None:
            self.private_ips = m.get('privateIps')
        if m.get('ehcClusterId') is not None:
            self.ehc_cluster_id = m.get('ehcClusterId')
        return self
