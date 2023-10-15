import React from "react";
import "./home.css";
import { useState } from "react";
import btn from "../../assets/Vectorinputicon.png";

const Home = () => {
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  return (
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
          <button className="inputBtn">
            <img className="inputImg" alt="go" src={btn}></img>
          </button>
        </div>
        {/* <p>You typed: {inputValue}</p>*/} .
      </div>
    </section>
  );
};

export default Home;
