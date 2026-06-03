"""
Request entity for ImportDataSrcResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class ImportDataSrcResponse(BceResponse):
    """
    ImportDataSrcResponse
    """

    def __init__(self, data_src_id=None):
        """
        Initialize ImportDataSrcResponse response.

        :param data_src_id: 数据源唯一ID
        :type data_src_id: str (optional)
        """
        super().__init__()
        self.data_src_id = data_src_id

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.data_src_id is not None:
            result['dataSrcId'] = self.data_src_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ImportDataSrcResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('dataSrcId') is not None:
            self.data_src_id = m.get('dataSrcId')
        return self
