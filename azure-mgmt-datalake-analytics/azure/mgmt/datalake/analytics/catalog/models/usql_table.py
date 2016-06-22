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

from .catalog_item import CatalogItem


class USqlTable(CatalogItem):
    """A Data Lake Analytics catalog U-SQL table item.

    :param compute_account_name: the name of the Data Lake Analytics account.
    :type compute_account_name: str
    :param version: the version of the catalog item.
    :type version: str
    :param database_name: the name of the database.
    :type database_name: str
    :param schema_name: the name of the schema associated with this table and
     database.
    :type schema_name: str
    :param name: the name of the table.
    :type name: str
    :param column_list: the list of columns in this table
    :type column_list: list of :class:`USqlTableColumn
     <azure.mgmt.datalake.analytics.catalog.models.USqlTableColumn>`
    :param index_list: the list of indices in this table
    :type index_list: list of :class:`USqlIndex
     <azure.mgmt.datalake.analytics.catalog.models.USqlIndex>`
    :param partition_key_list: the list of partition keys in the table
    :type partition_key_list: list of str
    :param external_table: the external table associated with the table.
    :type external_table: :class:`ExternalTable
     <azure.mgmt.datalake.analytics.catalog.models.ExternalTable>`
    :param distribution_info: the distributions info of the table
    :type distribution_info: :class:`USqlDistributionInfo
     <azure.mgmt.datalake.analytics.catalog.models.USqlDistributionInfo>`
    """ 

    _attribute_map = {
        'compute_account_name': {'key': 'computeAccountName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'schema_name': {'key': 'schemaName', 'type': 'str'},
        'name': {'key': 'tableName', 'type': 'str'},
        'column_list': {'key': 'columnList', 'type': '[USqlTableColumn]'},
        'index_list': {'key': 'indexList', 'type': '[USqlIndex]'},
        'partition_key_list': {'key': 'partitionKeyList', 'type': '[str]'},
        'external_table': {'key': 'externalTable', 'type': 'ExternalTable'},
        'distribution_info': {'key': 'distributionInfo', 'type': 'USqlDistributionInfo'},
    }

    def __init__(self, compute_account_name=None, version=None, database_name=None, schema_name=None, name=None, column_list=None, index_list=None, partition_key_list=None, external_table=None, distribution_info=None):
        super(USqlTable, self).__init__(compute_account_name=compute_account_name, version=version)
        self.database_name = database_name
        self.schema_name = schema_name
        self.name = name
        self.column_list = column_list
        self.index_list = index_list
        self.partition_key_list = partition_key_list
        self.external_table = external_table
        self.distribution_info = distribution_info
