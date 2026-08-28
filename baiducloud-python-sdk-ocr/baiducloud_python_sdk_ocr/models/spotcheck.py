"""
Spotcheck information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Spotcheck(AbstractModel):
    """
    Spotcheck
    """

    def __init__(self, no=None, executiveorg=None, type=None, ocr_date=None, consequence=None, remark=None):
        """
        Initialize Spotcheck instance.

        :param no: 登记编号
        :type no: str (optional)

        :param executiveorg: 检查实施机关
        :type executiveorg: str (optional)

        :param type: 类型
        :type type: str (optional)

        :param ocr_date: 日期
        :type ocr_date: str (optional)

        :param consequence: 结果
        :type consequence: str (optional)

        :param remark: 备注
        :type remark: str (optional)
        """
        super().__init__()
        self.no = no
        self.executiveorg = executiveorg
        self.type = type
        self.ocr_date = ocr_date
        self.consequence = consequence
        self.remark = remark

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
        if self.no is not None:
            result['no'] = self.no
        if self.executiveorg is not None:
            result['executiveorg'] = self.executiveorg
        if self.type is not None:
            result['type'] = self.type
        if self.ocr_date is not None:
            result['date'] = self.ocr_date
        if self.consequence is not None:
            result['consequence'] = self.consequence
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Spotcheck

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('no') is not None:
            self.no = m.get('no')
        if m.get('executiveorg') is not None:
            self.executiveorg = m.get('executiveorg')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('date') is not None:
            self.ocr_date = m.get('date')
        if m.get('consequence') is not None:
            self.consequence = m.get('consequence')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self
