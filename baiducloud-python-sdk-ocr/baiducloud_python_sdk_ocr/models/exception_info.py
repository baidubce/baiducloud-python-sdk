"""
ExceptionInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ExceptionInfo(AbstractModel):
    """
    ExceptionInfo
    """

    def __init__(
        self,
        addreason=None,
        adddate=None,
        removereason=None,
        removedate=None,
        decisionoffice=None,
        removedecisionoffice=None,
    ):
        """
        Initialize ExceptionInfo instance.

        :param addreason: 列入经营异常名录原因
        :type addreason: str (optional)

        :param adddate: 列入日期
        :type adddate: str (optional)

        :param removereason: 移出经营异常名录原因
        :type removereason: str (optional)

        :param removedate: 移出日期
        :type removedate: str (optional)

        :param decisionoffice: 作出决定机关
        :type decisionoffice: str (optional)

        :param removedecisionoffice: 移除决定机关
        :type removedecisionoffice: str (optional)
        """
        super().__init__()
        self.addreason = addreason
        self.adddate = adddate
        self.removereason = removereason
        self.removedate = removedate
        self.decisionoffice = decisionoffice
        self.removedecisionoffice = removedecisionoffice

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
        if self.addreason is not None:
            result['addreason'] = self.addreason
        if self.adddate is not None:
            result['adddate'] = self.adddate
        if self.removereason is not None:
            result['removereason'] = self.removereason
        if self.removedate is not None:
            result['removedate'] = self.removedate
        if self.decisionoffice is not None:
            result['decisionoffice'] = self.decisionoffice
        if self.removedecisionoffice is not None:
            result['removedecisionoffice'] = self.removedecisionoffice
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ExceptionInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('addreason') is not None:
            self.addreason = m.get('addreason')
        if m.get('adddate') is not None:
            self.adddate = m.get('adddate')
        if m.get('removereason') is not None:
            self.removereason = m.get('removereason')
        if m.get('removedate') is not None:
            self.removedate = m.get('removedate')
        if m.get('decisionoffice') is not None:
            self.decisionoffice = m.get('decisionoffice')
        if m.get('removedecisionoffice') is not None:
            self.removedecisionoffice = m.get('removedecisionoffice')
        return self
