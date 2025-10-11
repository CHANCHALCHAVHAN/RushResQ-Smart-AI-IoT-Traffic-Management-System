export function statusCard(title: string, text: string) {
  const el = document.createElement('div')
  el.className = 'p-4 border rounded-lg bg-gray-50'
  el.innerHTML = `<h3 class="font-semibold">${title}</h3><p class="text-sm text-gray-600">${text}</p>`
  return el
}
