const { app, BrowserWindow } = require('electron')
const { spawn } = require('child_process')
const http = require('http')
const path = require('path')

const BACKEND_URL = 'http://127.0.0.1:5000'
let backend = null

// Start the Python (Flask) server
function startBackend() {
  backend = spawn('python', ['app.py'], {
    cwd: path.join(__dirname, 'backend'),
    stdio: 'inherit',
  })
  backend.on('error', (err) => {
    console.error('Could not start the Python backend:', err.message)
  })
}

// Wait until the server answers (tries for about 10 seconds)
function waitForBackend(retries = 50) {
  return new Promise((resolve, reject) => {
    const attempt = (left) => {
      http
        .get(BACKEND_URL, (res) => {
          res.resume()
          resolve()
        })
        .on('error', () => {
          if (left <= 0) return reject(new Error('Backend did not start'))
          setTimeout(() => attempt(left - 1), 200)
        })
    }
    attempt(retries)
  })
}

async function createWindow() {
  const win = new BrowserWindow({
    width: 1100,
    height: 750,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
    },
  })

  try {
    await waitForBackend()
    win.loadURL(BACKEND_URL)
  } catch (err) {
    const html = '<h2>Backend failed to start</h2><p>Check that Python and Flask are installed.</p>'
    win.loadURL('data:text/html;charset=utf-8,' + encodeURIComponent(html))
  }
}

app.whenReady().then(() => {
  startBackend()
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Stop the Python server when the app closes
app.on('will-quit', () => {
  if (backend) backend.kill()
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})