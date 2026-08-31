from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    tag: str
    description: str
    technologies: list[str]
    features: list[str]
    demo_url: str
    github_url: str


class SkillGroup(BaseModel):
    category: str
    items: list[str]


class ExperienceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    role: str
    company: str
    location: str
    period: str
    type: str
    description: str
    highlights: list[str]


class ContactCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    subject: str = Field(min_length=3, max_length=200)
    message: str = Field(min_length=10, max_length=3000)


class ContactResponse(BaseModel):
    id: int
    message: str
    created_at: datetime
