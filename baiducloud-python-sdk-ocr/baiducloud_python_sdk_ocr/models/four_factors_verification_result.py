"""
FourFactorsVerificationResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FourFactorsVerificationResult(AbstractModel):
    """
    FourFactorsVerificationResult
    """

    def __init__(self, verifyresult=None, namematch=None, idnummatch=None, companymatch=None, regnummatch=None):
        """
        Initialize FourFactorsVerificationResult instance.

        :param verifyresult: 核验结果：返回值为: 1（四要素完全匹配） 0（四要素不完全匹配）
        :type verifyresult: str (optional)

        :param namematch: 法人姓名匹配结果，1：匹配 0：不匹配 2：无法验证
        :type namematch: str (optional)

        :param idnummatch: 注册证件号匹配结果，1：匹配 0：不匹配 2：无法验证
        :type idnummatch: str (optional)

        :param companymatch: 企业名称匹配结果，1：匹配 0：不匹配 2：无法验证
        :type companymatch: str (optional)

        :param regnummatch: 统一社会信用代码匹配结果，1：匹配 0：不匹配 2：无法验证
        :type regnummatch: str (optional)
        """
        super().__init__()
        self.verifyresult = verifyresult
        self.namematch = namematch
        self.idnummatch = idnummatch
        self.companymatch = companymatch
        self.regnummatch = regnummatch

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
        if self.verifyresult is not None:
            result['verifyresult'] = self.verifyresult
        if self.namematch is not None:
            result['namematch'] = self.namematch
        if self.idnummatch is not None:
            result['idnummatch'] = self.idnummatch
        if self.companymatch is not None:
            result['companymatch'] = self.companymatch
        if self.regnummatch is not None:
            result['regnummatch'] = self.regnummatch
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FourFactorsVerificationResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('verifyresult') is not None:
            self.verifyresult = m.get('verifyresult')
        if m.get('namematch') is not None:
            self.namematch = m.get('namematch')
        if m.get('idnummatch') is not None:
            self.idnummatch = m.get('idnummatch')
        if m.get('companymatch') is not None:
            self.companymatch = m.get('companymatch')
        if m.get('regnummatch') is not None:
            self.regnummatch = m.get('regnummatch')
        return self
