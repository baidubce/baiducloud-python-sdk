"""
Response information
"""
from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_bls.models.shard import Shard

from baiducloud_python_sdk_bls.models. import Hit



class Response(BceResponse):
    """
    Response
    """
    def __init__(self, took=None, timed_out=None, shards=None, hits=None, aggregations=None):
        """
        Initialize Response instance.

        :param took: 查询耗时
        :type took: int (optional)

        :param timed_out: 是否超时
        :type timed_out: bool (optional)

        :param shards: shards attribute
        :type shards: Shard (optional)

        :param hits: 命中的文档
        :type hits: Dict[str, List[Hit]] (optional)

        :param aggregations: aggregations attribute
        :type aggregations: Dict[str, object] (optional)
        """
        super().__init__()
        self.took = took
        self.timed_out = timed_out
        self.shards = shards
        self.hits = hits
        self.aggregations = aggregations


    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.took is not None:
            result['took'] = self.took
        if self.timed_out is not None:
            result['timed_out'] = self.timed_out
        if self.shards is not None:
            result['_shards'] = self.shards.to_dict()
        if self.hits is not None:
            
            result['hits'] = {k: [i.to_dict() for i in v] for k, v in self.hits.items()}
            
        if self.aggregations is not None:
            
            result['aggregations'] = self.aggregations
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Response

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('took') is not None:
            self.took = m.get('took')
        if m.get('timed_out') is not None:
            self.timed_out = m.get('timed_out')
        if m.get('_shards') is not None:
            self.shards = Shard().from_dict(m.get('_shards'))
        if m.get('hits') is not None:
            
            self.hits = {k: [Hit().from_dict(i) for i in v] for k, v in m.get('hits').items()}
            
        if m.get('aggregations') is not None:
            
            self.aggregations = m.get('aggregations')
        return self
