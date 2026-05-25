"""
Request entity for CreateBlbResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateBlbResponse(BceResponse):
    """
    CreateBlbResponse
    """

    def __init__(self, address=None, name=None, blb_id=None, desc=None):
        """
        Initialize CreateBlbResponse response.

        :param address: 分配的内网服务地址IP，通过这个IP即能通过内网访问该实例
        :type address: str (optional)

        :param name: LoadBalancer的名称
        :type name: str (optional)

        :param blb_id: LoadBalancer的ID。后续针对该实例的操作，均需要在请求中带上此ID
        :type blb_id: str (optional)

        :param desc: LoadBalancer的描述
        :type desc: str (optional)
        """
        super().__init__()
        self.address = address
        self.name = name
        self.blb_id = blb_id
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
        if self.address is not None:
            result['address'] = self.address
        if self.name is not None:
            result['name'] = self.name
        if self.blb_id is not None:
            result['blbId'] = self.blb_id
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
        :rtype: CreateBlbResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self
