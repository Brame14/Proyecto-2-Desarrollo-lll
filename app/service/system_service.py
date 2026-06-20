from app.repository.donor_repository import DonorRepository
from app.repository.toy_repository import ToyRepository
from app.repository.beneficiary_repository import BeneficiaryRepository
from app.repository.campaign_repository import CampaignRepository
from app.repository.delivery_repository import DeliveryRepository


class SystemService:

    def __init__(self):

        self.donor_repository = DonorRepository()
        self.toy_repository = ToyRepository()
        self.beneficiary_repository = BeneficiaryRepository()
        self.campaign_repository = CampaignRepository()
        self.delivery_repository = DeliveryRepository()

    # =========================
    # DONADORES
    # =========================

    def register_donor(self, donor):
        self.donor_repository.save_donor(donor)

    def get_donors(self):
        return self.donor_repository.get_all_donors()

    # =========================
    # JUGUETES
    # =========================

    def register_toy(self, toy):
        self.toy_repository.save_toy(toy)

    def get_toys(self):
        return self.toy_repository.get_all_toys()

    # =========================
    # BENEFICIARIOS
    # =========================

    def register_beneficiary(self, beneficiary):
        self.beneficiary_repository.save_beneficiary(beneficiary)

    def get_beneficiaries(self):
        return self.beneficiary_repository.get_all_beneficiaries()

    # =========================
    # CAMPAÑAS
    # =========================

    def register_campaign(self, campaign):
        self.campaign_repository.save_campaign(campaign)

    def get_campaigns(self):
        return self.campaign_repository.get_all_campaigns()

    # =========================
    # ENTREGAS
    # =========================

    def register_delivery(self, delivery):

        toys = self.toy_repository.get_all_toys()

        toy_found = False

        for toy in toys:

            if toy["name"] == delivery.toy_name:

                toy_found = True

                if toy["quantity"] <= 0:
                    return False

                toy["quantity"] -= 1

        if not toy_found:
            return False

        self.toy_repository.update_toys(toys)

        self.delivery_repository.save_delivery(delivery)

        return True

    def get_deliveries(self):
        return self.delivery_repository.get_all_deliveries()

    # =========================
    # REPORTES
    # =========================

    def total_deliveries(self):
        deliveries = self.delivery_repository.get_all_deliveries()
        return len(deliveries)

    def available_toys(self):

        toys = self.toy_repository.get_all_toys()

        available = []

        for toy in toys:
            if toy["quantity"] > 0:
                available.append(toy)

        return available