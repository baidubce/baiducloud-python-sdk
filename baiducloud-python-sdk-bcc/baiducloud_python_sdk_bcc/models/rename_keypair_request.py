"""
Request entity for RenameKeypairRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RenameKeypairRequest(AbstractModel):
    """
    Request entity for RenameKeypairRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, keypair_id, name):
        """
        Initialize RenameKeypairRequest request entity.

        :param keypair_id: keypair_id parameter
        :type keypair_id: str (required)

        :param name: 新的密钥对名称，只支持大小写字母、数字、汉字以及-_ /.特殊字符，必须以字母开头，长度1-65。
        :type name: str (required)
        """
        super().__init__()
        self.keypair_id = keypair_id
        self.name = name

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RenameKeypairRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keypairId') is not None:
            self.keypair_id = m.get('keypairId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
