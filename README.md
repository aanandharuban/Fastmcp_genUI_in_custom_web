# FastMCP Custom HTML Dashboard

A full-stack Local Analytics Server using the FastMCP framework. This project demonstrates the official MCP Apps Extension architecture by strictly separating the backend data pipeline (Python) from the frontend presentation layer (HTML/JS/Tailwind).

## 🚀 Features
* **Separation of Concerns:** Clean architecture with a Python backend (`server.py`) and a standalone frontend (`dashboard.html`).
* **Official MCP SDK:** Utilizes the `@modelcontextprotocol/ext-apps` JavaScript SDK to securely pass data from Python to the UI.
* **Custom UI Frameworks:** Frontend is styled with Tailwind CSS and uses Chart.js for dynamic, interactive data visualization.
* **Strict Security:** Implements FastMCP's `ResourceCSP` (Content Security Policy) to safely load external CDNs within the sandbox.

## 📂 Project Structure
Ensure your files are organized exactly like this in the same folder:
```text
/fastmcp-html-dashboard
│
├── server.py          # FastMCP backend (Data logic & UI routing)
├── dashboard.html     # Frontend UI (Tailwind, Chart.js, MCP SDK)
├── README.md          # Documentation
└── /venv              # Python virtual environment (ignored in git)
🛠️ Installation & Setup
1. Create a fresh Virtual Environment
Run this in your terminal to create an isolated environment:

PowerShell
python -m venv venv
2. Activate the Virtual Environment

Windows PowerShell:

PowerShell
.\venv\Scripts\activate
Mac/Linux:

Bash
source venv/bin/activate
3. Install Dependencies
Install the FastMCP application server. (Note: prefab-ui is not required for this custom HTML build).

PowerShell
pip install "fastmcp[apps]"
💻 Running the Server
To launch the developer preview environment, ensure you are in the project folder and run:

PowerShell
fastmcp dev apps server.py
How to view your dashboard:

Open your web browser and navigate to http://localhost:8080.

Locate master_analytics_workspace in the tool directory.

Click the Run Tool (or Execute) button. The Python server will read dashboard.html, fetch the data, and render the UI.

⚙️ Troubleshooting
"Waiting for Content..."
If the browser hangs after clicking Run Tool:

Hard Refresh: Press Ctrl + F5 (or Shift + F5) to clear the browser's iframe cache and reload the HTML file.

Check File Paths: Ensure dashboard.html is in the exact same folder as server.py. The Python script uses Path(__file__).parent to locate it.

Server Fails to Start (Port in Use)
If you see RuntimeError: User server did not start on port 8000, a previous session is still running in the background. Use alternate ports:

PowerShell
fastmcp dev apps server.py --mcp-port 8001 --dev-port 8081
(You will then access the dashboard at http://localhost:8081)

Modifying the UI
You can edit dashboard.html using standard web development tools (like VS Code's HTML formatter). Just save the file, go to your browser, and click Run Tool again to see the changes instantly—no need to restart the Python server!
