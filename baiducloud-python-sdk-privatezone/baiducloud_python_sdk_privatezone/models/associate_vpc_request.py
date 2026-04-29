"""
Request entity for AssociateVpcRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AssociateVpcRequest(AbstractModel):
    """
    Request entity for AssociateVpcRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, zone_id, action, region, vpc_ids, client_token=None):
        """
        Initialize AssociateVpcRequest request entity.

        :param zone_id: zone_id parameter
        :type zone_id: str (required)

        :param action: action parameter
        :type action: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param region: 关联或者解关联的VPC所属的区域
        :type region: str (required)

        :param vpc_ids: 想要关联或者解关联的VPC的ID列表
        :type vpc_ids: List[str] (required)
        """
        super().__init__()
        self.zone_id = zone_id
        self.action = action
        self.client_token = client_token
        self.region = region
        self.vpc_ids = vpc_ids

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
        if self.region is not None:
            result['region'] = self.region
        if self.vpc_ids is not None:
            result['vpcIds'] = self.vpc_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AssociateVpcRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('vpcIds') is not None:
            self.vpc_ids = m.get('vpcIds')
        return self
