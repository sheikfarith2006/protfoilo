import { Download, ExternalLink, FileText } from 'lucide-react'
import SectionHeader from './SectionHeader'

const resumePath = '/resume/A-Sheik-Farith-Resume.md'

export default function Resume() {
  return <section id="resume" className="section shell resume-section"><SectionHeader number="06" eyebrow="Resume" title={<>The concise <em>version of my story.</em></>} /><div className="resume-card reveal"><div className="resume-mark"><FileText size={25} /></div><div><p className="resume-title">A. Sheik Farith · Full Stack Developer</p><p>Experience, technical skills, projects, and education—based on the available resume information.</p></div><div className="resume-actions"><a className="button ghost" href={resumePath} target="_blank" rel="noreferrer">View resume <ExternalLink size={15} /></a><a className="button primary" href={resumePath} download>Download <Download size={15} /></a></div></div><p className="resume-note">Replace the included resume source in <code>public/resume/</code> with your final PDF when it is ready.</p></section>
}
