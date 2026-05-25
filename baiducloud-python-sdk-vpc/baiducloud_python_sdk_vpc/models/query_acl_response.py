"""
Request entity for QueryAclResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.acl_entry import AclEntry


class QueryAclResponse(BceResponse):
    """
    QueryAclResponse
    """

    def __init__(self, vpc_id=None, vpc_name=None, vpc_cidr=None, acl_entrys=None):
        """
        Initialize QueryAclResponse response.

        :param vpc_id: VPC的ID
        :type vpc_id: str (optional)

        :param vpc_name: VPC的名称
        :type vpc_name: str (optional)

        :param vpc_cidr: VPC的CIDR
        :type vpc_cidr: str (optional)

        :param acl_entrys: ACL的Entry列表
        :type acl_entrys: List[AclEntry] (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.vpc_cidr = vpc_cidr
        self.acl_entrys = acl_entrys

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['vpcName'] = self.vpc_name
        if self.vpc_cidr is not None:
            result['vpcCidr'] = self.vpc_cidr
        if self.acl_entrys is not None:
            result['aclEntrys'] = [i.to_dict() for i in self.acl_entrys]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryAclResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcName') is not None:
            self.vpc_name = m.get('vpcName')
        if m.get('vpcCidr') is not None:
            self.vpc_cidr = m.get('vpcCidr')
        if m.get('aclEntrys') is not None:
            self.acl_entrys = [AclEntry().from_dict(i) for i in m.get('aclEntrys')]
        return self
