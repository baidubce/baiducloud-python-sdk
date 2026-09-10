"""
InstancePage information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstancePage(AbstractModel):
    """
    InstancePage
    """

    def __init__(
        self,
        cluster_id=None,
        keyword_type=None,
        keyword=None,
        order_by=None,
        order=None,
        page_no=None,
        page_size=None,
        total_count=None,
        instance_list=None,
    ):
        """
        Initialize InstancePage instance.

        :param cluster_id:
        :type cluster_id: str (optional)

        :param keyword_type:
        :type keyword_type: str (optional)

        :param keyword:
        :type keyword: str (optional)

        :param order_by:
        :type order_by: str (optional)

        :param order:
        :type order: str (optional)

        :param page_no:
        :type page_no: int (optional)

        :param page_size:
        :type page_size: int (optional)

        :param total_count:
        :type total_count: int (optional)

        :param instance_list:
        :type instance_list: List[object] (optional)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.keyword_type = keyword_type
        self.keyword = keyword
        self.order_by = order_by
        self.order = order
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.instance_list = instance_list

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.cluster_id is not None:
            result['clusterID'] = self.cluster_id
        if self.keyword_type is not None:
            result['keywordType'] = self.keyword_type
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.order is not None:
            result['order'] = self.order
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.instance_list is not None:
            result['instanceList'] = self.instance_list
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstancePage

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('keywordType') is not None:
            self.keyword_type = m.get('keywordType')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('instanceList') is not None:
            self.instance_list = m.get('instanceList')
        return self
