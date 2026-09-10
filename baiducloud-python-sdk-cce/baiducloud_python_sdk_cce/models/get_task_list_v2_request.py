"""
Request entity for GetTaskListV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetTaskListV2Request(AbstractModel):
    """
    Request entity for GetTaskListV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        task_type,
        target_id,
        operation_type=None,
        phase=None,
        order=None,
        order_by=None,
        page_no=None,
        page_size=None,
    ):
        """
        Initialize GetTaskListV2Request request entity.

        :param task_type: task_type parameter
        :type task_type: str (required)

        :param target_id: target_id parameter
        :type target_id: str (required)

        :param operation_type: operation_type parameter
        :type operation_type: str (optional)

        :param phase: phase parameter
        :type phase: str (optional)

        :param order: order parameter
        :type order: str (optional)

        :param order_by: order_by parameter
        :type order_by: str (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.task_type = task_type
        self.target_id = target_id
        self.operation_type = operation_type
        self.phase = phase
        self.order = order
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetTaskListV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('targetID') is not None:
            self.target_id = m.get('targetID')
        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
