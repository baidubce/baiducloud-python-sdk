"""
Request entity for DescribeJobWebterminalResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DescribeJobWebterminalResponse(BceResponse):
    """
    DescribeJobWebterminalResponse
    """

    def __init__(self, request_id=None, web_terminal_url=None):
        """
        Initialize DescribeJobWebterminalResponse response.

        :param request_id: 请求ID
        :type request_id: str (optional)

        :param web_terminal_url: WebTerminal的连接地址
        :type web_terminal_url: str (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.web_terminal_url = web_terminal_url

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.web_terminal_url is not None:
            result['webTerminalUrl'] = self.web_terminal_url
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeJobWebterminalResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('webTerminalUrl') is not None:
            self.web_terminal_url = m.get('webTerminalUrl')
        return self
