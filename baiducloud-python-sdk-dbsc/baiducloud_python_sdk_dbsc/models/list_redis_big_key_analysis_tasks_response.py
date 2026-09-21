"""
Request entity for ListRedisBigKeyAnalysisTasksResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.big_key_result_info import BigKeyResultInfo
from baiducloud_python_sdk_dbsc.models.big_key_result_info import BigKeyResultInfo


class ListRedisBigKeyAnalysisTasksResponse(BceResponse):
    """
    ListRedisBigKeyAnalysisTasksResponse
    """

    def __init__(self, data_collection_time=None, element_count_result=None, memory_result=None):
        """
        Initialize ListRedisBigKeyAnalysisTasksResponse response.

        :param data_collection_time: 数据采集时间
        :type data_collection_time: str (optional)

        :param element_count_result: 按数量分析结果
        :type element_count_result: List[BigKeyResultInfo] (optional)

        :param memory_result: 按内存分析结果
        :type memory_result: List[BigKeyResultInfo] (optional)
        """
        super().__init__()
        self.data_collection_time = data_collection_time
        self.element_count_result = element_count_result
        self.memory_result = memory_result

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
        if self.data_collection_time is not None:
            result['dataCollectionTime'] = self.data_collection_time
        if self.element_count_result is not None:
            result['elementCountResult'] = [i.to_dict() for i in self.element_count_result]
        if self.memory_result is not None:
            result['memoryResult'] = [i.to_dict() for i in self.memory_result]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListRedisBigKeyAnalysisTasksResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('dataCollectionTime') is not None:
            self.data_collection_time = m.get('dataCollectionTime')
        if m.get('elementCountResult') is not None:
            self.element_count_result = [BigKeyResultInfo().from_dict(i) for i in m.get('elementCountResult')]
        if m.get('memoryResult') is not None:
            self.memory_result = [BigKeyResultInfo().from_dict(i) for i in m.get('memoryResult')]
        return self
