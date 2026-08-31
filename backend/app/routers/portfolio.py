from collections import OrderedDict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ContactMessage, Experience, Project, Skill
from app.schemas import ContactCreate, ContactResponse, ExperienceResponse, ProjectResponse, SkillGroup

router = APIRouter(prefix='/api', tags=['portfolio'])


@router.get('/projects', response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).order_by(Project.id).all()
    return [{**project.__dict__, 'technologies': project.technologies.split('|'), 'features': project.features.split('|')} for project in projects]


@router.get('/skills', response_model=list[SkillGroup])
def get_skills(db: Session = Depends(get_db)):
    grouped: OrderedDict[str, list[str]] = OrderedDict()
    for skill in db.query(Skill).order_by(Skill.id, Skill.display_order).all():
        grouped.setdefault(skill.category, []).append(skill.name)
    return [{'category': category, 'items': items} for category, items in grouped.items()]


@router.get('/experience', response_model=list[ExperienceResponse])
def get_experience(db: Session = Depends(get_db)):
    entries = db.query(Experience).order_by(Experience.display_order).all()
    return [{**entry.__dict__, 'type': entry.employment_type, 'highlights': entry.highlights.split('|')} for entry in entries]


@router.post('/contact', response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
def create_contact(payload: ContactCreate, db: Session = Depends(get_db)):
    message = ContactMessage(**payload.model_dump())
    try:
        db.add(message)
        db.commit()
        db.refresh(message)
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=500, detail='Unable to save your message right now.') from error
    return ContactResponse(id=message.id, message='Message saved successfully.', created_at=message.created_at)
