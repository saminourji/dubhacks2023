import React from "react";
import "./main.css";
import { CloseButton } from '@chakra-ui/react';
import nbcImage from "../../assets/334_nbc.jpg"; // Corrected import path to your local image file
import nytImage from "../../assets/nyt.png";
import foxImage from "../../assets/fox.webp";
import washingtonImage from "../../assets/washington.png";
import cnnImage from "../../assets/CNN_International_logo.svg.png";


const Main = () => {
    return (
        <section>
            <div className="main">
                <div className="buttonContainer">
                    <div className="buttonText">Back</div>
                </div>
                <div className="mainTitle">Israel and Palestine Conflict</div>
                <div className="textNewsContainer">
                <div className="textNews">The New York Times</div>
                <img src={nytImage} alt="Description" className="ellipseImage" />
                <div className="textNews">CNN</div>
                <img src={cnnImage} alt="Description" className="ellipseImage" />
                <div className="textNews">NBC</div>
                <img src={nbcImage} alt="Description" className="ellipseImage" />
                <div className="textNews">The Washington Times</div>
                <img src={washingtonImage} alt="Description" className="ellipseImage" />
                <div className="textNews">Fox News</div>
                <img src={foxImage} alt="Description" className="ellipseImage" />
                </div>
                <div className="summaryContainer">
                  <div className = "summaryTitle">Quick Summary</div>
                    <div className="closeButtonContainer">
                        <CloseButton className="closeButton" />
                    </div>
                    Origins: Conflict rooted in 19th-century nationalist movements, with Jews and Arabs both claiming historic ties to Palestine.
1948: UN partition plan led to the establishment of Israel and displacement of hundreds of thousands of Palestinians (Nakba).
Key Issues: Borders, status of Jerusalem, security, and right of return for Palestinian refugees are central points of contention.
Attempts for Peace: Multiple wars, uprisings, and peace initiatives, including Oslo Accords in the 1990s, aimed at a two-state solution.
Ongoing Challenges: Violence, economic instability, and social divisions affect civilian populations on both sides.
International Involvement: Involvement of various regional and international actors adds complexity to the conflict resolution process.
Current Situation: Despite diplomatic efforts, a comprehensive and lasting peace agreement remains elusive.
                </div>
            </div>
        </section>
    );
};

export default Main;
