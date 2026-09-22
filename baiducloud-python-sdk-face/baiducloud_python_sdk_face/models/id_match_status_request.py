"""
Request entity for IdMatchStatusRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IdMatchStatusRequest(AbstractModel):
    """
    Request entity for IdMatchStatusRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, id_card_number, start_date, end_date):
        """
        Initialize IdMatchStatusRequest request entity.

        :param name: 姓名（注：需要是UTF-8编码的中文）
        :type name: str (required)

        :param id_card_number: 身份证号
        :type id_card_number: str (required)

        :param start_date: start_date parameter
        :type start_date: str (required)

        :param end_date: end_date parameter
        :type end_date: str (required)
        """
        super().__init__()
        self.name = name
        self.id_card_number = id_card_number
        self.start_date = start_date
        self.end_date = end_date

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
        if self.name is not None:
            result['name'] = self.name
        if self.id_card_number is not None:
            result['id_card_number'] = self.id_card_number
        if self.start_date is not None:
            result['start_date'] = self.start_date
        if self.end_date is not None:
            result['end_date'] = self.end_date
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IdMatchStatusRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id_card_number') is not None:
            self.id_card_number = m.get('id_card_number')
        if m.get('start_date') is not None:
            self.start_date = m.get('start_date')
        if m.get('end_date') is not None:
            self.end_date = m.get('end_date')
        return self
