"""
Request entity for EipPostpaidToPrepaidRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EipPostpaidToPrepaidRequest(AbstractModel):
    """
    Request entity for EipPostpaidToPrepaidRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eip, purchase_length, band_width, client_token=None):
        """
        Initialize EipPostpaidToPrepaidRequest request entity.

        :param eip: eip parameter
        :type eip: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param purchase_length: 预付费EIP的购买时长，单位为月，取值为1-9,12,24,36。
        :type purchase_length: int (required)

        :param band_width: 预付费EIP的公网带宽。
        :type band_width: int (required)
        """
        super().__init__()
        self.eip = eip
        self.client_token = client_token
        self.purchase_length = purchase_length
        self.band_width = band_width

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
        if self.purchase_length is not None:
            result['purchaseLength'] = self.purchase_length
        if self.band_width is not None:
            result['bandWidth'] = self.band_width
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EipPostpaidToPrepaidRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('purchaseLength') is not None:
            self.purchase_length = m.get('purchaseLength')
        if m.get('bandWidth') is not None:
            self.band_width = m.get('bandWidth')
        return self
