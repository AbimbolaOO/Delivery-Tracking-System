from marshmallow import Schema, fields

from .tracker_schema import TrackerSchema


class ShipmentSchema(Schema):
    id = fields.UUID(dump_only=True)
    waybill_no = fields.Str(required=True)
    ecommerce_company = fields.Str(required=True)
    reciepient_name = fields.Str(required=True)
    reciepient_email = fields.Email(required=True)
    reciepient_phone = fields.Str(required=True)
    reciepient_address = fields.Str(required=True)
    is_completed = fields.Bool(dump_only=True)
    is_cancelled = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        order = True


class ShipmentWaybillNoSchema(Schema):
    waybill_no = fields.Str(required=True)

    class Meta:
        order = True


class ShipmentAndTrackingDataSchema(Schema):
    id = fields.UUID(dump_only=True)
    waybill_no = fields.Str(required=True)
    ecommerce_company = fields.Str(required=True)
    reciepient_name = fields.Str(required=True)
    reciepient_email = fields.Email(required=True)
    reciepient_phone = fields.Str(required=True)
    reciepient_address = fields.Str(required=True)
    tracker = fields.Nested(TrackerSchema, many=True)
    is_completed = fields.Bool(dump_only=True)
    is_cancelled = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        order = True
