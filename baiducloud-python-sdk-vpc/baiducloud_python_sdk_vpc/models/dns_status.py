"""
DnsStatus information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DnsStatus(AbstractModel):
    """
    DnsStatus
    """

    def __init__(self, close=None, wait=None, syncing=None, open=None, closing=None):
        """
        Initialize DnsStatus instance.

        :param close: 关闭同步
        :type close: str (optional)

        :param wait: 等待同步
        :type wait: str (optional)

        :param syncing: 同步中
        :type syncing: str (optional)

        :param open: 开启同步
        :type open: str (optional)

        :param closing: 关闭同步中
        :type closing: str (optional)
        """
        super().__init__()
        self.close = close
        self.wait = wait
        self.syncing = syncing
        self.open = open
        self.closing = closing

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
        if self.close is not None:
            result['close'] = self.close
        if self.wait is not None:
            result['wait'] = self.wait
        if self.syncing is not None:
            result['syncing'] = self.syncing
        if self.open is not None:
            result['open'] = self.open
        if self.closing is not None:
            result['closing'] = self.closing
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DnsStatus

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('close') is not None:
            self.close = m.get('close')
        if m.get('wait') is not None:
            self.wait = m.get('wait')
        if m.get('syncing') is not None:
            self.syncing = m.get('syncing')
        if m.get('open') is not None:
            self.open = m.get('open')
        if m.get('closing') is not None:
            self.closing = m.get('closing')
        return self
