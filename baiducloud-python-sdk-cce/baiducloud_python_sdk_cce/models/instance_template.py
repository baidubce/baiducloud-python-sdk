"""
InstanceTemplate information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceTemplate(AbstractModel):
    """
    InstanceTemplate
    """

    def __init__(
        self,
        machine_type=None,
        instance_type=None,
        instance_name=None,
        vpc_config=None,
        instance_resource=None,
        check_gpu_driver=None,
        image_id=None,
        user_data=None,
        instance_os=None,
        scale_down_disabled=None,
        is_open_hostname_domain=None,
        need_eip=None,
        eip_option=None,
        iam_role=None,
        deploy_custom_config=None,
        runtime_type=None,
        runtime_version=None,
        deploy_set_ids=None,
        labels=None,
        annotations=None,
        tags=None,
        taints=None,
        relation_tag=None,
        instance_pre_charging_option=None,
    ):
        """
        Initialize InstanceTemplate instance.

        :param machine_type:
        :type machine_type: str (optional)

        :param instance_type:
        :type instance_type: str (optional)

        :param instance_name:
        :type instance_name: str (optional)

        :param vpc_config:
        :type vpc_config: object (optional)

        :param instance_resource:
        :type instance_resource: object (optional)

        :param check_gpu_driver:
        :type check_gpu_driver: bool (optional)

        :param image_id:
        :type image_id: str (optional)

        :param user_data:
        :type user_data: object (optional)

        :param instance_os:
        :type instance_os: object (optional)

        :param scale_down_disabled:
        :type scale_down_disabled: bool (optional)

        :param is_open_hostname_domain:
        :type is_open_hostname_domain: bool (optional)

        :param need_eip:
        :type need_eip: bool (optional)

        :param eip_option:
        :type eip_option: object (optional)

        :param iam_role:
        :type iam_role: object (optional)

        :param deploy_custom_config:
        :type deploy_custom_config: object (optional)

        :param runtime_type:
        :type runtime_type: str (optional)

        :param runtime_version:
        :type runtime_version: str (optional)

        :param deploy_set_ids:
        :type deploy_set_ids: List[str] (optional)

        :param labels:
        :type labels: Dict[str, str] (optional)

        :param annotations:
        :type annotations: Dict[str, str] (optional)

        :param tags:
        :type tags: List[str] (optional)

        :param taints:
        :type taints: List[str] (optional)

        :param relation_tag:
        :type relation_tag: bool (optional)

        :param instance_pre_charging_option:
        :type instance_pre_charging_option: object (optional)
        """
        super().__init__()
        self.machine_type = machine_type
        self.instance_type = instance_type
        self.instance_name = instance_name
        self.vpc_config = vpc_config
        self.instance_resource = instance_resource
        self.check_gpu_driver = check_gpu_driver
        self.image_id = image_id
        self.user_data = user_data
        self.instance_os = instance_os
        self.scale_down_disabled = scale_down_disabled
        self.is_open_hostname_domain = is_open_hostname_domain
        self.need_eip = need_eip
        self.eip_option = eip_option
        self.iam_role = iam_role
        self.deploy_custom_config = deploy_custom_config
        self.runtime_type = runtime_type
        self.runtime_version = runtime_version
        self.deploy_set_ids = deploy_set_ids
        self.labels = labels
        self.annotations = annotations
        self.tags = tags
        self.taints = taints
        self.relation_tag = relation_tag
        self.instance_pre_charging_option = instance_pre_charging_option

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
        if self.machine_type is not None:
            result['machineType'] = self.machine_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.vpc_config is not None:
            result['vpcConfig'] = self.vpc_config
        if self.instance_resource is not None:
            result['instanceResource'] = self.instance_resource
        if self.check_gpu_driver is not None:
            result['checkGPUDriver'] = self.check_gpu_driver
        if self.image_id is not None:
            result['imageID'] = self.image_id
        if self.user_data is not None:
            result['userData'] = self.user_data
        if self.instance_os is not None:
            result['instanceOS'] = self.instance_os
        if self.scale_down_disabled is not None:
            result['scaleDownDisabled'] = self.scale_down_disabled
        if self.is_open_hostname_domain is not None:
            result['isOpenHostnameDomain'] = self.is_open_hostname_domain
        if self.need_eip is not None:
            result['needEIP'] = self.need_eip
        if self.eip_option is not None:
            result['eipOption'] = self.eip_option
        if self.iam_role is not None:
            result['iamRole'] = self.iam_role
        if self.deploy_custom_config is not None:
            result['deployCustomConfig'] = self.deploy_custom_config
        if self.runtime_type is not None:
            result['runtimeType'] = self.runtime_type
        if self.runtime_version is not None:
            result['runtimeVersion'] = self.runtime_version
        if self.deploy_set_ids is not None:
            result['deploySetIDs'] = self.deploy_set_ids
        if self.labels is not None:
            result['labels'] = self.labels
        if self.annotations is not None:
            result['annotations'] = self.annotations
        if self.tags is not None:
            result['tags'] = self.tags
        if self.taints is not None:
            result['taints'] = self.taints
        if self.relation_tag is not None:
            result['relationTag'] = self.relation_tag
        if self.instance_pre_charging_option is not None:
            result['instancePreChargingOption'] = self.instance_pre_charging_option
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceTemplate

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('machineType') is not None:
            self.machine_type = m.get('machineType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('vpcConfig') is not None:
            self.vpc_config = m.get('vpcConfig')
        if m.get('instanceResource') is not None:
            self.instance_resource = m.get('instanceResource')
        if m.get('checkGPUDriver') is not None:
            self.check_gpu_driver = m.get('checkGPUDriver')
        if m.get('imageID') is not None:
            self.image_id = m.get('imageID')
        if m.get('userData') is not None:
            self.user_data = m.get('userData')
        if m.get('instanceOS') is not None:
            self.instance_os = m.get('instanceOS')
        if m.get('scaleDownDisabled') is not None:
            self.scale_down_disabled = m.get('scaleDownDisabled')
        if m.get('isOpenHostnameDomain') is not None:
            self.is_open_hostname_domain = m.get('isOpenHostnameDomain')
        if m.get('needEIP') is not None:
            self.need_eip = m.get('needEIP')
        if m.get('eipOption') is not None:
            self.eip_option = m.get('eipOption')
        if m.get('iamRole') is not None:
            self.iam_role = m.get('iamRole')
        if m.get('deployCustomConfig') is not None:
            self.deploy_custom_config = m.get('deployCustomConfig')
        if m.get('runtimeType') is not None:
            self.runtime_type = m.get('runtimeType')
        if m.get('runtimeVersion') is not None:
            self.runtime_version = m.get('runtimeVersion')
        if m.get('deploySetIDs') is not None:
            self.deploy_set_ids = m.get('deploySetIDs')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('annotations') is not None:
            self.annotations = m.get('annotations')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('taints') is not None:
            self.taints = m.get('taints')
        if m.get('relationTag') is not None:
            self.relation_tag = m.get('relationTag')
        if m.get('instancePreChargingOption') is not None:
            self.instance_pre_charging_option = m.get('instancePreChargingOption')
        return self
