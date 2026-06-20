from app.service.system_service import SystemService

class SystemController:

    def __init__(self):
        self.service = SystemService()

    # DONADORES


    def register_donor(self, donor):
        self.service.register_donor(donor)

    def get_donors(self):
        return self.service.get_donors()


    # JUGUETES


    def register_toy(self, toy):
        self.service.register_toy(toy)

    def get_toys(self):
        return self.service.get_toys()


    # BENEFICIARIOS


    def register_beneficiary(self, beneficiary):
        self.service.register_beneficiary(beneficiary)

    def get_beneficiaries(self):
        return self.service.get_beneficiaries()


    # CAMPAÑAS


    def register_campaign(self, campaign):
        self.service.register_campaign(campaign)

    def get_campaigns(self):
        return self.service.get_campaigns()


    # ENTREGAS


    def register_delivery(self, delivery):
        return self.service.register_delivery(delivery)

    def get_deliveries(self):
        return self.service.get_deliveries()


    # REPORTES


    def total_deliveries(self):
        return self.service.total_deliveries()

    def available_toys(self):
            return self.service.available_toys()