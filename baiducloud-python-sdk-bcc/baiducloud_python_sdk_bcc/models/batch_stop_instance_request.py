"""
Request entity for BatchStopInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BatchStopInstanceRequest(AbstractModel):
    """
    Request entity for BatchStopInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_ids, force_stop=None, stop_with_no_charge=None):
        """
        Initialize BatchStopInstanceRequest request entity.

        :param instance_ids: 实例id组成的集合，集合元素数量不超过100个
        :type instance_ids: List[str] (required)

        :param force_stop: 指定实例是否强制关机，可选值：true、false，缺省为false
        :type force_stop: bool (optional)

        :param stop_with_no_charge: 指定实例是否关机不计费，可选值：true、false，缺省为false
        :type stop_with_no_charge: bool (optional)
        """
        super().__init__()
        self.instance_ids = instance_ids
        self.force_stop = force_stop
        self.stop_with_no_charge = stop_with_no_charge

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
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.force_stop is not None:
            result['forceStop'] = self.force_stop
        if self.stop_with_no_charge is not None:
            result['stopWithNoCharge'] = self.stop_with_no_charge
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchStopInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('forceStop') is not None:
            self.force_stop = m.get('forceStop')
        if m.get('stopWithNoCharge') is not None:
            self.stop_with_no_charge = m.get('stopWithNoCharge')
        return self
