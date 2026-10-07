import { useState } from "react"

function ReviewPage() {
  const [owner, setOwner] = useState("")
  const [repo, setRepo] = useState("")
  const [pullNumber, setPullNumber] = useState("")
  const [reviews, setReviews] = useState([])
  const [loading, setLoading] = useState(false)

  async function getReview() {
    setLoading(true)
    setReviews([])
   const response = await fetch(`https://ai-code-review-platform-production-959f.up.railway.app/review/${owner}/${repo}/pulls/${pullNumber}`)
    const data = await response.json()
    setReviews(data)
    setLoading(false)
  }

  const isDisabled = !owner || !repo || !pullNumber || loading

  return (
    <div className="app-container">
      <div className="app-header">
        <span className="badge">AI-POWERED</span>
        <h1>Review a Pull Request</h1>
        <p>Get an instant AI-generated code review, posted straight to GitHub</p>
      </div>

      <div className="form-card">
        <div className="input-group">
          <label>Repository Owner</label>
          <input value={owner} onChange={(e) => setOwner(e.target.value)} placeholder="e.g. Payal-Saharan" />
        </div>
        <div className="input-group">
          <label>Repository Name</label>
          <input value={repo} onChange={(e) => setRepo(e.target.value)} placeholder="e.g. html_test" />
        </div>
        <div className="input-group">
          <label>Pull Request Number</label>
          <input value={pullNumber} onChange={(e) => setPullNumber(e.target.value)} placeholder="e.g. 1" />
        </div>
        <button onClick={getReview} disabled={isDisabled}>
          {loading ? "Reviewing..." : "Get AI Review"}
        </button>
      </div>

      {loading && (
        <div className="loading-box">
          <div className="spinner"></div>
          Analyzing code changes, this can take a moment...
        </div>
      )}

      {!loading && reviews.length > 0 && (
        <div className="results-section">
          {reviews.map((review, index) => (
            <div key={index} className="review-card">
              <div className="review-card-header">
                <h3>{review.filename}</h3>
                <span className={`status-badge ${review.comment_status === 201 ? "status-posted" : "status-failed"}`}>
                  {review.comment_status === 201 ? "✓ Posted to GitHub" : "Not posted"}
                </span>
              </div>
              <p>{review.review}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default ReviewPage