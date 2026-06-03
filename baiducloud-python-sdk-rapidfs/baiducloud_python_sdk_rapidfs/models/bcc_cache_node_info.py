"""
BCCCacheNodeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BCCCacheNodeInfo(AbstractModel):
    """
    BCCCacheNodeInfo
    """

    def __init__(self, bcc_id=None, bcc_name=None, zone=None, bcc_spec=None):
        """
        Initialize BCCCacheNodeInfo instance.

        :param bcc_id: BCC 实例 ID
        :type bcc_id: str (optional)

        :param bcc_name: BCC 加入时的实例名称
        :type bcc_name: str (optional)

        :param zone: 可用区
        :type zone: str (optional)

        :param bcc_spec: BCC 规格
        :type bcc_spec: str (optional)
        """
        super().__init__()
        self.bcc_id = bcc_id
        self.bcc_name = bcc_name
        self.zone = zone
        self.bcc_spec = bcc_spec

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
        if self.bcc_id is not None:
            result['bccId'] = self.bcc_id
        if self.bcc_name is not None:
            result['bccName'] = self.bcc_name
        if self.zone is not None:
            result['zone'] = self.zone
        if self.bcc_spec is not None:
            result['bccSpec'] = self.bcc_spec
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BCCCacheNodeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bccId') is not None:
            self.bcc_id = m.get('bccId')
        if m.get('bccName') is not None:
            self.bcc_name = m.get('bccName')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('bccSpec') is not None:
            self.bcc_spec = m.get('bccSpec')
        return self
