import { useEffect, useState } from 'react'
import { portfolioApi } from '../services/api'

export function usePortfolioData(key, fallback) {
  const [data, setData] = useState(fallback)
  const [loading, setLoading] = useState(true)
  useEffect(() => { let active = true; portfolioApi[key]().then(result => active && setData(result)).catch(() => {}).finally(() => active && setLoading(false)); return () => { active = false } }, [key])
  return { data, loading }
}
