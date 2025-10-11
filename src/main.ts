import './styles/index.css'
import { statusCard } from './components/statusCard'
import { API_BASE } from './config'

const app = document.getElementById('app')!
app.innerHTML = `
  <main class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-2xl p-8 bg-white rounded-2xl shadow-lg">
    <h1 class="text-2xl font-bold mb-2">RushResQ — vapi (Hackathon)</h1>
      <p class="text-sm text-gray-600 mb-4">From-scratch branch scaffold for API integration & dashboard.</p>
      <div id="card-slot" class="space-y-3"></div>
        <div class="mt-6 text-right text-xs text-gray-500">Branch: <strong>vapi</strong></div>
    </div>
  </main>
`
const slot = document.getElementById('card-slot')!
slot.appendChild(statusCard('API Status', `Base: ${API_BASE}`))
