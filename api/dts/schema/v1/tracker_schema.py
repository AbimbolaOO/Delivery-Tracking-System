from marshmallow import Schema, fields, validate

from dts.utils.commons import Commons


class TrackerSchema(Schema):
    id = fields.UUID(dump_only=True)
    shipment_id = fields.UUID(dump_only=True)
    dispatcher_name = fields.Str(required=True)
    package_status = fields.Str(validate=validate.OneOf([*Commons.package_status()]))
    location = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        order = True
