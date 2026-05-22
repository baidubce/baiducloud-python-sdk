"""
AdditionalCertDomain information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AdditionalCertDomain(AbstractModel):
    """
    AdditionalCertDomain
    """

    def __init__(self, cert_id=None, host=None):
        """
        Initialize AdditionalCertDomain instance.

        :param cert_id: 证书ID
        :type cert_id: str (optional)

        :param host: 证书域名。若证书的产品类型为通配符域名版还支持通配符域名及其子域名
        :type host: str (optional)
        """
        super().__init__()
        self.cert_id = cert_id
        self.host = host

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
        if self.cert_id is not None:
            result['certId'] = self.cert_id
        if self.host is not None:
            result['Host'] = self.host
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AdditionalCertDomain

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('certId') is not None:
            self.cert_id = m.get('certId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        return self
