export default function SectionHeader({ number, eyebrow, title, text }) {
  return <div className="section-header reveal"><div className="section-index">{number}</div><div><p className="eyebrow">{eyebrow}</p><h2>{title}</h2>{text && <p>{text}</p>}</div></div>
}
