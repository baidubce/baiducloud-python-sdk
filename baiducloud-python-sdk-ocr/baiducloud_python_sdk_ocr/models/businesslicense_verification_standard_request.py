"""
Request entity for BusinesslicenseVerificationStandardRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BusinesslicenseVerificationStandardRequest(AbstractModel):
    """
    Request entity for BusinesslicenseVerificationStandardRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, verifynum):
        """
        Initialize BusinesslicenseVerificationStandardRequest request entity.

        :param verifynum: 查询关键字段（企业名称、注册号、社会统一信用代码，可任意输入其中一种）
        :type verifynum: str (required)
        """
        super().__init__()
        self.verifynum = verifynum

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
        if self.verifynum is not None:
            result['verifynum'] = self.verifynum
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BusinesslicenseVerificationStandardRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('verifynum') is not None:
            self.verifynum = m.get('verifynum')
        return self
