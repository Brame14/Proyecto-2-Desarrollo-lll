from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base


class Delivery(Base):
    __tablename__ = "deliveries"

    delivery_id = Column(Integer, primary_key=True, index=True)

    beneficiary_id = Column(
        Integer,
        ForeignKey("beneficiaries.beneficiary_id"),
        nullable=False
    )

    toy_id = Column(
        Integer,
        ForeignKey("toys.toy_id"),
        nullable=False
    )

    campaign_id = Column(
        Integer,
        ForeignKey("campaigns.campaign_id"),
        nullable=False
    )

    delivery_date = Column(Date, nullable=False)

    beneficiary = relationship("Beneficiary")
    toy = relationship("Toy")
    campaign = relationship("Campaign")