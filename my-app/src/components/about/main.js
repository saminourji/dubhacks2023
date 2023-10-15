import React from "react";
import "./main.css";
import nbcImage from "../../assets/334_nbc.jpg"; // Corrected import path to your local image file
import nytImage from "../../assets/nyt.png";
import foxImage from "../../assets/fox.webp";
import washingtonImage from "../../assets/washington.png";
import cnnImage from "../../assets/CNN_International_logo.svg.png";
import { inputValue } from "../home/home";
import { Routes, Route, useNavigate, BrowserRouter } from "react-router-dom";

const Main = () => {
  const navigate = useNavigate();

  const goHome = () => {
    navigate("/");
  };

  return (
    <>
      <div className="main">
        <div className="buttonContainer">
          <button className="buttonText" onClick={goHome}>
            Back
          </button>
        </div>
        <div className="mainTitle">Israel and Palestine Conflict</div>
        <div className="timelineContainer">
          <ul class="timeline">
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img
                      src={washingtonImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">The Washington Times</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img
                      src={nytImage}
                      alt="New York Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">New York Times</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img
                      src={nbcImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">NBC</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img
                      src={foxImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">Fox News</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img
                      src={cnnImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">CNN</div>
                </div>
              </div>
            </li>
          </ul>
        </div>

        <div className="summaryContainer">
          <div className="summaryTitle">Quick Summary</div>
          <div className="summaryText">
            Origins: Conflict rooted in 19th-century nationalist movements, with
            Jews and Arabs both claiming historic ties to Palestine. 1948: UN
            partition plan led to the establishment of Israel and displacement
            of hundreds of thousands of Palestinians (Nakba). Key Issues:
            Borders, status of Jerusalem, security, and right of return for
            Palestinian refugees are central points of contention. Current
            Situation: Despite diplomatic efforts, a comprehensive and lasting
            peace agreement remains elusive.
          </div>
        </div>
      </div>
    </>
  );
};

export default Main;
