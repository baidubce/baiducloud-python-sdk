"""
VehicleNumber information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VehicleNumber(AbstractModel):
    """
    VehicleNumber
    """

    def __init__(self, car=None, truck=None, bus=None, motorbike=None, tricycle=None, carplate=None):
        """
        Initialize VehicleNumber instance.

        :param car: 小轿车数量
        :type car: int (optional)

        :param truck: 卡车数量
        :type truck: int (optional)

        :param bus: 公交车数量
        :type bus: int (optional)

        :param motorbike: 摩托车数量
        :type motorbike: int (optional)

        :param tricycle: 三轮车数量
        :type tricycle: int (optional)

        :param carplate: 车牌数量
        :type carplate: int (optional)
        """
        super().__init__()
        self.car = car
        self.truck = truck
        self.bus = bus
        self.motorbike = motorbike
        self.tricycle = tricycle
        self.carplate = carplate

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
        if self.car is not None:
            result['car'] = self.car
        if self.truck is not None:
            result['truck'] = self.truck
        if self.bus is not None:
            result['bus'] = self.bus
        if self.motorbike is not None:
            result['motorbike'] = self.motorbike
        if self.tricycle is not None:
            result['tricycle'] = self.tricycle
        if self.carplate is not None:
            result['carplate'] = self.carplate
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VehicleNumber

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('car') is not None:
            self.car = m.get('car')
        if m.get('truck') is not None:
            self.truck = m.get('truck')
        if m.get('bus') is not None:
            self.bus = m.get('bus')
        if m.get('motorbike') is not None:
            self.motorbike = m.get('motorbike')
        if m.get('tricycle') is not None:
            self.tricycle = m.get('tricycle')
        if m.get('carplate') is not None:
            self.carplate = m.get('carplate')
        return self
