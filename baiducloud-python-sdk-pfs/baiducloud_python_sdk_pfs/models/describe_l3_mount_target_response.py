"""
Request entity for DescribeL3MountTargetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DescribeL3MountTargetResponse(BceResponse):
    """
    DescribeL3MountTargetResponse
    """

    def __init__(self, request_id=None, domain=None, mount_target_id=None, ovip=None, vpc_id=None, subnet_id=None):
        """
        Initialize DescribeL3MountTargetResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type request_id: str (optional)

        :param domain: 挂载地址
        :type domain: str (optional)

        :param mount_target_id: 挂载点ID
        :type mount_target_id: str (optional)

        :param ovip: 挂载点IP
        :type ovip: str (optional)

        :param vpc_id: 挂载点所在VPCID
        :type vpc_id: str (optional)

        :param subnet_id: 挂载点所在子网ID
        :type subnet_id: str (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.domain = domain
        self.mount_target_id = mount_target_id
        self.ovip = ovip
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.domain is not None:
            result['domain'] = self.domain
        if self.mount_target_id is not None:
            result['mountTargetId'] = self.mount_target_id
        if self.ovip is not None:
            result['ovip'] = self.ovip
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeL3MountTargetResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('mountTargetId') is not None:
            self.mount_target_id = m.get('mountTargetId')
        if m.get('ovip') is not None:
            self.ovip = m.get('ovip')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        return self
