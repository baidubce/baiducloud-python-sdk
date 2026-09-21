"""
MongodbDatabaseSpaceItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MongodbDatabaseSpaceItem(AbstractModel):
    """
    MongodbDatabaseSpaceItem
    """

    def __init__(
        self,
        database=None,
        collection_count=None,
        storage_size=None,
        data_size=None,
        index_size=None,
        object_count=None,
        index_count=None,
        avg_obj_size=None,
        views=None,
        fragmentation_ratio=None,
        index_fragmentation_ratio=None,
        total_size=None,
        free_storage_size=None,
        index_free_storage_size=None,
        total_free_storage_size=None,
    ):
        """
        Initialize MongodbDatabaseSpaceItem instance.

        :param database: 数据库名称
        :type database: str (optional)

        :param collection_count: 集合数量
        :type collection_count: int (optional)

        :param storage_size: 存储空间（字节），分配给空间用于存储文档的空间总和，包括可用空间
        :type storage_size: int (optional)

        :param data_size: 数据空间（字节），保存的未压缩数据的总大小，当删除文档时会减小
        :type data_size: int (optional)

        :param index_size: 索引空间（字节），分配给所有索引的空间总和，包括可用索引空间
        :type index_size: int (optional)

        :param object_count: 文档数量，对象（文档）数量
        :type object_count: int (optional)

        :param index_count: 索引数量，索引总数
        :type index_count: int (optional)

        :param avg_obj_size: 平均文档大小（字节），即dataSize/objects
        :type avg_obj_size: int (optional)

        :param views: 视图数量，视图的数量
        :type views: int (optional)

        :param fragmentation_ratio: 碎片率，可回收空间/总空间
        :type fragmentation_ratio: float (optional)

        :param index_fragmentation_ratio: 索引碎片率，索引空闲空间/索引空间
        :type index_fragmentation_ratio: float (optional)

        :param total_size: 总空间（字节）， 存储大小和索引大小之和
        :type total_size: int (optional)

        :param free_storage_size: 文档空闲空间（字节），分配给空间用于存储文档的可用空间总和
        :type free_storage_size: int (optional)

        :param index_free_storage_size: 索引空闲空间（字节），分配给所有索引的可用空间总和
        :type index_free_storage_size: int (optional)

        :param total_free_storage_size: 总空闲空间（字节），文档空闲空间和索引空闲空间之和
        :type total_free_storage_size: int (optional)
        """
        super().__init__()
        self.database = database
        self.collection_count = collection_count
        self.storage_size = storage_size
        self.data_size = data_size
        self.index_size = index_size
        self.object_count = object_count
        self.index_count = index_count
        self.avg_obj_size = avg_obj_size
        self.views = views
        self.fragmentation_ratio = fragmentation_ratio
        self.index_fragmentation_ratio = index_fragmentation_ratio
        self.total_size = total_size
        self.free_storage_size = free_storage_size
        self.index_free_storage_size = index_free_storage_size
        self.total_free_storage_size = total_free_storage_size

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
        if self.database is not None:
            result['database'] = self.database
        if self.collection_count is not None:
            result['collectionCount'] = self.collection_count
        if self.storage_size is not None:
            result['storageSize'] = self.storage_size
        if self.data_size is not None:
            result['dataSize'] = self.data_size
        if self.index_size is not None:
            result['indexSize'] = self.index_size
        if self.object_count is not None:
            result['objectCount'] = self.object_count
        if self.index_count is not None:
            result['indexCount'] = self.index_count
        if self.avg_obj_size is not None:
            result['avgObjSize'] = self.avg_obj_size
        if self.views is not None:
            result['views'] = self.views
        if self.fragmentation_ratio is not None:
            result['fragmentationRatio'] = self.fragmentation_ratio
        if self.index_fragmentation_ratio is not None:
            result['indexFragmentationRatio'] = self.index_fragmentation_ratio
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        if self.free_storage_size is not None:
            result['freeStorageSize'] = self.free_storage_size
        if self.index_free_storage_size is not None:
            result['indexFreeStorageSize'] = self.index_free_storage_size
        if self.total_free_storage_size is not None:
            result['totalFreeStorageSize'] = self.total_free_storage_size
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MongodbDatabaseSpaceItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('database') is not None:
            self.database = m.get('database')
        if m.get('collectionCount') is not None:
            self.collection_count = m.get('collectionCount')
        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')
        if m.get('dataSize') is not None:
            self.data_size = m.get('dataSize')
        if m.get('indexSize') is not None:
            self.index_size = m.get('indexSize')
        if m.get('objectCount') is not None:
            self.object_count = m.get('objectCount')
        if m.get('indexCount') is not None:
            self.index_count = m.get('indexCount')
        if m.get('avgObjSize') is not None:
            self.avg_obj_size = m.get('avgObjSize')
        if m.get('views') is not None:
            self.views = m.get('views')
        if m.get('fragmentationRatio') is not None:
            self.fragmentation_ratio = m.get('fragmentationRatio')
        if m.get('indexFragmentationRatio') is not None:
            self.index_fragmentation_ratio = m.get('indexFragmentationRatio')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        if m.get('freeStorageSize') is not None:
            self.free_storage_size = m.get('freeStorageSize')
        if m.get('indexFreeStorageSize') is not None:
            self.index_free_storage_size = m.get('indexFreeStorageSize')
        if m.get('totalFreeStorageSize') is not None:
            self.total_free_storage_size = m.get('totalFreeStorageSize')
        return self
