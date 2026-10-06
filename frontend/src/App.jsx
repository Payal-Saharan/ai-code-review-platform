import { useState } from "react"
import "./App.css"

function App() {
  const [owner, setOwner] = useState("")
  const [repo, setRepo] = useState("")
  const [pullNumber, setPullNumber] = useState("")
  const [reviews, setReviews] = useState([])
  const [loading, setLoading] = useState(false)

  async function getReview() {
    setLoading(true)
    const response = await fetch(`http://127.0.0.1:8000/review/${owner}/${repo}/pulls/${pullNumber}`)
    const data = await response.json()
    setReviews(data)
    setLoading(false)
  }

  return (
    <div className="app-container">
      <div className="app-header">
        <h1>AI Code Review Platform</h1>
        <p>Enter a pull request to get an AI-generated code review</p>
      </div>

      <div className="form-card">
        <input
          value={owner}
          onChange={(e) => setOwner(e.target.value)}
          placeholder="Repo owner"
        />
        <input
          value={repo}
          onChange={(e) => setRepo(e.target.value)}
          placeholder="Repo name"
        />
        <input
          value={pullNumber}
          onChange={(e) => setPullNumber(e.target.value)}
          placeholder="PR number"
        />
        <button onClick={getReview}>Get AI Review</button>
      </div>

      {loading && <p className="loading-text">Loading review, please wait...</p>}

      {reviews.map((review, index) => (
        <div key={index} className="review-card">
          <h3>{review.filename}</h3>
          <p>{review.review}</p>
        </div>
      ))}
    </div>
  )
}

export default App