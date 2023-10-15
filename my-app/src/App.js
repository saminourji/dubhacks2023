import logo from "./logo.svg";
import "./App.css";
import Home from "./components/home/home";
import Main from "./components/about/main";
import React, {useState, useEffect} from "react";

function App() {

  
  // const [accuracy, setAccuracy] = useState(0)

  // useEffect(() => {
  //   setAccuracy(accuracy+1)
  //   // fetch("/api/route").then((res) => res.json()).then((data) => {setAccuracy(data)});
  // }, [])
  return (
    <div className="App">
      <Home />
    </div>
  );
}

export default App;
