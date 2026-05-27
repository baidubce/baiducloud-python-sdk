"""
Request entity for CreateAppBlbServerGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateAppBlbServerGroupResponse(BceResponse):
    """
    CreateAppBlbServerGroupResponse
    """

    def __init__(self, id=None, name=None, desc=None, status=None):
        """
        Initialize CreateAppBlbServerGroupResponse response.

        :param id: 服务器组id
        :type id: str (optional)

        :param name: 服务器组的名称
        :type name: str (optional)

        :param desc: 服务器组的描述
        :type desc: str (optional)

        :param status: 服务器组状态，详见[blbStatus](BLB/API参考/附录.md#blbStatus)
        :type status: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.desc = desc
        self.status = status

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAppBlbServerGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
