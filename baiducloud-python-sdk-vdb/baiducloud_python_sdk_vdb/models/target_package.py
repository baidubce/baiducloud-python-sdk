"""
TargetPackage information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TargetPackage(AbstractModel):
    """
    TargetPackage
    """

    def __init__(self, target_milvus_kernel_version=None, target_package_version=None, upgrade_note=None):
        """
        Initialize TargetPackage instance.

        :param target_milvus_kernel_version:
        :type target_milvus_kernel_version: str (optional)

        :param target_package_version:
        :type target_package_version: str (optional)

        :param upgrade_note:
        :type upgrade_note: str (optional)
        """
        super().__init__()
        self.target_milvus_kernel_version = target_milvus_kernel_version
        self.target_package_version = target_package_version
        self.upgrade_note = upgrade_note

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
        if self.target_milvus_kernel_version is not None:
            result['targetMilvusKernelVersion'] = self.target_milvus_kernel_version
        if self.target_package_version is not None:
            result['targetPackageVersion'] = self.target_package_version
        if self.upgrade_note is not None:
            result['upgradeNote'] = self.upgrade_note
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TargetPackage

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('targetMilvusKernelVersion') is not None:
            self.target_milvus_kernel_version = m.get('targetMilvusKernelVersion')
        if m.get('targetPackageVersion') is not None:
            self.target_package_version = m.get('targetPackageVersion')
        if m.get('upgradeNote') is not None:
            self.upgrade_note = m.get('upgradeNote')
        return self
