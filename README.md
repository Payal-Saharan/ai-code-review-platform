# AI Code Review Platform

An AI-powered platform that connects to GitHub repositories, analyzes pull requests, and helps developers review code more effectively. This project is being built step by step as a learning-and-building exercise in backend engineering and AI integration.

## Current Status

This project is in early development. Right now, it is a FastAPI backend that connects to the GitHub API. The following features currently work:

- Fetch public GitHub user profile info
- Fetch authenticated GitHub user profile info (using a Personal Access Token)
- List open pull requests for any public repository
- Fetch changed files and code diffs for a specific pull request

AI-based code review, bug detection, and automated patch generation are planned next.

## Tech Stack

- **Backend:** Python, FastAPI
- **HTTP Client:** httpx
- **Environment Management:** python-dotenv
- **External API:** GitHub REST API

## How to Run Locally

1. Clone this repository
git clone https://github.com/Payal-Saharan/ai-code-review-platform.git
2. Create a virtual environment and activate it
3. Install dependencies
pip install fastapi uvicorn httpx python-dotenv
4. Create a `.env` file in the project root with your GitHub token:
GITHUB_TOKEN=your_github_personal_access_token
5. Run the server
uvicorn main:app --reload
6. Visit `http://127.0.0.1:8000/hello` to confirm it's running

## Planned Features

- AI-powered code review comments on pull requests
- Automated bug and security issue detection
- Test generation for changed code
- Sandboxed test execution
- Automated patch suggestions