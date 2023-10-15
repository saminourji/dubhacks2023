import React from "react";
import "./home.css";
import { useState } from "react";
import btn from "../../assets/Vectorinputicon.png";
import { Routes, Route, useNavigate, BrowserRouter } from "react-router-dom";
import Main from "../about/main";

const Home = () => {
  const [inputValue, setInputValue] = useState("");
  const navigate = useNavigate();

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const goMain = () => {
    navigate("/main");
  };

  return (
    <>
      <section>
        <div className="title">SpectrumAI</div>
        <div className="subtitle"> Experience multiple perspectives </div>
        <div className="input">
          <div className="inputBoxContainer">
            <input
              className="inputBox"
              type="text"
              value={inputValue}
              onChange={handleInputChange}
              placeholder="What do you want to know?"
            />
            <button className="inputBtn" onClick={goMain}>
              <img className="inputImg" alt="go" src={btn}></img>
            </button>
            <p className="p">Learn more about: {inputValue}</p>
          </div>
        </div>
      </section>
    </>
  );
};

export default Home;
