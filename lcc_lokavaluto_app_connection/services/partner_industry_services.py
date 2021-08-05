import logging
from odoo.addons.base_rest import restapi
from odoo.addons.base_rest_datamodel.restapi import Datamodel
from odoo.addons.base_rest.components.service import to_bool, to_int
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class PartnerIndustryService(Component):
    _inherit = "base.rest.service"
    _name = "partner_industry.service"
    _usage = "partner_industry"
    _collection = "lokavaluto.public.services"
    _description = """
        Partner Industry Services
        Access to the Partner Industry services is allowed to everyone
    """

    @restapi.method(
        [(["/", "/get"], "GET")],
        input_param=Datamodel("partner.industry.info.param"),
        output_param=Datamodel("partner.industry.info.response.list")
    )
    def get_partner_industry_info(self, partner_industry_info):
        """
        Get the complete list of partner indutries
        """
        ids = partner_industry_info.ids
        # Domain construction
        domain = [('active', '=', True)]
        if ids:
            domain.append(('id', 'in', ids))
        _logger.debug('DOMAIN = %s' % domain)
        # Partner indutries retrieval
        partner_indutries = self.env['res.partner.industry'].search(domain)
        _logger.debug('INDUSTRIES = %s' % partner_indutries)

        # Construction of the answer
        PartnerIndustryInfoResponseList = self.env.datamodels["partner.industry.info.response.list"]
        PartnerIndustryInfoResponse = self.env.datamodels["partner.industry.info.response"]
        res = PartnerIndustryInfoResponseList(count=len(partner_indutries), rows=[])        
        for industry in partner_indutries:
            industry_info = PartnerIndustryInfoResponse(id=industry.id, name = industry.name)
            _logger.debug('INDUSTRY INFO = %s' % industry_info)
            res.rows.append(industry_info)
        return res



    # def _validator_return_get(self):
    #     res = {
    #         "count": {"type": "integer", "required": True},
    #         "rows": {
    #             "type": "list",
    #             "required": True,
    #             "schema": {"type": "dict", "schema": self._return_partner_industry()},
    #         },
    #     }
    #     return res

    # def _return_partner_industry(self):
    #     res = {
    #         "id": {"type": "integer", "required": True, "nullable": False},
    #         "name": {"type": "string", "required": True, "empty": True},
    #     }
    #     return res

    # def _get_partner_industry_parser(self):
    #     parser = [
    #         'id',
    #         'name',
    #     ]
    #     return parser
