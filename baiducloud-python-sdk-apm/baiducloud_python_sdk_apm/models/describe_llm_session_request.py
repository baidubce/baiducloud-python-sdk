"""
Request entity for DescribeLLMSessionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeLLMSessionRequest(AbstractModel):
    """
    Request entity for DescribeLLMSessionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, session_id, begin_datetime, end_datetime):
        """
        Initialize DescribeLLMSessionRequest request entity.

        :param session_id: 会话ID
        :type session_id: str (required)

        :param begin_datetime: Session开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: Session结束时间，UTC时间
        :type end_datetime: str (required)
        """
        super().__init__()
        self.session_id = session_id
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime

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
        if self.session_id is not None:
            result['sessionID'] = self.session_id
        if self.begin_datetime is not None:
            result['beginDatetime'] = self.begin_datetime
        if self.end_datetime is not None:
            result['endDatetime'] = self.end_datetime
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLLMSessionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sessionID') is not None:
            self.session_id = m.get('sessionID')
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        return self
