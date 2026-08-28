"""
QusFigure information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.fig_location import FigLocation


class QusFigure(AbstractModel):
    """
    QusFigure
    """

    def __init__(self, fig_location=None):
        """
        Initialize QusFigure instance.

        :param fig_location: fig_location attribute
        :type fig_location: FigLocation (optional)
        """
        super().__init__()
        self.fig_location = fig_location

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
        if self.fig_location is not None:
            result['fig_location'] = self.fig_location.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QusFigure

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fig_location') is not None:
            self.fig_location = FigLocation().from_dict(m.get('fig_location'))
        return self
