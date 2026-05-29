"""
Request entity for CreateAppBlbIpGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateAppBlbIpGroupResponse(BceResponse):
    """
    CreateAppBlbIpGroupResponse
    """

    def __init__(self, id=None, name=None, desc=None):
        """
        Initialize CreateAppBlbIpGroupResponse response.

        :param id: IP组id
        :type id: str (optional)

        :param name: IP组名称
        :type name: str (optional)

        :param desc: IP组描述
        :type desc: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.desc = desc

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
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateAppBlbIpGroupResponse

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
        return self
