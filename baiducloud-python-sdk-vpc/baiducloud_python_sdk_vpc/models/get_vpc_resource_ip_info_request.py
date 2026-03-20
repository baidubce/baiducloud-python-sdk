"""
Request entity for GetVpcResourceIpInfoRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetVpcResourceIpInfoRequest(AbstractModel):
    """
    Request entity for GetVpcResourceIpInfoRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpc_id, subnet_id=None, resource_type=None, page_no=None, page_size=None):
        """
        Initialize GetVpcResourceIpInfoRequest request entity.

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (required)

        :param subnet_id: subnet_id parameter
        :type subnet_id: str (optional)

        :param resource_type: resource_type parameter
        :type resource_type: str (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.resource_type = resource_type
        self.page_no = page_no
        self.page_size = page_size

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
        :rtype: GetVpcResourceIpInfoRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
