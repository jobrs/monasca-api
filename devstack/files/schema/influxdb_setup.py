#!/usr/bin/env python

#
# (C) Copyright 2015 Hewlett Packard Enterprise Development Company LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""A simple script to setup influxdb user and roles. At some point this should
   become a more full featured module.  Also this assumes that none of the
   python based influxdb clients are available on this system.
"""

ADMIN = 'root'
ADMIN_PASS = 'root'
DBNAME = 'mon'
USERS = {}
USERS['mon_api'] = 'password'
USERS['mon_persister'] = 'password'

URL = 'http://127.0.0.1:8086'

SHARDSPACE_NAME = 'persister_all'
REPLICATION = 1
RETENTION = '90d'

import json
import sys
import time
import urllib
import urllib2


def influxdb_get(uri, query, db=None):
    """Runs a query via HTTP GET and returns the response as a Python list."""

    getparams = {"q": query}
    if db:
        getparams['db'] = db

    try:
        params = urllib.urlencode(getparams)
        uri = "{}&{}".format(uri,params)
        req = urllib2.urlopen(uri)
        json_value = json.loads(req.read())

        if (len(json_value['results'][0]) > 0 and
           'values' in json_value['results'][0]['series'][0]):
            return json_value['results'][0]['series'][0]['values']
        else:
            return []

    except KeyError:
        print "Query returned a non-successful result: {0}".format(json_value['results'])
        sys.exit(1)


def main(argv=None):
    """If necessary, create the database, retention policy, and users"""
    auth_str = '?u=%s&p=%s' % (ADMIN, ADMIN_PASS)
    api_uri = "{0}/query{1}".format(URL, auth_str)

#    List current databases
    dbs = influxdb_get(uri=api_uri, query="SHOW DATABASES")
    if [DBNAME] not in dbs:
        print "Creating database '{}'".format(DBNAME)
        influxdb_get(uri=api_uri, query="CREATE DATABASE {0}".format(DBNAME))
        print "...created!"

#   Check retention policy
    policies = influxdb_get(uri=api_uri,
                            query="SHOW RETENTION POLICIES {0}".format(DBNAME))
    if not any(pol[0] == SHARDSPACE_NAME for pol in policies):
        # Set retention policy
        policy = "CREATE RETENTION POLICY {0} ON {1} DURATION {2} REPLICATION {3} DEFAULT".format(SHARDSPACE_NAME,
                                                                                          DBNAME,
                                                                                          RETENTION,
                                                                                          REPLICATION)
        influxdb_get(uri=api_uri, db=DBNAME, query=policy)

#   Create the users
    users = influxdb_get(uri=api_uri, query="SHOW USERS", db=DBNAME)
    for name, password in USERS.iteritems():
        if not any(user[0] == name for user in users):
            influxdb_get(uri=api_uri,
                         query=unicode("CREATE USER {0} WITH PASSWORD '{1}'".format(name, password)),
                         db=DBNAME)

if __name__ == "__main__":
    sys.exit(main())
