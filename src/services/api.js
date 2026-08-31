const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  })
  if (!response.ok) {
    const body = await response.json().catch(() => ({}))
    throw new Error(body.detail || 'Something went wrong. Please try again.')
  }
  return response.json()
}

export const portfolioApi = {
  projects: () => request('/projects'),
  skills: () => request('/skills'),
  experience: () => request('/experience'),
  contact: (data) => request('/contact', { method: 'POST', body: JSON.stringify(data) }),
}
