from sqlalchemy import Column, Integer, String, Date

from app.config.database import Base


class Campaign(Base):
    __tablename__ = "campaigns"

    campaign_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(String(300), nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String(150), nullable=False)