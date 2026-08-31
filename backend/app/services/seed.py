from sqlalchemy.orm import Session

from app.models import Experience, Project, Skill

PROJECTS = [
    {'title': 'AI-Powered PDF Chatbot', 'tag': 'Generative AI', 'description': 'A document-grounded chatbot that turns uploaded PDFs into context-aware conversations using retrieval and embeddings.', 'technologies': 'Python|Flask|LangChain|RAG|ChromaDB|JavaScript', 'features': 'PDF upload and text extraction|Semantic document retrieval|Context-aware answers|Persistent chat history'},
    {'title': 'Hospital Management System', 'tag': 'Mobile + Backend', 'description': 'A role-based mobile application for doctors, patients, and administrators to manage everyday clinic workflows.', 'technologies': 'React Native|Expo|Django REST Framework|MySQL', 'features': 'Role-based authentication|Appointment booking|Medical records and prescriptions|Doctor availability'},
]
SKILLS = {
    'Languages': ['Python', 'JavaScript', 'HTML', 'CSS', 'JSON'],
    'Backend & APIs': ['FastAPI', 'Flask', 'Django', 'Django REST Framework', 'REST APIs'],
    'AI & Retrieval': ['LangChain', 'RAG', 'LLMs', 'Embeddings', 'Semantic Search', 'ChromaDB'],
    'Frontend & Mobile': ['React', 'React Native', 'Expo'],
    'Data & Tools': ['MySQL', 'SQL', 'Git', 'GitHub', 'Postman', 'VS Code', 'Android Studio'],
}
EXPERIENCE = [
    {'role': 'Full Stack Developer', 'company': 'Onstep Technologies', 'location': 'Chennai', 'period': 'Jun 2026 — Present', 'employment_type': 'Full-time', 'description': 'Building a client-facing LangChain business chatbot with practical retrieval and conversational workflows.', 'highlights': 'Developing context-aware Q&A and document retrieval flows with LangChain and RAG.|Building Python/Flask REST APIs and integrating an HTML, CSS, and JavaScript chat interface.|Debugging prompt, context, API integration, and frontend/backend communication flows.'},
    {'role': 'Full Stack Developer Intern', 'company': 'Onstep Technologies', 'location': 'Chennai', 'period': 'Mar 2026 — May 2026', 'employment_type': 'Internship', 'description': 'Contributed to a clinic-management application and progressed into a full-time developer role.', 'highlights': 'Worked with React Native, Django REST Framework, MySQL, authentication, and CRUD workflows.|Supported doctor availability, appointments, medical records, prescriptions, and laboratory reports.|Received the Best Intern Award at Onstep Technologies.'},
]


def seed_portfolio_data(db: Session) -> None:
    if not db.query(Project).first():
        db.add_all([Project(**project) for project in PROJECTS])
    if not db.query(Skill).first():
        db.add_all([Skill(category=category, name=name, display_order=index) for category, names in SKILLS.items() for index, name in enumerate(names)])
    if not db.query(Experience).first():
        db.add_all([Experience(**entry, display_order=index) for index, entry in enumerate(EXPERIENCE)])
    db.commit()
