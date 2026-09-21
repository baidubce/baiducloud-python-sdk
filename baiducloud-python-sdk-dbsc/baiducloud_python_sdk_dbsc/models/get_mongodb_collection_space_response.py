"""
Request entity for GetMongodbCollectionSpaceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.mongodb_collection_space_item import MongodbCollectionSpaceItem


class GetMongodbCollectionSpaceResponse(BceResponse):
    """
    GetMongodbCollectionSpaceResponse
    """

    def __init__(self, items=None, total_count=None, collection_time=None):
        """
        Initialize GetMongodbCollectionSpaceResponse response.

        :param items: 集合空间信息列表
        :type items: List[MongodbCollectionSpaceItem] (optional)

        :param total_count: 集合总数
        :type total_count: int (optional)

        :param collection_time: 采集时间
        :type collection_time: str (optional)
        """
        super().__init__()
        self.items = items
        self.total_count = total_count
        self.collection_time = collection_time

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
        if self.items is not None:
            result['items'] = [i.to_dict() for i in self.items]
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.collection_time is not None:
            result['collectionTime'] = self.collection_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetMongodbCollectionSpaceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('items') is not None:
            self.items = [MongodbCollectionSpaceItem().from_dict(i) for i in m.get('items')]
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('collectionTime') is not None:
            self.collection_time = m.get('collectionTime')
        return self
