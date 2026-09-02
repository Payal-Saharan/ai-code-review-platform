# AI Code Review Platform

An AI-powered platform that connects to GitHub repositories, analyzes pull requests, and helps developers review code more effectively. This project is being built step by step as a learning-and-building exercise in backend engineering and AI integration.

## Current Status

This project is in early development. Right now, it is a FastAPI backend that connects to the GitHub API and Google's Gemini AI model. The following features currently work:

- Fetch public GitHub user profile info
- Fetch authenticated GitHub user profile info (using a Personal Access Token)
- List open pull requests for any public repository
- Fetch changed files and code diffs for a specific pull request
- Generate an AI-powered code review for every changed file in a pull request, using Google Gemini — detects potential bugs, security issues, and code quality problems, with explanations and suggested fixes
- Automatically post each AI-generated review as a real comment directly on the GitHub pull request


## Tech Stack

- **Backend:** Python, FastAPI
- **HTTP Client:** httpx
- **Environment Management:** python-dotenv
- **External API:** GitHub REST API, Google Gemini API

## How to Run Locally

1. Clone this repository
git clone https://github.com/Payal-Saharan/ai-code-review-platform.git

2. Create a virtual environment and activate it
3. Install dependencies
pip install fastapi uvicorn httpx python-dotenv

4. Create a `.env` file in the project root with your GitHub token:
GITHUB_TOKEN=your_github_personal_access_token
GEMINI_API_KEY=your_gemini_api_key

5. Run the server
uvicorn main:app --reload

6. Visit `http://127.0.0.1:8000/hello` to confirm it's running or try 
`http://127.0.0.1:8000/review/{owner}/{repo}/pulls/{pull_number}` on a real public repository to see an AI-generated code review

## Planned Features

- Automated bug and security issue detection across a whole repository
- Test generation for changed code
- Sandboxed test execution
- Automated patch suggestions