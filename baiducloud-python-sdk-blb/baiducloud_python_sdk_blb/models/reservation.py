"""
Reservation information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Reservation(AbstractModel):
    """
    Reservation
    """

    def __init__(self, reservation_length=None):
        """
        Initialize Reservation instance.

        :param reservation_length: 购买月份时长，取值范围为：[1,2,3,4,5,6,7,8,9,12,24,36]
        :type reservation_length: int (optional)
        """
        super().__init__()
        self.reservation_length = reservation_length

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
        return self
