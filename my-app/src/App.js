import logo from "./logo.svg";
import "./App.css";
import Home from "./components/home/home";
import Main from "./components/about/main";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/main" element={<Main />} />
          <Route path="/" element={<Home />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
