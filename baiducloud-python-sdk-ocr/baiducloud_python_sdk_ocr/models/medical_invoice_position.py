"""
MedicalInvoicePosition information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MedicalInvoicePosition(AbstractModel):
    """
    MedicalInvoicePosition
    """

    def __init__(self, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None, x4=None, y4=None):
        """
        Initialize MedicalInvoicePosition instance.

        :param x1: 左上角横坐标
        :type x1: int (optional)

        :param y1: 左上角纵坐标
        :type y1: int (optional)

        :param x2: 右上角横坐标
        :type x2: int (optional)

        :param y2: 右上角纵坐标
        :type y2: int (optional)

        :param x3: 右下角横坐标
        :type x3: int (optional)

        :param y3: 右下角纵坐标
        :type y3: int (optional)

        :param x4: 左下角横坐标
        :type x4: int (optional)

        :param y4: 左下角纵坐标
        :type y4: int (optional)
        """
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

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
        if self.x1 is not None:
            result['x1'] = self.x1
        if self.y1 is not None:
            result['y1'] = self.y1
        if self.x2 is not None:
            result['x2'] = self.x2
        if self.y2 is not None:
            result['y2'] = self.y2
        if self.x3 is not None:
            result['x3'] = self.x3
        if self.y3 is not None:
            result['y3'] = self.y3
        if self.x4 is not None:
            result['x4'] = self.x4
        if self.y4 is not None:
            result['y4'] = self.y4
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalInvoicePosition

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('x1') is not None:
            self.x1 = m.get('x1')
        if m.get('y1') is not None:
            self.y1 = m.get('y1')
        if m.get('x2') is not None:
            self.x2 = m.get('x2')
        if m.get('y2') is not None:
            self.y2 = m.get('y2')
        if m.get('x3') is not None:
            self.x3 = m.get('x3')
        if m.get('y3') is not None:
            self.y3 = m.get('y3')
        if m.get('x4') is not None:
            self.x4 = m.get('x4')
        if m.get('y4') is not None:
            self.y4 = m.get('y4')
        return self
