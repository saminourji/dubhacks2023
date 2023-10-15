import React from "react";
import "./home.css";
import { useState } from "react";
import btn from "../../assets/Vectorinputicon.png";
import bg from "../../assets/bg.svg";

const Home = () => {
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  return (
    <section> 
      <img className="bg" alt="bg" src={bg} />
      <div className="title">SpectrumAI</div>
      <div className="subtitle"> The biases in your news sources, ranked and summarized. </div>
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
