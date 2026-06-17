"""
Request entity for ImportAlarmTemplatesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcm.models.template import Template


class ImportAlarmTemplatesRequest(AbstractModel):
    """
    Request entity for ImportAlarmTemplatesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, overwrite, templates):
        """
        Initialize ImportAlarmTemplatesRequest request entity.

        :param overwrite: 若模板重名，是否覆盖（true覆盖/false跳过）
        :type overwrite: bool (required)

        :param templates: 报警模板列表
        :type templates: List[Template] (required)
        """
        super().__init__()
        self.overwrite = overwrite
        self.templates = templates

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
        if self.overwrite is not None:
            result['overwrite'] = self.overwrite
        if self.templates is not None:
            result['templates'] = [i.to_dict() for i in self.templates]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ImportAlarmTemplatesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')
        if m.get('templates') is not None:
            self.templates = [Template().from_dict(i) for i in m.get('templates')]
        return self
