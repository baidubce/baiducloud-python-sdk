"""
SmartStructTableRelations information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.smart_struct_kv_relation import SmartStructKVRelation

from baiducloud_python_sdk_ocr.models.smart_struct_kv_relation import SmartStructKVRelation

from baiducloud_python_sdk_ocr.models.smart_struct_kv_relation import SmartStructKVRelation


class SmartStructTableRelations(AbstractModel):
    """
    SmartStructTableRelations
    """

    def __init__(self, kk_relations=None, kv_relations=None, vv_relations=None):
        """
        Initialize SmartStructTableRelations instance.

        :param kk_relations: 表格区的 k-k 结构关系，即多级表头的结构关系，可支持一对一、一对多的关系
        :type kk_relations: List[SmartStructKVRelation] (optional)

        :param kv_relations: 表格区的k-v结构关系，可支持一对一、一对多的关系
        :type kv_relations: List[SmartStructKVRelation] (optional)

        :param vv_relations: 表格区的v-v结构关系，可支持一对一、一对多的关系
        :type vv_relations: List[SmartStructKVRelation] (optional)
        """
        super().__init__()
        self.kk_relations = kk_relations
        self.kv_relations = kv_relations
        self.vv_relations = vv_relations

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
        if self.kk_relations is not None:
            result['kk_relations'] = [i.to_dict() for i in self.kk_relations]
        if self.kv_relations is not None:
            result['kv_relations'] = [i.to_dict() for i in self.kv_relations]
        if self.vv_relations is not None:
            result['vv_relations'] = [i.to_dict() for i in self.vv_relations]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SmartStructTableRelations

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('kk_relations') is not None:
            self.kk_relations = [SmartStructKVRelation().from_dict(i) for i in m.get('kk_relations')]
        if m.get('kv_relations') is not None:
            self.kv_relations = [SmartStructKVRelation().from_dict(i) for i in m.get('kv_relations')]
        if m.get('vv_relations') is not None:
            self.vv_relations = [SmartStructKVRelation().from_dict(i) for i in m.get('vv_relations')]
        return self
