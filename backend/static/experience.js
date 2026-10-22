// Availability calendar for the experience page.
// The server puts the available days in <script id="availability-data">.
(function () {
  const root = document.getElementById('availability-calendar')
  const dataEl = document.getElementById('availability-data')
  if (!root || !dataEl) return

  const days = JSON.parse(dataEl.textContent) // { "2026-11-03": "available" | "limited" }
  const bookUrl = root.getAttribute('data-book-url')
  const bookLink = document.getElementById('book-link')
  const summary = document.getElementById('cal-summary')
  const title = root.querySelector('.cal-title')
  const grid = root.querySelector('.cal-grid')
  const prev = root.querySelector('.cal-prev')
  const next = root.querySelector('.cal-next')

  const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December']
  const WEEKDAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

  const now = new Date()
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
  const keys = Object.keys(days).sort()

  const monthOf = (key) => new Date(Number(key.slice(0, 4)), Number(key.slice(5, 7)) - 1, 1)
  const firstMonth = new Date(today.getFullYear(), today.getMonth(), 1)
  const lastMonth = keys.length ? monthOf(keys[keys.length - 1]) : firstMonth
  let view = keys.length ? monthOf(keys[0]) : firstMonth
  let selected = null

  const pad = (n) => (n < 10 ? '0' + n : String(n))
  const toKey = (y, m, d) => y + '-' + pad(m + 1) + '-' + pad(d)
  const longDate = (date) => date.toLocaleDateString('en-GB', {
    weekday: 'long', day: 'numeric', month: 'long', year: 'numeric',
  })

  function select(key) {
    selected = key
    const date = new Date(Number(key.slice(0, 4)), Number(key.slice(5, 7)) - 1, Number(key.slice(8, 10)))
    summary.textContent = 'Selected: ' + longDate(date)
    if (bookLink) {
      bookLink.href = bookUrl + (bookUrl.indexOf('?') === -1 ? '?' : '&') + 'date=' + key
      bookLink.textContent = 'Book for ' + date.toLocaleDateString('en-GB', { day: 'numeric', month: 'short' })
    }
    render()
  }

  function render() {
    const y = view.getFullYear()
    const m = view.getMonth()
    title.textContent = MONTHS[m] + ' ' + y
    grid.innerHTML = ''

    WEEKDAYS.forEach((name) => {
      const cell = document.createElement('div')
      cell.className = 'cal-dow'
      cell.textContent = name
      grid.appendChild(cell)
    })

    const offset = (new Date(y, m, 1).getDay() + 6) % 7 // week starts on Monday
    for (let i = 0; i < offset; i++) {
      const blank = document.createElement('div')
      blank.className = 'cal-day blank'
      grid.appendChild(blank)
    }

    const count = new Date(y, m + 1, 0).getDate()
    for (let d = 1; d <= count; d++) {
      const key = toKey(y, m, d)
      const date = new Date(y, m, d)
      const status = days[key]
      const button = document.createElement('button')
      button.type = 'button'
      button.className = 'cal-day'
      button.textContent = d
      if (date.getTime() === today.getTime()) button.classList.add('today')

      if (status && date > today) {
        button.classList.add(status)
        button.setAttribute('aria-label', longDate(date) + ', ' + (status === 'limited' ? 'few spots left' : 'available'))
        if (key === selected) {
          button.classList.add('selected')
          button.setAttribute('aria-pressed', 'true')
        }
        button.addEventListener('click', () => select(key))
      } else {
        button.disabled = true
        button.setAttribute('aria-label', longDate(date) + ', not available')
      }
      grid.appendChild(button)
    }

    prev.disabled = view <= firstMonth
    next.disabled = view >= lastMonth
  }

  prev.addEventListener('click', () => { view = new Date(view.getFullYear(), view.getMonth() - 1, 1); render() })
  next.addEventListener('click', () => { view = new Date(view.getFullYear(), view.getMonth() + 1, 1); render() })

  render()
})()