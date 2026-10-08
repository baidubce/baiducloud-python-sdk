"""
ClusterType information
"""


class ClusterType:
    """
    Enum class for ClusterType
    Allowed values: CLUSTER, MASTER_SLAVE
    """

    CLUSTER = 'cluster'
    MASTER_SLAVE = 'master_slave'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['cluster', 'master_slave']
        return value in valid_values
