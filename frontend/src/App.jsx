import { use, useState } from "react"

function App(){
  const [owner, setOwner]= useState("")
  const [repo, setRepo] =useState("")
  const [pullNumber, setPullNumber] =useState("")

  async function  getReview(){
    const response=await fetch(`http://127.0.0.1:8000/review/${owner}/${repo}/pulls/${pullNumber}`)
    const data= await response.json()
    console.log(data)
  }
  return (
    <div>
    <h1>AI Code Review Platform </h1>
    <input value={owner} onChange={(e)=> setOwner(e.target.value)} placeholder="Rpo owner" />
    <input value={repo} onChange={(e)=>setRepo(e.target.value)} placeholder="Repo Name" />
    <input value={pullNumber} onChange={(e)=>setPullNumber(e.target.value)} placeholder="PR number" />
    {/* <p>Owner : {owner} </p>
    <p>Repo : {repo}</p>
    <p> PR Number : {pullNumber}</p> */}
    <button onClick={getReview}>Get AI Review</button>
    </div>
  )
  }

export default App