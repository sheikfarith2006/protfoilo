import { useState } from 'react'
import { Menu, X } from 'lucide-react'

const links = ['About', 'Skills', 'Experience', 'Projects', 'Resume', 'Contact']

export default function Navbar() {
  const [open, setOpen] = useState(false)
  const navigate = (id) => { setOpen(false); document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' }) }
  return <header className="nav-wrap">
    <nav className="nav shell" aria-label="Main navigation">
      <button className="brand" onClick={() => navigate('home')} aria-label="Back to top"><span>SF</span> A. Sheik Farith</button>
      <button className="menu-button" onClick={() => setOpen(!open)} aria-label="Toggle navigation">{open ? <X /> : <Menu />}</button>
      <div className={`nav-links ${open ? 'open' : ''}`}>{links.map((link) => <button key={link} onClick={() => navigate(link.toLowerCase())}>{link}</button>)}<button className="nav-contact" onClick={() => navigate('contact')}>Let’s talk <span>↗</span></button></div>
    </nav>
  </header>
}
