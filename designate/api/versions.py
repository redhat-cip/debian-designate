# Copyright 2012 Hewlett-Packard Development Company, L.P. All Rights Reserved.
#
# Author: Kiall Mac Innes <kiall@hp.com>
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
import flask
from oslo.config import cfg


def factory(global_config, **local_conf):
    app = flask.Flask('designate.api.versions')

    versions = []

    if cfg.CONF['service:api'].enable_api_v1:
        versions.append({
            "id": "v1",
            "status": "CURRENT"
        })

    if cfg.CONF['service:api'].enable_api_v2:
        versions.append({
            "id": "v2",
            "status": "EXPERIMENTAL"
        })

    @app.route('/', methods=['GET'])
    def version_list():
        return flask.jsonify({
            "versions": versions
        })

    return app
