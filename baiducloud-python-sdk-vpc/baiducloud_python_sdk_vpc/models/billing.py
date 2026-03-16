from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.reservation import Reservation


class Billing(AbstractModel):
    """
    Billing class represents the billing information for resources.
    
    Attributes:
        payment_timing (str): The payment timing for the billing.
        reservation (Reservation): The reservation details if applicable.
    """
    
    def __init__(self, payment_timing=None, reservation=None):
        """
        Initialize Billing instance.
        
        Args:
            payment_timing (str, optional): The payment timing. Defaults to None.
            reservation (Reservation, optional): The reservation details. Defaults to None.
        """
        super().__init__()
        self.payment_timing = payment_timing
        self.reservation = reservation

    def to_dict(self):
        """
        Convert the Billing object to a dictionary.
        
        Returns:
            dict: A dictionary containing the billing information.
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.reservation is not None:
            result['reservation'] = self.reservation.to_dict()
        return result


    def from_dict(self, m):
        """
        Initialize Billing object from a dictionary.
        
        Args:
            m (dict): A dictionary containing the billing information.
            
        Returns:
            Billing: The Billing object initialized from the dictionary.
        """
        m = m or dict()
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('reservation') is not None:
            self.reservation = Reservation().from_dict(m.get('reservation'))
        return self