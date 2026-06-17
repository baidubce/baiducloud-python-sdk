"""
Request entity for DescribeDataSrcRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeDataSrcRequest(AbstractModel):
    """
    Request entity for DescribeDataSrcRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, data_src_id):
        """
        Initialize DescribeDataSrcRequest request entity.

        :param instance_id: RapidFS 实例ID
        :type instance_id: str (required)

        :param data_src_id: 待修改的数据源 ID
        :type data_src_id: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.data_src_id = data_src_id

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.data_src_id is not None:
            result['dataSrcId'] = self.data_src_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeDataSrcRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('dataSrcId') is not None:
            self.data_src_id = m.get('dataSrcId')
        return self
