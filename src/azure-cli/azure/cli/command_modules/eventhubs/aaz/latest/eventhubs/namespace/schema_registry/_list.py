# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "eventhubs namespace schema-registry list",
)
class List(AAZCommand):
    """List all the Schema Groups in a Namespace.
    """

    _aaz_info = {
        "version": "2022-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.eventhub/namespaces/{}/schemagroups", "2022-01-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.namespace_name = AAZStrArg(
            options=["--namespace-name"],
            help="The Namespace name",
            required=True,
            fmt=AAZStrArgFormat(
                max_length=50,
                min_length=6,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.skip = AAZIntArg(
            options=["--skip"],
            help="Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.",
            fmt=AAZIntArgFormat(
                maximum=1000,
                minimum=0,
            ),
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="May be used to limit the number of results to the most recent N usageDetails.",
            fmt=AAZIntArgFormat(
                maximum=1000,
                minimum=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SchemaRegistryListByNamespace(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class SchemaRegistryListByNamespace(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/namespaces/{namespaceName}/schemagroups",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "namespaceName", self.ctx.args.namespace_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$skip", self.ctx.args.skip,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2022-01-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.created_at_utc = AAZStrType(
                serialized_name="createdAtUtc",
                flags={"read_only": True},
            )
            properties.e_tag = AAZStrType(
                serialized_name="eTag",
                flags={"read_only": True},
            )
            properties.group_properties = AAZDictType(
                serialized_name="groupProperties",
            )
            properties.schema_compatibility = AAZStrType(
                serialized_name="schemaCompatibility",
            )
            properties.schema_type = AAZStrType(
                serialized_name="schemaType",
            )
            properties.updated_at_utc = AAZStrType(
                serialized_name="updatedAtUtc",
                flags={"read_only": True},
            )

            group_properties = cls._schema_on_200.value.Element.properties.group_properties
            group_properties.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


__all__ = ["List"]
