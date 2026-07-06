"""
Request entity for DescribeJobsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeJobsRequest(AbstractModel):
    """
    Request entity for DescribeJobsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        resource_pool_id,
        queue_id=None,
        queue=None,
        status=None,
        keyword_type=None,
        keyword=None,
        order_by=None,
        order=None,
        page_number=None,
        page_size=None,
    ):
        """
        Initialize DescribeJobsRequest request entity.

        :param resource_pool_id: resource_pool_id parameter
        :type resource_pool_id: str (required)

        :param queue_id: queue_id parameter
        :type queue_id: str (optional)

        :param queue: 训练任务所属队列，通用资源池须填入队列名称，不填时返回所有。托管资源池须填入队列Id
        :type queue: str (optional)

        :param status: 基于状态筛选任务
        :type status: str (optional)

        :param keyword_type: 筛选关键字类型，当前仅支持name/queueName
        :type keyword_type: str (optional)

        :param keyword: 关键字值
        :type keyword: str (optional)

        :param order_by: 排序字段，支持createdAt，finishedAt，默认为createdAt
        :type order_by: str (optional)

        :param order: 排序方式，可选 [asc, desc]，asc 为升序，desc 为降序，默认值为 desc
        :type order: str (optional)

        :param page_number: 请求分页参数，表示第几页
        :type page_number: int (optional)

        :param page_size: 单页结果数，默认值为10
        :type page_size: int (optional)
        """
        super().__init__()
        self.resource_pool_id = resource_pool_id
        self.queue_id = queue_id
        self.queue = queue
        self.status = status
        self.keyword_type = keyword_type
        self.keyword = keyword
        self.order_by = order_by
        self.order = order
        self.page_number = page_number
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
        if self.queue is not None:
            result['queue'] = self.queue
        if self.status is not None:
            result['status'] = self.status
        if self.keyword_type is not None:
            result['keywordType'] = self.keyword_type
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeJobsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resourcePoolId') is not None:
            self.resource_pool_id = m.get('resourcePoolId')
        if m.get('queueID') is not None:
            self.queue_id = m.get('queueID')
        if m.get('queue') is not None:
            self.queue = m.get('queue')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('keywordType') is not None:
            self.keyword_type = m.get('keywordType')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
