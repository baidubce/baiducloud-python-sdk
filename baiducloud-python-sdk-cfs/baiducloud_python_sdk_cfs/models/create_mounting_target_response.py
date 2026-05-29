"""
Request entity for CreateMountingTargetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateMountingTargetResponse(BceResponse):
    """
    CreateMountingTargetResponse
    """

    def __init__(self, domain=None, mount_id=None):
        """
        Initialize CreateMountingTargetResponse response.

        :param domain: 分配的服务dns，通过此dns执行文件系统挂载，即可访问服务
        :type domain: str (optional)

        :param mount_id: MountTarget的ID
        :type mount_id: str (optional)
        """
        super().__init__()
        self.domain = domain
        self.mount_id = mount_id

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
        if self.domain is not None:
            result['domain'] = self.domain
        if self.mount_id is not None:
            result['mountId'] = self.mount_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateMountingTargetResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('mountId') is not None:
            self.mount_id = m.get('mountId')
        return self
