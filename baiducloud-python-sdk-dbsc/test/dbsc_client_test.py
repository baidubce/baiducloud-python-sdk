import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_dbsc.api.dbsc_client import DbscClient
from baiducloud_python_sdk_dbsc import models as dbsc_models


class DbscClientTest(unittest.TestCase):
    """DbscClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''

        # ==== AK/SK 鉴权 ====
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        self.client = DbscClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_check_mysql_rate_limit_support(self):
        self.client.check_mysql_rate_limit_support(dbsc_models.CheckMysqlRateLimitSupportRequest())

    def test_create_mysql_rate_limit_task(self):
        self.client.create_mysql_rate_limit_task(dbsc_models.CreateMysqlRateLimitTaskRequest())

    def test_create_redis_big_key_analysis_task(self):
        self.client.create_redis_big_key_analysis_task(dbsc_models.CreateRedisBigKeyAnalysisTaskRequest())

    def test_delete_mysql_rate_limit_task(self):
        self.client.delete_mysql_rate_limit_task(dbsc_models.DeleteMysqlRateLimitTaskRequest())

    def test_delete_redis_big_key_analysis_task(self):
        self.client.delete_redis_big_key_analysis_task(dbsc_models.DeleteRedisBigKeyAnalysisTaskRequest())

    def test_get_mongodb_collection_indexes(self):
        self.client.get_mongodb_collection_indexes(dbsc_models.GetMongodbCollectionIndexesRequest())

    def test_get_mongodb_collection_space(self):
        self.client.get_mongodb_collection_space(dbsc_models.GetMongodbCollectionSpaceRequest())

    def test_get_mongodb_collection_space_trend(self):
        self.client.get_mongodb_collection_space_trend(dbsc_models.GetMongodbCollectionSpaceTrendRequest())

    def test_get_mongodb_database_space(self):
        self.client.get_mongodb_database_space(dbsc_models.GetMongodbDatabaseSpaceRequest())

    def test_get_mongodb_database_space_trend(self):
        self.client.get_mongodb_database_space_trend(dbsc_models.GetMongodbDatabaseSpaceTrendRequest())

    def test_get_mongodb_slow_log_time_distribution(self):
        self.client.get_mongodb_slow_log_time_distribution(dbsc_models.GetMongodbSlowLogTimeDistributionRequest())

    def test_get_mongodb_slow_log_trend(self):
        self.client.get_mongodb_slow_log_trend(dbsc_models.GetMongodbSlowLogTrendRequest())

    def test_get_mongodb_slow_query_template(self):
        self.client.get_mongodb_slow_query_template(dbsc_models.GetMongodbSlowQueryTemplateRequest())

    def test_get_mongodb_space_summary(self):
        self.client.get_mongodb_space_summary(dbsc_models.GetMongodbSpaceSummaryRequest())

    def test_get_mysql_active_sessions(self):
        self.client.get_mysql_active_sessions(dbsc_models.GetMysqlActiveSessionsRequest())

    def test_get_mysql_database_space(self):
        self.client.get_mysql_database_space(dbsc_models.GetMysqlDatabaseSpaceRequest())

    def test_get_mysql_deadlock_info(self):
        self.client.get_mysql_deadlock_info(dbsc_models.GetMysqlDeadlockInfoRequest())

    def test_get_mysql_kill_session_history(self):
        self.client.get_mysql_kill_session_history(dbsc_models.GetMysqlKillSessionHistoryRequest())

    def test_get_mysql_rate_limit_task_detail(self):
        self.client.get_mysql_rate_limit_task_detail(dbsc_models.GetMysqlRateLimitTaskDetailRequest())

    def test_get_mysql_slow_log_template(self):
        self.client.get_mysql_slow_log_template(dbsc_models.GetMysqlSlowLogTemplateRequest())

    def test_get_mysql_slow_log_time_distribution(self):
        self.client.get_mysql_slow_log_time_distribution(dbsc_models.GetMysqlSlowLogTimeDistributionRequest())

    def test_get_mysql_slow_log_trend(self):
        self.client.get_mysql_slow_log_trend(dbsc_models.GetMysqlSlowLogTrendRequest())

    def test_get_mysql_space_summary(self):
        self.client.get_mysql_space_summary(dbsc_models.GetMysqlSpaceSummaryRequest())

    def test_get_mysql_table_indexes(self):
        self.client.get_mysql_table_indexes(dbsc_models.GetMysqlTableIndexesRequest())

    def test_get_mysql_table_space(self):
        self.client.get_mysql_table_space(dbsc_models.GetMysqlTableSpaceRequest())

    def test_get_pegadb_slow_log_template(self):
        self.client.get_pegadb_slow_log_template(dbsc_models.GetPegadbSlowLogTemplateRequest())

    def test_get_pegadb_slow_log_time_distribution(self):
        self.client.get_pegadb_slow_log_time_distribution(dbsc_models.GetPegadbSlowLogTimeDistributionRequest())

    def test_get_pegadb_slow_log_trend(self):
        self.client.get_pegadb_slow_log_trend(dbsc_models.GetPegadbSlowLogTrendRequest())

    def test_get_postgresql_slow_log_template(self):
        self.client.get_postgresql_slow_log_template(dbsc_models.GetPostgresqlSlowLogTemplateRequest())

    def test_get_postgresql_slow_log_time_distribution(self):
        self.client.get_postgresql_slow_log_time_distribution(
            dbsc_models.GetPostgresqlSlowLogTimeDistributionRequest()
        )

    def test_get_postgresql_slow_log_trend(self):
        self.client.get_postgresql_slow_log_trend(dbsc_models.GetPostgresqlSlowLogTrendRequest())

    def test_get_redis_big_key_analysis_result(self):
        self.client.get_redis_big_key_analysis_result(dbsc_models.GetRedisBigKeyAnalysisResultRequest())

    def test_get_redis_slow_log_template(self):
        self.client.get_redis_slow_log_template(dbsc_models.GetRedisSlowLogTemplateRequest())

    def test_get_redis_slow_log_time_distribution(self):
        self.client.get_redis_slow_log_time_distribution(dbsc_models.GetRedisSlowLogTimeDistributionRequest())

    def test_get_redis_slow_log_trend(self):
        self.client.get_redis_slow_log_trend(dbsc_models.GetRedisSlowLogTrendRequest())

    def test_kill_mysql_session(self):
        self.client.kill_mysql_session(dbsc_models.KillMysqlSessionRequest())

    def test_list_mongodb_slow_logs(self):
        self.client.list_mongodb_slow_logs(dbsc_models.ListMongodbSlowLogsRequest())

    def test_list_mysql_rate_limit_tasks(self):
        self.client.list_mysql_rate_limit_tasks(dbsc_models.ListMysqlRateLimitTasksRequest())

    def test_list_mysql_slow_logs(self):
        self.client.list_mysql_slow_logs(dbsc_models.ListMysqlSlowLogsRequest())

    def test_list_pegadb_slow_logs(self):
        self.client.list_pegadb_slow_logs(dbsc_models.ListPegadbSlowLogsRequest())

    def test_list_postgresql_slow_logs(self):
        self.client.list_postgresql_slow_logs(dbsc_models.ListPostgresqlSlowLogsRequest())

    def test_list_redis_big_key_analysis_tasks(self):
        self.client.list_redis_big_key_analysis_tasks(dbsc_models.ListRedisBigKeyAnalysisTasksRequest())

    def test_list_redis_slow_logs(self):
        self.client.list_redis_slow_logs(dbsc_models.ListRedisSlowLogsRequest())

    def test_start_stop_mysql_instance_flow_limiting_task(self):
        self.client.start_stop_mysql_instance_flow_limiting_task(
            dbsc_models.StartStopMysqlInstanceFlowLimitingTaskRequest()
        )

    def test_update_mysql_rate_limit_task(self):
        self.client.update_mysql_rate_limit_task(dbsc_models.UpdateMysqlRateLimitTaskRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(DbscClientTest("test_check_mysql_rate_limit_support"))
    suite.addTest(DbscClientTest("test_create_mysql_rate_limit_task"))
    suite.addTest(DbscClientTest("test_create_redis_big_key_analysis_task"))
    suite.addTest(DbscClientTest("test_delete_mysql_rate_limit_task"))
    suite.addTest(DbscClientTest("test_delete_redis_big_key_analysis_task"))
    suite.addTest(DbscClientTest("test_get_mongodb_collection_indexes"))
    suite.addTest(DbscClientTest("test_get_mongodb_collection_space"))
    suite.addTest(DbscClientTest("test_get_mongodb_collection_space_trend"))
    suite.addTest(DbscClientTest("test_get_mongodb_database_space"))
    suite.addTest(DbscClientTest("test_get_mongodb_database_space_trend"))
    suite.addTest(DbscClientTest("test_get_mongodb_slow_log_time_distribution"))
    suite.addTest(DbscClientTest("test_get_mongodb_slow_log_trend"))
    suite.addTest(DbscClientTest("test_get_mongodb_slow_query_template"))
    suite.addTest(DbscClientTest("test_get_mongodb_space_summary"))
    suite.addTest(DbscClientTest("test_get_mysql_active_sessions"))
    suite.addTest(DbscClientTest("test_get_mysql_database_space"))
    suite.addTest(DbscClientTest("test_get_mysql_deadlock_info"))
    suite.addTest(DbscClientTest("test_get_mysql_kill_session_history"))
    suite.addTest(DbscClientTest("test_get_mysql_rate_limit_task_detail"))
    suite.addTest(DbscClientTest("test_get_mysql_slow_log_template"))
    suite.addTest(DbscClientTest("test_get_mysql_slow_log_time_distribution"))
    suite.addTest(DbscClientTest("test_get_mysql_slow_log_trend"))
    suite.addTest(DbscClientTest("test_get_mysql_space_summary"))
    suite.addTest(DbscClientTest("test_get_mysql_table_indexes"))
    suite.addTest(DbscClientTest("test_get_mysql_table_space"))
    suite.addTest(DbscClientTest("test_get_pegadb_slow_log_template"))
    suite.addTest(DbscClientTest("test_get_pegadb_slow_log_time_distribution"))
    suite.addTest(DbscClientTest("test_get_pegadb_slow_log_trend"))
    suite.addTest(DbscClientTest("test_get_postgresql_slow_log_template"))
    suite.addTest(DbscClientTest("test_get_postgresql_slow_log_time_distribution"))
    suite.addTest(DbscClientTest("test_get_postgresql_slow_log_trend"))
    suite.addTest(DbscClientTest("test_get_redis_big_key_analysis_result"))
    suite.addTest(DbscClientTest("test_get_redis_slow_log_template"))
    suite.addTest(DbscClientTest("test_get_redis_slow_log_time_distribution"))
    suite.addTest(DbscClientTest("test_get_redis_slow_log_trend"))
    suite.addTest(DbscClientTest("test_kill_mysql_session"))
    suite.addTest(DbscClientTest("test_list_mongodb_slow_logs"))
    suite.addTest(DbscClientTest("test_list_mysql_rate_limit_tasks"))
    suite.addTest(DbscClientTest("test_list_mysql_slow_logs"))
    suite.addTest(DbscClientTest("test_list_pegadb_slow_logs"))
    suite.addTest(DbscClientTest("test_list_postgresql_slow_logs"))
    suite.addTest(DbscClientTest("test_list_redis_big_key_analysis_tasks"))
    suite.addTest(DbscClientTest("test_list_redis_slow_logs"))
    suite.addTest(DbscClientTest("test_start_stop_mysql_instance_flow_limiting_task"))
    suite.addTest(DbscClientTest("test_update_mysql_rate_limit_task"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
