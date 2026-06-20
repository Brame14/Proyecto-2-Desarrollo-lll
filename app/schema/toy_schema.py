from pydantic import BaseModel


class ToyBase(BaseModel):
    name: str
    category: str
    condition: str
    donor_id: int


class ToyCreate(ToyBase):
    pass


class ToyUpdate(ToyBase):
    pass


class ToyResponse(ToyBase):
    toy_id: int

    class Config:
        from_attributes = True