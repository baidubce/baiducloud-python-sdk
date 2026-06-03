"""
Request entity for DeleteVpcLinkRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteVpcLinkRequest(AbstractModel):
    """
    Request entity for DeleteVpcLinkRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, vpc_id, subnet_id):
        """
        Initialize DeleteVpcLinkRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param vpc_id: 私有网络ID
        :type vpc_id: str (required)

        :param subnet_id: 私有网络子网ID
        :type subnet_id: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id

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
        if self.vpc_id is not None:
            result['vpcID'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetID'] = self.subnet_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteVpcLinkRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('vpcID') is not None:
            self.vpc_id = m.get('vpcID')
        if m.get('subnetID') is not None:
            self.subnet_id = m.get('subnetID')
        return self
