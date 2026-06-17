"""
Request entity for DescribeRegionsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeRegionsRequest(AbstractModel):
    """
    Request entity for DescribeRegionsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, region=None):
        """
        Initialize DescribeRegionsRequest request entity.

        :param region: 指定地域获取对应的域名，不传默认获取全部地域域名列表
        :type region: str (optional)
        """
        super().__init__()
        self.region = region

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
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeRegionsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        return self
