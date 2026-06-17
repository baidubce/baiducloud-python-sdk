"""
Request entity for BatchChangeToPrepaidRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.prepay_config import PrepayConfig


class BatchChangeToPrepaidRequest(AbstractModel):
    """
    Request entity for BatchChangeToPrepaidRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, config):
        """
        Initialize BatchChangeToPrepaidRequest request entity.

        :param config: 需要批量转包年包月实例的配置，最多支持20个
        :type config: List[PrepayConfig] (required)
        """
        super().__init__()
        self.config = config

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
        if self.config is not None:
            result['config'] = [i.to_dict() for i in self.config]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchChangeToPrepaidRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('config') is not None:
            self.config = [PrepayConfig().from_dict(i) for i in m.get('config')]
        return self
