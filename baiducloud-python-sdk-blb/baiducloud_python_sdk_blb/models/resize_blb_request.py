"""
Request entity for ResizeBlbRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResizeBlbRequest(AbstractModel):
    """
    Request entity for ResizeBlbRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, client_token=None, performance_level=None):
        """
        Initialize ResizeBlbRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param performance_level:
            性能规格。取值如下：\"small1\"标准型1，\"small2\"标准型2，\"medium1\"增强型1，\"medium2\"增强型2，\"large1\"超大型1，\"large2\"超大型2，
            \"large3\"超大型3。仅后付费-按使用量支持变配为\"unlimited\"不限速。
        :type performance_level: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.performance_level = performance_level

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
        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResizeBlbRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')
        return self
