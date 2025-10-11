import './styles/index.css'
import { statusCard } from './components/statusCard'
import { API_BASE } from './config'

const app = document.getElementById('app')!
app.innerHTML = `
  <main class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-2xl p-8 bg-white rounded-2xl shadow-lg">
