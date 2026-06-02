"""
BillingForRenew information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.reservation_for_create import ReservationForCreate


class BillingForRenew(AbstractModel):
    """
    BillingForRenew
    """

    def __init__(self, reservation=None):
        """
        Initialize BillingForRenew instance.

        :param reservation: reservation attribute
        :type reservation: ReservationForCreate (optional)
        """
        super().__init__()
        self.reservation = reservation

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
        if self.reservation is not None:
            result['reservation'] = self.reservation.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BillingForRenew

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservation') is not None:
            self.reservation = ReservationForCreate().from_dict(m.get('reservation'))
        return self
