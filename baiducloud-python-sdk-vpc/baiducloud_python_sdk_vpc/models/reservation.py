"""
Reservation information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Reservation(AbstractModel):
    """
    Reservation
    """

    def __init__(self, reservation_length=None, reservation_time_unit=None):
        """
        Initialize Reservation instance.

        :param reservation_length: 时长，[1,2,3,4,5,6,7,8,9,12,24,36]
        :type reservation_length: int (optional)

        :param reservation_time_unit: 时间单位，month，当前仅支持按月
        :type reservation_time_unit: str (optional)
        """
        super().__init__()
        self.reservation_length = reservation_length
        self.reservation_time_unit = reservation_time_unit

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
        if self.reservation_length is not None:
            result['reservationLength'] = self.reservation_length
        if self.reservation_time_unit is not None:
            result['reservationTimeUnit'] = self.reservation_time_unit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Reservation

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservationLength') is not None:
            self.reservation_length = m.get('reservationLength')
        if m.get('reservationTimeUnit') is not None:
            self.reservation_time_unit = m.get('reservationTimeUnit')
        return self
