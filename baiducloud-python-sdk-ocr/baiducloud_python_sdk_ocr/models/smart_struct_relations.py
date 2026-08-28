"""
SmartStructRelations information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.smart_struct_kv_relation import SmartStructKVRelation

from baiducloud_python_sdk_ocr.models.smart_struct_table_relations import SmartStructTableRelations


class SmartStructRelations(AbstractModel):
    """
    SmartStructRelations
    """

    def __init__(self, kv_relations=None, table_relations=None):
        """
        Initialize SmartStructRelations instance.

        :param kv_relations: 非表格区的 k-v 结构化关系，可支持一对一、一对多的关系
        :type kv_relations: List[SmartStructKVRelation] (optional)

        :param table_relations: table_relations attribute
        :type table_relations: SmartStructTableRelations (optional)
        """
        super().__init__()
        self.kv_relations = kv_relations
        self.table_relations = table_relations

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
        if self.kv_relations is not None:
            result['kv_relations'] = [i.to_dict() for i in self.kv_relations]
        if self.table_relations is not None:
            result['table_relations'] = self.table_relations.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SmartStructRelations

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('kv_relations') is not None:
            self.kv_relations = [SmartStructKVRelation().from_dict(i) for i in m.get('kv_relations')]
        if m.get('table_relations') is not None:
            self.table_relations = SmartStructTableRelations().from_dict(m.get('table_relations'))
        return self
