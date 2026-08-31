import { ArrowDown, ArrowUpRight, Github, Linkedin, Sparkles } from 'lucide-react'

export default function Hero() {
  const jump = (id) => document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
  return <section id="home" className="hero shell">
    <div className="hero-copy reveal">
      <p className="eyebrow"><Sparkles size={14} /> Available for thoughtful work</p>
      <h1>Building useful software <em>where ideas meet intelligence.</em></h1>
      <p className="hero-lede">Software developer specializing in Python backends, REST APIs, AI-powered applications, LangChain/RAG workflows, and full-stack development.</p>
      <div className="hero-actions"><button className="button primary" onClick={() => jump('projects')}>Explore my work <ArrowUpRight size={17} /></button><button className="button ghost" onClick={() => jump('contact')}>Get in touch</button><a className="button ghost resume-hero" href="/resume/A-Sheik-Farith-Resume.md" download>Download resume</a></div>
      <div className="social-row"><a href="https://github.com/sheikfarith2006" target="_blank" rel="noreferrer" aria-label="GitHub profile"><Github size={18} /> GitHub</a><a href="https://www.linkedin.com/in/sheik-farith-a-ab223b326/" target="_blank" rel="noreferrer" aria-label="LinkedIn profile"><Linkedin size={18} /> LinkedIn</a></div>
    </div>
    <div className="hero-visual reveal" aria-label="Decorative developer and AI illustration">
      <div className="orbit orbit-one" /><div className="orbit orbit-two" />
      <div className="ai-card main-card"><div className="card-top"><span className="pulse" /> RAG_WORKFLOW <span>•••</span></div><div className="code-lines"><i /><i /><i /><i /></div><div className="node-row"><b>PDF</b><span>→</span><b className="accent-node">AI</b><span>→</span><b>ANS</b></div></div>
      <div className="floating-chip chip-one">Python <span>•</span></div><div className="floating-chip chip-two">LangChain</div>
      <div className="profile-disk"><span>&lt;/&gt;</span><small>BUILD<br />WITH INTENT</small></div>
      <div className="scroll-note"><ArrowDown size={15} /> Scroll to explore</div>
    </div>
  </section>
}
