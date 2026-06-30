"""
Idp information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Idp(AbstractModel):
    """
    Idp
    """

    def __init__(self, status=None, domain_id=None, encode_metadata=None, file_name=None, auxiliary_domain=None):
        """
        Initialize Idp instance.

        :param status: 用户联合功能状态，开启状态返回enable，关闭状态为disable
        :type status: str (optional)

        :param domain_id: 账户ID
        :type domain_id: str (optional)

        :param encode_metadata: Base64编码后的IdP元数据
        :type encode_metadata: str (optional)

        :param file_name: IdP元数据文件名称
        :type file_name: str (optional)

        :param auxiliary_domain: 辅助域名
        :type auxiliary_domain: str (optional)
        """
        super().__init__()
        self.status = status
        self.domain_id = domain_id
        self.encode_metadata = encode_metadata
        self.file_name = file_name
        self.auxiliary_domain = auxiliary_domain

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.domain_id is not None:
            result['domainId'] = self.domain_id
        if self.encode_metadata is not None:
            result['encodeMetadata'] = self.encode_metadata
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.auxiliary_domain is not None:
            result['auxiliaryDomain'] = self.auxiliary_domain
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Idp

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')
        if m.get('encodeMetadata') is not None:
            self.encode_metadata = m.get('encodeMetadata')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('auxiliaryDomain') is not None:
            self.auxiliary_domain = m.get('auxiliaryDomain')
        return self
