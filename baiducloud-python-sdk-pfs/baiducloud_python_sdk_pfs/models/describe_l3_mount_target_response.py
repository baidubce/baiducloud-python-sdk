"""
Request entity for DescribeL3MountTargetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DescribeL3MountTargetResponse(BceResponse):
    """
    DescribeL3MountTargetResponse
    """

    def __init__(
        self,
        request_id=None,
        domain=None,
        mount_target_id=None,
        ovip=None,
        vpc_id=None,
        subnet_id=None,
        name=None,
        protocol=None,
        access_group_name=None,
        client_count=None,
        admission_status=None,
    ):
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

        :param name: response body
        :type name: str (optional)

        :param protocol: 协议类型
        :type protocol: str (optional)

        :param access_group_name: 权限组名称
        :type access_group_name: str (optional)

        :param client_count: 挂载客户端数量
        :type client_count: int (optional)

        :param admission_status: 挂载点状态（0 启动；1 禁用）
        :type admission_status: int (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.domain = domain
        self.mount_target_id = mount_target_id
        self.ovip = ovip
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.name = name
        self.protocol = protocol
        self.access_group_name = access_group_name
        self.client_count = client_count
        self.admission_status = admission_status

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
        if self.name is not None:
            result['name'] = self.name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        if self.client_count is not None:
            result['clientCount'] = self.client_count
        if self.admission_status is not None:
            result['admissionStatus'] = self.admission_status
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
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('clientCount') is not None:
            self.client_count = m.get('clientCount')
        if m.get('admissionStatus') is not None:
            self.admission_status = m.get('admissionStatus')
        return self
