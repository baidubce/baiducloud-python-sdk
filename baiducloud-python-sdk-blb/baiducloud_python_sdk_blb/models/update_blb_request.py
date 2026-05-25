"""
Request entity for UpdateBlbRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateBlbRequest(AbstractModel):
    """
    Request entity for UpdateBlbRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, client_token=None, name=None, desc=None, allow_delete=None, allocate_ipv6=None):
        """
        Initialize UpdateBlbRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: name parameter
        :type name: str (optional)

        :param desc: LoadBalancer实例的描述，便于用户添加更详细的描述信息。长度0~450个字节，支持中文。默认为空
        :type desc: str (optional)

        :param allow_delete: 是否允许删除。缺省值为true，代表允许删除
        :type allow_delete: bool (optional)

        :param allocate_ipv6: 是否分配ipv6地址。true代表分配ipv6地址，false代表不分配ipv6地址
        :type allocate_ipv6: bool (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.name = name
        self.desc = desc
        self.allow_delete = allow_delete
        self.allocate_ipv6 = allocate_ipv6

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
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.allow_delete is not None:
            result['allowDelete'] = self.allow_delete
        if self.allocate_ipv6 is not None:
            result['allocateIpv6'] = self.allocate_ipv6
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateBlbRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('allowDelete') is not None:
            self.allow_delete = m.get('allowDelete')
        if m.get('allocateIpv6') is not None:
            self.allocate_ipv6 = m.get('allocateIpv6')
        return self
