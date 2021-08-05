from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel
from odoo.addons.datamodel.fields import NestedModel


class PartnerIndustry(Datamodel):
    _name = "partner.industry.info.param"

    ids = fields.List(fields.Integer())

class PartnerIndustryInfoResponse(Datamodel):
    _name = "partner.industry.info.response"

    id = fields.Integer(required=True, allow_nono=False)
    name = fields.String(required=True, allow_none=False)


class PartnerIndustryInfoResponseList(Datamodel):
    _name = "partner.industry.info.response.list"

    count = fields.Integer(required=False, allow_nono=False)
    rows = fields.List(NestedModel("partner.industry.info.response"))