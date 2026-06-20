from pydantic import BaseModel, EmailStr


class DonorBase(BaseModel):
    name: str
    phone: str
    email: EmailStr


class DonorCreate(DonorBase):
    pass


class DonorUpdate(DonorBase):
    pass


class DonorResponse(DonorBase):
    donor_id: int

    class Config:
        from_attributes = True