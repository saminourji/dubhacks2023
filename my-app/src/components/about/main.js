import React, {useState, useEffect} from "react";
import "./main.css";
import nbcImage from "../../assets/334_nbc.jpg"; // Corrected import path to your local image file
import nytImage from "../../assets/nyt.png";
import foxImage from "../../assets/fox.webp";
import washingtonImage from "../../assets/washington.png";
import cnnImage from "../../assets/CNN_International_logo.svg.png";
// import TextDisplay from './TextDisplay';

const Main = (props) => {
  
  const [text, setText] = useState('');
  const [articles, setArticles] = useState([]);
  const [title, setTitle] = useState("Quick Summary");

  useEffect(() => {
    // Make an API request to the backend
    fetch('/get_text') // Update with the actual backend URL
      .then((response) => (response[0].text(), response[1]))
      .then((data) => setText(data))
      .catch((error) => console.error('Error:', error));
  }, []);

  useEffect(() => {
    // Make an API request to the backend
    fetch('/get_articles') // Update with the actual backend URL
      // .then((response) => json.loads(response))
      .then((data) => setArticles(data))
      .catch((error) => console.error('Error:', error));
  }, []);

  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageClick = (imageName) => {
    setSelectedImage(imageName);
    setText(articles[Number(selectedImage)-1]["summary"])
    setTitle(articles[Number(selectedImage)-1]["title"])
  };

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
                    <img onClick={() => handleImageClick('1')} 
                      src={washingtonImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">articles[0]["media"]</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img onClick={() => handleImageClick('2')} 
                      src={nytImage}
                      alt="New York Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">articles[1]["media"]</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img onClick={() => handleImageClick('3')} 
                      src={nbcImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">articles[2]["media"]</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img onClick={() => handleImageClick('4')} 
                      src={foxImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">articles[3]["media"]</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img onClick={() => handleImageClick('5')} 
                      src={cnnImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">{articles[4]["media"]}</div>
                </div>
              </div>
            </li>
          </ul>
        </div>

        <div className="summaryContainer">
          <div className="summaryTitle">{title}</div>
          <div className="summaryText">
            {text}
          </div>
        </div>
      </div>
    </>
  );
};

export default Main;
