import React, {useState} from "react";
import "./main.css";
import nbcImage from "../../assets/334_nbc.jpg"; // Corrected import path to your local image file
import nytImage from "../../assets/nyt.png";
import foxImage from "../../assets/fox.webp";
import washingtonImage from "../../assets/washington.png";
import cnnImage from "../../assets/CNN_International_logo.svg.png";

const Main = (props) => {
  return (
    <>
      <div className="main">
        <div className="buttonContainer">
          <div className="buttonText">Back</div>
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
            {props.summary}
          </div>
        </div>
      </div>
    </>
  );
};

export default Main;
