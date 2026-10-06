import { useState, useEffect } from "react"

function HistoryPage() {
  const [history, setHistory] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function fetchHistory() {
      const response = await fetch("http://127.0.0.1:8000/history")
      const data = await response.json()
      setHistory(data)
      setLoading(false)
    }
    fetchHistory()
  }, [])

  const uniquePRs = new Set(history.map((h) => `${h.repo_owner}/${h.repo_name}#${h.pull_number}`)).size

  return (
    <div className="app-container">
      <div className="app-header">
        <span className="badge">ARCHIVE</span>
        <h1>Review History</h1>
        <p>Every AI-generated review, saved permanently</p>
      </div>

      {!loading && history.length > 0 && (
        <div className="stats-row">
          <div className="stat-box">
            <div className="stat-number">{history.length}</div>
            <div className="stat-label">Files Reviewed</div>
          </div>
          <div className="stat-box">
            <div className="stat-number">{uniquePRs}</div>
            <div className="stat-label">Pull Requests</div>
          </div>
        </div>
      )}

      {loading && (
        <div className="loading-box">
          <div className="spinner"></div>
          Loading history...
        </div>
      )}

      {!loading && history.length === 0 && (
        <div className="empty-state">
          <div className="icon">📭</div>
          <p>No reviews yet. Go review a pull request to see it here.</p>
        </div>
      )}

      {!loading && history.length > 0 && (
        <div className="results-section">
          {history.slice().reverse().map((item) => (
            <div key={item.id} className="review-card">
              <div className="meta-line">
                {item.repo_owner}/{item.repo_name} · PR #{item.pull_number} · {new Date(item.created_at).toLocaleString()}
              </div>
              <div className="review-card-header">
                <h3>{item.filename}</h3>
              </div>
              <p>{item.review_text}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default HistoryPage