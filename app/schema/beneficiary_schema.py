from pydantic import BaseModel


class BeneficiaryBase(BaseModel):
    name: str
    age: int
    gender: str
    community: str


class BeneficiaryCreate(BeneficiaryBase):
    pass


class BeneficiaryUpdate(BeneficiaryBase):
    pass


class BeneficiaryResponse(BeneficiaryBase):
    beneficiary_id: int

    class Config:
        from_attributes = True