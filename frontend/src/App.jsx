import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom"
import "./App.css"
import ReviewPage from "./pages/ReviewPage"
import HistoryPage from "./pages/HistoryPage"

function App() {
  return (
    <BrowserRouter>
      <nav className="navbar">
        <span className="brand">🤖 AI Code Review</span>
        <div className="nav-links">
          <NavLink to="/" end className={({ isActive }) => isActive ? "active" : ""}>Review</NavLink>
          <NavLink to="/history" className={({ isActive }) => isActive ? "active" : ""}>History</NavLink>
        </div>
      </nav>

      <Routes>
        <Route path="/" element={<ReviewPage />} />
        <Route path="/history" element={<HistoryPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App