"""
BccNameConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BccNameConfig(AbstractModel):
    """
    BccNameConfig
    """

    def __init__(self, bcc_name=None, bcc_hostname=None, auto_seq_suffix=None, open_hostname_domain=None):
        """
        Initialize BccNameConfig instance.

        :param bcc_name: 虚拟机名字（可选）。默认都不指定name。如果指定name：批量时name作为名字的前缀。后端将加上后缀
        :type bcc_name: str (optional)

        :param bcc_hostname: bcc_hostname attribute
        :type bcc_hostname: str (optional)

        :param auto_seq_suffix: 是否自动生成name和hostname有序后缀（可选参数） 是:true 否:false
        :type auto_seq_suffix: bool (optional)

        :param open_hostname_domain: 是否自动生成hostname domain（可选参数） 是:true 否:false
        :type open_hostname_domain: bool (optional)
        """
        super().__init__()
        self.bcc_name = bcc_name
        self.bcc_hostname = bcc_hostname
        self.auto_seq_suffix = auto_seq_suffix
        self.open_hostname_domain = open_hostname_domain

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
        if self.bcc_name is not None:
            result['bccName'] = self.bcc_name
        if self.bcc_hostname is not None:
            result['bccHostname'] = self.bcc_hostname
        if self.auto_seq_suffix is not None:
            result['autoSeqSuffix'] = self.auto_seq_suffix
        if self.open_hostname_domain is not None:
            result['openHostnameDomain'] = self.open_hostname_domain
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BccNameConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bccName') is not None:
            self.bcc_name = m.get('bccName')
        if m.get('bccHostname') is not None:
            self.bcc_hostname = m.get('bccHostname')
        if m.get('autoSeqSuffix') is not None:
            self.auto_seq_suffix = m.get('autoSeqSuffix')
        if m.get('openHostnameDomain') is not None:
            self.open_hostname_domain = m.get('openHostnameDomain')
        return self
