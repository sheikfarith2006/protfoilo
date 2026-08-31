from datetime import datetime

from sqlalchemy import DateTime, Index, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Timestamped:
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class Project(Timestamped, Base):
    __tablename__ = 'projects'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(160), unique=True, nullable=False)
    tag: Mapped[str] = mapped_column(String(80), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    technologies: Mapped[str] = mapped_column(Text, nullable=False)  # pipe-separated for a small portfolio dataset
    features: Mapped[str] = mapped_column(Text, nullable=False)      # pipe-separated for a small portfolio dataset
    demo_url: Mapped[str] = mapped_column(String(500), default='#', nullable=False)
    github_url: Mapped[str] = mapped_column(String(500), default='#', nullable=False)


class Skill(Timestamped, Base):
    __tablename__ = 'skills'
    __table_args__ = (Index('ix_skills_category_name', 'category', 'name'),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)


class Experience(Timestamped, Base):
    __tablename__ = 'experience'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role: Mapped[str] = mapped_column(String(160), nullable=False)
    company: Mapped[str] = mapped_column(String(160), nullable=False)
    location: Mapped[str] = mapped_column(String(120), nullable=False)
    period: Mapped[str] = mapped_column(String(80), nullable=False)
    employment_type: Mapped[str] = mapped_column(String(80), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    highlights: Mapped[str] = mapped_column(Text, nullable=False)   # pipe-separated list
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)


class ContactMessage(Base):
    __tablename__ = 'contact_messages'
    __table_args__ = (Index('ix_contact_messages_created_at', 'created_at'), Index('ix_contact_messages_email', 'email'),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    subject: Mapped[str] = mapped_column(String(200), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
