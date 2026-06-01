"""
Request entity for DescribeLLMServicesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.tag import Tag


class DescribeLLMServicesRequest(AbstractModel):
    """
    Request entity for DescribeLLMServicesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        begin_datetime,
        end_datetime,
        service_name=None,
        service_id=None,
        env=None,
        tag=None,
        order_by=None,
        order=None,
    ):
        """
        Initialize DescribeLLMServicesRequest request entity.

        :param begin_datetime: 开始时间，UTC时间
        :type begin_datetime: str (required)

        :param end_datetime: 结束时间，UTC时间
        :type end_datetime: str (required)

        :param service_name: 按应用名过滤，若未设置返回所有应用
        :type service_name: str (optional)

        :param service_id: 按应用ID过滤
        :type service_id: str (optional)

        :param env: 按env过滤
        :type env: str (optional)

        :param tag: tag parameter
        :type tag: Tag (optional)

        :param order_by: 排序字段，默认值：requests
        :type order_by: str (optional)

        :param order: 排序方向，默认值：desc，可选值：asc(升序)、desc(降序)
        :type order: str (optional)
        """
        super().__init__()
        self.begin_datetime = begin_datetime
        self.end_datetime = end_datetime
        self.service_name = service_name
        self.service_id = service_id
        self.env = env
        self.tag = tag
        self.order_by = order_by
        self.order = order

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
        if self.begin_datetime is not None:
            result['beginDatetime'] = self.begin_datetime
        if self.end_datetime is not None:
            result['endDatetime'] = self.end_datetime
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.env is not None:
            result['env'] = self.env
        if self.tag is not None:
            result['tag'] = self.tag.to_dict()
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLLMServicesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('beginDatetime') is not None:
            self.begin_datetime = m.get('beginDatetime')
        if m.get('endDatetime') is not None:
            self.end_datetime = m.get('endDatetime')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('env') is not None:
            self.env = m.get('env')
        if m.get('tag') is not None:
            self.tag = Tag().from_dict(m.get('tag'))
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        return self
