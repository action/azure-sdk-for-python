# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataLakeStoreAccountProperties(Model):
    """Data Lake Store account properties information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: the status of the Data Lake Store account while
     being provisioned. Possible values include: 'Failed', 'Creating',
     'Running', 'Succeeded', 'Patching', 'Suspending', 'Resuming',
     'Deleting', 'Deleted'
    :vartype provisioning_state: str or :class:`DataLakeStoreAccountStatus
     <azure.mgmt.datalake.store.account.models.DataLakeStoreAccountStatus>`
    :ivar state: the status of the Data Lake Store account after provisioning
     has completed. Possible values include: 'active', 'suspended'
    :vartype state: str or :class:`DataLakeStoreAccountState
     <azure.mgmt.datalake.store.account.models.DataLakeStoreAccountState>`
    :ivar creation_time: the account creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: the account last modified time.
    :vartype last_modified_time: datetime
    :param endpoint: the gateway host.
    :type endpoint: str
    :param default_group: the default owner group for all new folders and
     files created in the Data Lake Store account.
    :type default_group: str
    """ 

    _validation = {
        'provisioning_state': {'readonly': True},
        'state': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'DataLakeStoreAccountStatus'},
        'state': {'key': 'state', 'type': 'DataLakeStoreAccountState'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'default_group': {'key': 'defaultGroup', 'type': 'str'},
    }

    def __init__(self, endpoint=None, default_group=None):
        self.provisioning_state = None
        self.state = None
        self.creation_time = None
        self.last_modified_time = None
        self.endpoint = endpoint
        self.default_group = default_group
