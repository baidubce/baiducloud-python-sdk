"""
RoGroup information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.instance_dict import InstanceDict

from baiducloud_python_sdk_rds.models.app_list import AppList

from baiducloud_python_sdk_rds.models.simple_vpc_vo import SimpleVpcVo

from baiducloud_python_sdk_rds.models.subnet_vo import SubnetVo

from baiducloud_python_sdk_rds.models.simple_vpc_vo import SimpleVpcVo


class RoGroup(AbstractModel):
    """
    RoGroup
    """

    def __init__(
        self,
        ro_group_id=None,
        ro_group_name=None,
        ro_group_endpoint=None,
        vpc_id=None,
        subnet_id=None,
        eip_status=None,
        ro_group_app_list=None,
        simple_vpc_vo=None,
        subnet_vo=None,
        vpc_vo=None,
    ):
        """
        Initialize RoGroup instance.

        :param ro_group_id: 节点ID。
        :type ro_group_id: str (optional)

        :param ro_group_name: 可用区名称，多个逗号分隔。
        :type ro_group_name: str (optional)

        :param ro_group_endpoint: ro_group_endpoint attribute
        :type ro_group_endpoint: InstanceDict (optional)

        :param vpc_id: vpcID。
        :type vpc_id: str (optional)

        :param subnet_id: VPC地址。
        :type subnet_id: str (optional)

        :param eip_status: eip_status attribute
        :type eip_status: str (optional)

        :param ro_group_app_list: 只读组列表。
        :type ro_group_app_list: List[AppList] (optional)

        :param simple_vpc_vo: simple_vpc_vo attribute
        :type simple_vpc_vo: SimpleVpcVo (optional)

        :param subnet_vo: subnet_vo attribute
        :type subnet_vo: SubnetVo (optional)

        :param vpc_vo: vpc_vo attribute
        :type vpc_vo: SimpleVpcVo (optional)
        """
        super().__init__()
        self.ro_group_id = ro_group_id
        self.ro_group_name = ro_group_name
        self.ro_group_endpoint = ro_group_endpoint
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.eip_status = eip_status
        self.ro_group_app_list = ro_group_app_list
        self.simple_vpc_vo = simple_vpc_vo
        self.subnet_vo = subnet_vo
        self.vpc_vo = vpc_vo

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
        if self.ro_group_id is not None:
            result['roGroupId'] = self.ro_group_id
        if self.ro_group_name is not None:
            result['roGroupName'] = self.ro_group_name
        if self.ro_group_endpoint is not None:
            result['roGroupEndpoint'] = self.ro_group_endpoint.to_dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.eip_status is not None:
            result['eipStatus'] = self.eip_status
        if self.ro_group_app_list is not None:
            result['roGroupAppList'] = [i.to_dict() for i in self.ro_group_app_list]
        if self.simple_vpc_vo is not None:
            result['SimpleVpcVo'] = self.simple_vpc_vo.to_dict()
        if self.subnet_vo is not None:
            result['subnetVo'] = self.subnet_vo.to_dict()
        if self.vpc_vo is not None:
            result['vpcVo'] = self.vpc_vo.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RoGroup

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('roGroupId') is not None:
            self.ro_group_id = m.get('roGroupId')
        if m.get('roGroupName') is not None:
            self.ro_group_name = m.get('roGroupName')
        if m.get('roGroupEndpoint') is not None:
            self.ro_group_endpoint = InstanceDict().from_dict(m.get('roGroupEndpoint'))
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('eipStatus') is not None:
            self.eip_status = m.get('eipStatus')
        if m.get('roGroupAppList') is not None:
            self.ro_group_app_list = [AppList().from_dict(i) for i in m.get('roGroupAppList')]
        if m.get('SimpleVpcVo') is not None:
            self.simple_vpc_vo = SimpleVpcVo().from_dict(m.get('SimpleVpcVo'))
        if m.get('subnetVo') is not None:
            self.subnet_vo = SubnetVo().from_dict(m.get('subnetVo'))
        if m.get('vpcVo') is not None:
            self.vpc_vo = SimpleVpcVo().from_dict(m.get('vpcVo'))
        return self
