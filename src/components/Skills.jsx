import { usePortfolioData } from '../hooks/usePortfolioData'
import { skills as fallback } from '../data/fallback'
import SectionHeader from './SectionHeader'

export default function Skills() { const { data, loading } = usePortfolioData('skills', fallback); const skillGroups = data || fallback; return <section id="skills" className="section shell"><SectionHeader number="02" eyebrow="Technical toolkit" title={<>Tools for the <em>whole build.</em></>} text="A growing toolkit shaped by hands-on product and application work." />{loading ? <div className="loading-line">Loading skills…</div> : <div className="skills-grid reveal">{skillGroups.map((group, i) => <article className="skill-card" key={group.category}><span className="skill-number">0{i + 1}</span><h3>{group.category}</h3><div className="skill-tags">{group.items.map(skill => <span key={skill}>{skill}</span>)}</div></article>)}</div>}</section> }
