"""
DocAnalysisSecIdx information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DocAnalysisSecIdx(AbstractModel):
    """
    DocAnalysisSecIdx
    """

    def __init__(self, idx=None, para_idx=None, row_idx=None, col_idx=None):
        """
        Initialize DocAnalysisSecIdx instance.

        :param idx: sections返回参数中的5个版面属性里，每个属性下包含的文本行id序号
        :type idx: List[float] (optional)

        :param para_idx: para_idx attribute
        :type para_idx: List[float] (optional)

        :param row_idx: 当且仅当attribute=section时才会返回。表示，将所有栏表示成M×N的网格，所属网格的行的id
        :type row_idx: List[float] (optional)

        :param col_idx: 当且仅当attribute=section时才会返回。表示，将所有栏表示成M×N的网格，所属网格的列的id
        :type col_idx: List[float] (optional)
        """
        super().__init__()
        self.idx = idx
        self.para_idx = para_idx
        self.row_idx = row_idx
        self.col_idx = col_idx

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
        if self.idx is not None:
            result['idx'] = self.idx
        if self.para_idx is not None:
            result['para_idx'] = self.para_idx
        if self.row_idx is not None:
            result['row_idx'] = self.row_idx
        if self.col_idx is not None:
            result['col_idx'] = self.col_idx
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisSecIdx

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('idx') is not None:
            self.idx = m.get('idx')
        if m.get('para_idx') is not None:
            self.para_idx = m.get('para_idx')
        if m.get('row_idx') is not None:
            self.row_idx = m.get('row_idx')
        if m.get('col_idx') is not None:
            self.col_idx = m.get('col_idx')
        return self
