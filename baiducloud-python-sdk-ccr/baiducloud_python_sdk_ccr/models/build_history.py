"""
BuildHistory information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BuildHistory(AbstractModel):
    """
    BuildHistory
    """

    def __init__(self, created=None, comment=None, created_by=None, empty_layer=None):
        """
        Initialize BuildHistory instance.

        :param created: 创建时间
        :type created: str (optional)

        :param comment: 备注
        :type comment: str (optional)

        :param created_by: 创建命令
        :type created_by: str (optional)

        :param empty_layer: 是否为空层
        :type empty_layer: bool (optional)
        """
        super().__init__()
        self.created = created
        self.comment = comment
        self.created_by = created_by
        self.empty_layer = empty_layer

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
        if self.created is not None:
            result['created'] = self.created
        if self.comment is not None:
            result['comment'] = self.comment
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.empty_layer is not None:
            result['emptyLayer'] = self.empty_layer
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BuildHistory

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('emptyLayer') is not None:
            self.empty_layer = m.get('emptyLayer')
        return self
