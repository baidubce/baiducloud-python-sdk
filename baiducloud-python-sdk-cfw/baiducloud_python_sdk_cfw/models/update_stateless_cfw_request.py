"""
Request entity for UpdateStatelessCfwRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateStatelessCfwRequest(AbstractModel):
    """
    Request entity for UpdateStatelessCfwRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cfw_id, name=None, description=None, protocol=None, ip_list=None):
        """
        Initialize UpdateStatelessCfwRequest request entity.

        :param cfw_id: cfw_id parameter
        :type cfw_id: str (required)

        :param name: CFW名称，长度不超过65个字符，必须以字母或中文开头，只能包含大小写字母、数字、中文及-_/.字符
        :type name: str (optional)

        :param description: CFW描述，不超过200字符
        :type description: str (optional)

        :param protocol: 协议，取值 [ TCP \\| UDP \\| ICMP \\| ALL ]
        :type protocol: str (optional)

        :param ip_list: IP列表
        :type ip_list: List[str] (optional)
        """
        super().__init__()
        self.cfw_id = cfw_id
        self.name = name
        self.description = description
        self.protocol = protocol
        self.ip_list = ip_list

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
        if self.description is not None:
            result['description'] = self.description
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateStatelessCfwRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cfwId') is not None:
            self.cfw_id = m.get('cfwId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        return self
