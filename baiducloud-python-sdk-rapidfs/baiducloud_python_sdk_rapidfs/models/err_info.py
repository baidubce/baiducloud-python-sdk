"""
ErrInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ErrInfo(AbstractModel):
    """
    ErrInfo
    """

    def __init__(self, err_code=None, err_msg=None):
        """
        Initialize ErrInfo instance.

        :param err_code: 错误码
        :type err_code: str (optional)

        :param err_msg: 错误描述
        :type err_msg: str (optional)
        """
        super().__init__()
        self.err_code = err_code
        self.err_msg = err_msg

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
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ErrInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        return self
