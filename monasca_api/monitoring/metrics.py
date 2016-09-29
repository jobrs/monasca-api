# Copyright 2016 FUJITSU LIMITED
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

METRICS_REJECTED_COUNT = "api.metrics_rejected"

METRICS_PUBLISH_TIME = "api.metrics_publish_time_ms"
METRICS_PUBLISH_ERRORS = "api.metrics_publish_errors"
""" time needed to publish a metric batch to Kafka """
METRICS_LIST_TIME = "api.metrics_list_time_ms"
METRICS_RETRIEVE_TIME = "api.metrics_retrieve_time_ms"
METRICS_DIMS_RETRIEVE_TIME = "api.metrics_dims_retrieve_time_ms"
METRICS_STATS_TIME = "api.metrics_stats_time_ms"
ALARMS_LIST_TIME = "api.alarms_list_time_ms"

INFLUXDB_QUERY_TIME = "influxdb.query_time_ms"
TSDB_ERRORS = "api.tsdb_errors"
CONFIGDB_ERRORS = "api.config_db_errors"
CONFIGDB_TIME = "api.config_db_time"
KAFKA_PRODUCER_ERRORS = "kafka.producer_errors"
