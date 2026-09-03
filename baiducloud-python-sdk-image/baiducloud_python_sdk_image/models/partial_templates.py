"""
PartialTemplates information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_image.models.partial_human_options import PartialHumanOptions

from baiducloud_python_sdk_image.models.partial_human_options import PartialHumanOptions

from baiducloud_python_sdk_image.models.partial_human_options import PartialHumanOptions

from baiducloud_python_sdk_image.models.partial_human_options import PartialHumanOptions

from baiducloud_python_sdk_image.models.partial_human_options import PartialHumanOptions


class PartialTemplates(AbstractModel):
    """
    PartialTemplates
    """

    def __init__(self, male_old=None, female_old=None, female_young=None, male_young=None, child=None):
        """
        Initialize PartialTemplates instance.

        :param male_old: male_old attribute
        :type male_old: PartialHumanOptions (optional)

        :param female_old: female_old attribute
        :type female_old: PartialHumanOptions (optional)

        :param female_young: female_young attribute
        :type female_young: PartialHumanOptions (optional)

        :param male_young: male_young attribute
        :type male_young: PartialHumanOptions (optional)

        :param child: child attribute
        :type child: PartialHumanOptions (optional)
        """
        super().__init__()
        self.male_old = male_old
        self.female_old = female_old
        self.female_young = female_young
        self.male_young = male_young
        self.child = child

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
        if self.male_old is not None:
            result['male_old'] = self.male_old.to_dict()
        if self.female_old is not None:
            result['female_old'] = self.female_old.to_dict()
        if self.female_young is not None:
            result['female_young'] = self.female_young.to_dict()
        if self.male_young is not None:
            result['male_young'] = self.male_young.to_dict()
        if self.child is not None:
            result['child'] = self.child.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PartialTemplates

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('male_old') is not None:
            self.male_old = PartialHumanOptions().from_dict(m.get('male_old'))
        if m.get('female_old') is not None:
            self.female_old = PartialHumanOptions().from_dict(m.get('female_old'))
        if m.get('female_young') is not None:
            self.female_young = PartialHumanOptions().from_dict(m.get('female_young'))
        if m.get('male_young') is not None:
            self.male_young = PartialHumanOptions().from_dict(m.get('male_young'))
        if m.get('child') is not None:
            self.child = PartialHumanOptions().from_dict(m.get('child'))
        return self
