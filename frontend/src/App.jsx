import { useState } from "react"

function App() {
  const [owner, setOwner] = useState("")
  const [repo, setRepo] = useState("")
  const [pullNumber, setPullNumber] = useState("")
  const [reviews, setReviews] = useState([])

  async function getReview() {
    const response = await fetch(
      `http://127.0.0.1:8000/review/${owner}/${repo}/pulls/${pullNumber}`
    )

    const data = await response.json()

    setReviews(data)
  }

  return (
    <div>
      <h1>AI Code Review Platform</h1>

      <input
        value={owner}
        onChange={(e) => setOwner(e.target.value)}
        placeholder="Repo owner"
      />

      <input
        value={repo}
        onChange={(e) => setRepo(e.target.value)}
        placeholder="Repo Name"
      />

      <input
        value={pullNumber}
        onChange={(e) => setPullNumber(e.target.value)}
        placeholder="PR number"
      />

      <button onClick={getReview}>Get AI Review</button>

      {reviews.map((review, index) => (
        <div key={index}>
          <h3>{review.filename}</h3>
          <p>{review.review}</p>
        </div>
      ))}
    </div>
  )
}

export default App