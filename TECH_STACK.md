# Tech Stack

## Core
- **Electron** (^45.0.0): framework for building desktop apps with web technologies
- **Node.js**: JavaScript runtime used by Electron and by npm
- **npm**: package manager used to install Electron and run scripts

## Languages
- **JavaScript** (CommonJS modules): used in `main.js` and `preload.js`
- **HTML**: used in `index.html` for the window content

## Project Structure
- `main.js`: main process, creates the app window and handles the app lifecycle
- `preload.js`: safe bridge between the web page and Node/Electron (empty for now)
- `index.html`: the page shown inside the window (renderer process)
- `package.json`: project settings, dependencies and the `start` script

## Tools
- **PowerShell**: used to create files and run commands on Windows

## Run the app
```bash
npm start
```
