"""
MediInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MediInfo(AbstractModel):
    """
    MediInfo
    """

    def __init__(
        self, medi_code=None, medi_name=None, medi_register=None, medi_type=None, medi_region=None, medi_check=None
    ):
        """
        Initialize MediInfo instance.

        :param medi_code: 药品编码
        :type medi_code: str (optional)

        :param medi_name: 药品名
        :type medi_name: str (optional)

        :param medi_register: 药品注册号
        :type medi_register: str (optional)

        :param medi_type: 医保类型
        :type medi_type: str (optional)

        :param medi_region: 医保目录的城市
        :type medi_region: str (optional)

        :param medi_check: 是否命中医保目录，1表示命中，0表示未命中
        :type medi_check: int (optional)
        """
        super().__init__()
        self.medi_code = medi_code
        self.medi_name = medi_name
        self.medi_register = medi_register
        self.medi_type = medi_type
        self.medi_region = medi_region
        self.medi_check = medi_check

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
        if self.medi_code is not None:
            result['medi_code'] = self.medi_code
        if self.medi_name is not None:
            result['medi_name'] = self.medi_name
        if self.medi_register is not None:
            result['medi_register'] = self.medi_register
        if self.medi_type is not None:
            result['medi_type'] = self.medi_type
        if self.medi_region is not None:
            result['medi_region'] = self.medi_region
        if self.medi_check is not None:
            result['medi_check'] = self.medi_check
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MediInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('medi_code') is not None:
            self.medi_code = m.get('medi_code')
        if m.get('medi_name') is not None:
            self.medi_name = m.get('medi_name')
        if m.get('medi_register') is not None:
            self.medi_register = m.get('medi_register')
        if m.get('medi_type') is not None:
            self.medi_type = m.get('medi_type')
        if m.get('medi_region') is not None:
            self.medi_region = m.get('medi_region')
        if m.get('medi_check') is not None:
            self.medi_check = m.get('medi_check')
        return self
