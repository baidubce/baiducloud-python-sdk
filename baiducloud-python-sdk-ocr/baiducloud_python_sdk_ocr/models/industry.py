"""
Industry information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Industry(AbstractModel):
    """
    Industry
    """

    def __init__(self, industry=None, subindustry=None):
        """
        Initialize Industry instance.

        :param industry: 国民经济行业分类门类名称
        :type industry: str (optional)

        :param subindustry: 国民经济行业分类大类名称
        :type subindustry: str (optional)
        """
        super().__init__()
        self.industry = industry
        self.subindustry = subindustry

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
        if self.industry is not None:
            result['industry'] = self.industry
        if self.subindustry is not None:
            result['subindustry'] = self.subindustry
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Industry

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('subindustry') is not None:
            self.subindustry = m.get('subindustry')
        return self
