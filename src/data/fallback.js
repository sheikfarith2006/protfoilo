export const skills = [
  { category: 'Languages', items: ['Python', 'JavaScript', 'HTML', 'CSS', 'JSON'] },
  { category: 'Backend & APIs', items: ['FastAPI', 'Flask', 'Django', 'Django REST Framework', 'REST APIs'] },
  { category: 'AI & Retrieval', items: ['LangChain', 'RAG', 'LLMs', 'Embeddings', 'Semantic Search', 'ChromaDB'] },
  { category: 'Frontend & Mobile', items: ['React', 'React Native', 'Expo'] },
  { category: 'Data & Tools', items: ['MySQL', 'SQL', 'Git', 'GitHub', 'Postman', 'VS Code', 'Android Studio'] },
]

export const projects = [
  { id: 1, title: 'AI-Powered PDF Chatbot', tag: 'Generative AI', description: 'A document-grounded chatbot that turns uploaded PDFs into context-aware conversations using retrieval and embeddings.', technologies: ['Python', 'Flask', 'LangChain', 'RAG', 'ChromaDB', 'JavaScript'], features: ['PDF upload and text extraction', 'Semantic document retrieval', 'Context-aware answers', 'Persistent chat history'], demo_url: '#', github_url: '#' },
  { id: 2, title: 'Hospital Management System', tag: 'Mobile + Backend', description: 'A role-based mobile application for doctors, patients, and administrators to manage everyday clinic workflows.', technologies: ['React Native', 'Expo', 'Django REST Framework', 'MySQL'], features: ['Role-based authentication', 'Appointment booking', 'Medical records and prescriptions', 'Doctor availability'], demo_url: '#', github_url: '#' },
]

export const experience = [
  { id: 1, role: 'Full Stack Developer', company: 'Onstep Technologies', location: 'Chennai', period: 'Jun 2026 — Present', type: 'Full-time', description: 'Building a client-facing LangChain business chatbot with practical retrieval and conversational workflows.', highlights: ['Developing context-aware Q&A and document retrieval flows with LangChain and RAG.', 'Building Python/Flask REST APIs and integrating an HTML, CSS, and JavaScript chat interface.', 'Debugging prompt, context, API integration, and frontend/backend communication flows.'] },
  { id: 2, role: 'Full Stack Developer Intern', company: 'Onstep Technologies', location: 'Chennai', period: 'Mar 2026 — May 2026', type: 'Internship', description: 'Contributed to a clinic-management application and progressed into a full-time developer role.', highlights: ['Worked with React Native, Django REST Framework, MySQL, authentication, and CRUD workflows.', 'Supported doctor availability, appointments, medical records, prescriptions, and laboratory reports.', 'Received the Best Intern Award at Onstep Technologies.'] },
]
