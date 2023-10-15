import logo from "./logo.svg";
import "./App.css";
import Home from "./components/home/home";
import Main from "./components/about/main";
import React, {useState, useEffect} from "react";

function App() {

  const [accuracy, setAccuracy] = useState("Jerusalem Iraael Conflict")

  useEffect(() => {
    fetch("/api/route").then((res) => res.json()).then((data) => {setAccuracy(data)});
  }, [])
  return (
    <div className="App">
      <Main summary = {accuracy}/>
    </div>
  );
}

export default App;
