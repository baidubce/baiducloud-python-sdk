"""
Request entity for UpdateSubUserIdpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateSubUserIdpRequest(AbstractModel):
    """
    Request entity for UpdateSubUserIdpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, file_name, encode_metadata, auxiliary_domain=None):
        """
        Initialize UpdateSubUserIdpRequest request entity.

        :param file_name: 文件名称，必须为xml格式文件
        :type file_name: str (required)

        :param encode_metadata: Base64编码后的IdP元数据
        :type encode_metadata: str (required)

        :param auxiliary_domain: 辅助域名
        :type auxiliary_domain: str (optional)
        """
        super().__init__()
        self.file_name = file_name
        self.encode_metadata = encode_metadata
        self.auxiliary_domain = auxiliary_domain

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
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.encode_metadata is not None:
            result['encodeMetadata'] = self.encode_metadata
        if self.auxiliary_domain is not None:
            result['auxiliaryDomain'] = self.auxiliary_domain
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateSubUserIdpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('encodeMetadata') is not None:
            self.encode_metadata = m.get('encodeMetadata')
        if m.get('auxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('auxiliaryDomain')
        return self
