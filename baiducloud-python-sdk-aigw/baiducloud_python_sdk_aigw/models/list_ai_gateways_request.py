"""
Request entity for ListAiGatewaysRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListAiGatewaysRequest(AbstractModel):
    """
    Request entity for ListAiGatewaysRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        x_region,
        keyword=None,
        keyword_type=None,
        status=None,
        src_product=None,
        tag_key=None,
        tag_value=None,
        resource_group_id=None,
        page_no=None,
        page_size=None,
        order_by=None,
        order=None,
    ):
        """
        Initialize ListAiGatewaysRequest request entity.

        :param keyword: keyword parameter
        :type keyword: str (optional)

        :param keyword_type: keyword_type parameter
        :type keyword_type: str (optional)

        :param status: status parameter
        :type status: str (optional)

        :param src_product: src_product parameter
        :type src_product: str (optional)

        :param tag_key: tag_key parameter
        :type tag_key: str (optional)

        :param tag_value: tag_value parameter
        :type tag_value: str (optional)

        :param resource_group_id: resource_group_id parameter
        :type resource_group_id: str (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)

        :param order_by: order_by parameter
        :type order_by: str (optional)

        :param order: order parameter
        :type order: str (optional)

        :param x_region: x_region parameter
        :type x_region: str (required)
        """
        super().__init__()
        self.keyword = keyword
        self.keyword_type = keyword_type
        self.status = status
        self.src_product = src_product
        self.tag_key = tag_key
        self.tag_value = tag_value
        self.resource_group_id = resource_group_id
        self.page_no = page_no
        self.page_size = page_size
        self.order_by = order_by
        self.order = order
        self.x_region = x_region

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
        :rtype: ListAiGatewaysRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('keywordType') is not None:
            self.keyword_type = m.get('keywordType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('srcProduct') is not None:
            self.src_product = m.get('srcProduct')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('X-Region') is not None:
            self.x_region = m.get('X-Region')
        return self
