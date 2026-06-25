"""
Request entity for RemoteReadResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class RemoteReadResponse(BceResponse):
    """
    RemoteReadResponse
    """

    def __init__(
        self,
        status=None,
        is_partial=None,
        data=None,
        data_result_type=None,
        data_result=None,
        data_result_metric=None,
        data_result_values=None,
        data_result_value=None,
    ):
        """
        Initialize RemoteReadResponse response.

        :param status: 请求是否成功。
        :type status: str (optional)

        :param is_partial: 查询结果是否为部分数据。
        :type is_partial: bool (optional)

        :param data: data field
        :type data: object (optional)

        :param data_result_type: 查询结果类型，如 `matrix` 或 `vector`。
        :type data_result_type: str (optional)

        :param data_result: 查询结果列表，列表项包含 `metric` 以及 `values` 或 `value` 等信息。
        :type data_result: List[object] (optional)

        :param data_result_metric: 查询指标的所有维度。
        :type data_result_metric: Dict[str, object] (optional)

        :param data_result_values: 区间查询返回的样本点列表，每个元素为 `[时间戳, 数值]`。
        :type data_result_values: List[object] (optional)

        :param data_result_value: 即时查询返回的单个样本点，格式为 `[时间戳, 数值]`。
        :type data_result_value: List[object] (optional)
        """
        super().__init__()
        self.status = status
        self.is_partial = is_partial
        self.data = data
        self.data_result_type = data_result_type
        self.data_result = data_result
        self.data_result_metric = data_result_metric
        self.data_result_values = data_result_values
        self.data_result_value = data_result_value

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
        if self.status is not None:
            result['status'] = self.status
        if self.is_partial is not None:
            result['isPartial'] = self.is_partial
        if self.data is not None:
            result['data'] = self.data
        if self.data_result_type is not None:
            result['data.resultType'] = self.data_result_type
        if self.data_result is not None:
            result['data.result'] = self.data_result
        if self.data_result_metric is not None:
            result['data.result[].metric'] = self.data_result_metric
        if self.data_result_values is not None:
            result['data.result[].values'] = self.data_result_values
        if self.data_result_value is not None:
            result['data.result[].value'] = self.data_result_value
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoteReadResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('isPartial') is not None:
            self.is_partial = m.get('isPartial')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('data.resultType') is not None:
            self.data_result_type = m.get('data.resultType')
        if m.get('data.result') is not None:
            self.data_result = m.get('data.result')
        if m.get('data.result[].metric') is not None:
            self.data_result_metric = m.get('data.result[].metric')
        if m.get('data.result[].values') is not None:
            self.data_result_values = m.get('data.result[].values')
        if m.get('data.result[].value') is not None:
            self.data_result_value = m.get('data.result[].value')
        return self
