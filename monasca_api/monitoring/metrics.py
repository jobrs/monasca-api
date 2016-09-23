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

METRICS_PUBLISH_TIME = "api.metrics.publish_time_ms"
""" time needed to publish a metric batch to Kafka """
METRICS_LIST_TIME = "api.metrics.list_time_ms"
METRICS_RETRIEVE_TIME = "api.metrics.retrieve_time_ms"
METRICS_DIMS_RETRIEVE_TIME = "api.metrics.dims_retrieve_time_ms"
METRICS_STATS_TIME = "api.metrics.stats_time_ms"
ALARMS_LIST_TIME = "api.alarms.list_time_ms"

KAFKA_PRODUCER_ERRORS = "kafka.producer.errors"