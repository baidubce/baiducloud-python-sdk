"""
Request entity for TwoFactorsVerificationRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TwoFactorsVerificationRequest(AbstractModel):
    """
    Request entity for TwoFactorsVerificationRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, company, regnum):
        """
        Initialize TwoFactorsVerificationRequest request entity.

        :param company: 企业名称
        :type company: str (required)

        :param regnum: 社会统一信用代码
        :type regnum: str (required)
        """
        super().__init__()
        self.company = company
        self.regnum = regnum

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
        if self.company is not None:
            result['company'] = self.company
        if self.regnum is not None:
            result['regnum'] = self.regnum
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TwoFactorsVerificationRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('company') is not None:
            self.company = m.get('company')
        if m.get('regnum') is not None:
            self.regnum = m.get('regnum')
        return self
