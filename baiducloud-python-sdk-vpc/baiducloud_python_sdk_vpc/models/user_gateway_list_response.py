from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.cgw import Cgw


class UserGatewayListResponse(BceResponse):
    """This class represents the response for listing user gateways.
    
    Attributes:
        marker (str): The marker for pagination.
        is_truncated (bool): Indicates if the result is truncated.
        next_marker (str): The marker for next page.
        max_keys (int): The maximum number of keys returned.
        result (list): List of Cgw objects.
    """
    
    def __init__(self, marker=None, is_truncated=None, next_marker=None, max_keys=None, result=None):
        """Initialize the UserGatewayListResponse instance.
        
        Args:
            marker (str, optional): The marker for pagination. Defaults to None.
            is_truncated (bool, optional): Indicates if the result is truncated. Defaults to None.
            next_marker (str, optional): The marker for next page. Defaults to None.
            max_keys (int, optional): The maximum number of keys returned. Defaults to None.
            result (list, optional): List of Cgw objects. Defaults to None.
        """
        super().__init__()
        self.marker = marker
        self.is_truncated = is_truncated
        self.next_marker = next_marker
        self.max_keys = max_keys
        self.result = result

    def to_dict(self):
        """Convert the response object to a dictionary.
        
        Returns:
            dict: A dictionary containing the response data.
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.marker is not None:
            result['marker'] = self.marker
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        return result


    def from_dict(self, m):
        """Initialize the response object from a dictionary.
        
        Args:
            m (dict): A dictionary containing the response data.
            
        Returns:
            UserGatewayListResponse: The current instance.
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('result') is not None:
            self.result = [
            Cgw().from_dict(i)
            for i in m.get('result')
            ]
        return self