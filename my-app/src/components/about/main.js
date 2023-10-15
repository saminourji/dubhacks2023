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
  const [title1, setTitle1] = useState("Loading...");
  const [title2, setTitle2] = useState("Loading...");
  const [title3, setTitle3] = useState("Loading...");
  const [title4, setTitle4] = useState("Loading...");
  const [title5, setTitle5] = useState("Loading...");

  useEffect(() => {
    // Make an API request to the backend
    fetch('/get_text') // Update with the actual backend URL
      .then((response) => (response.text()))
      .then((data) => setText(data))
      .catch((error) => console.error('Error:', error));
  
    fetch('/get_articles') // Update with the actual backend URL
      // .then((response) => (response))
      .then((data) => { setArticles(data)
      setTitle1(data[0]["media"])
      setTitle2(data[1]["media"])
      setTitle3(data[2]["media"])
      setTitle4(data[3]["media"])
      setTitle5(data[4]["media"])
    })
      .catch((error) => console.error('Error:', error));
    }, []);

  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageClick = (imageName) => {
    setSelectedImage(imageName);
    setText(articles[Number(selectedImage)-1]["summary"])
    setTitle(articles[Number(selectedImage)-1]["title"])
  };

  return (
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
                      onClick={() => handleImageClick('1')} 
                      src={washingtonImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">{title1}</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img 
                      onClick={() => handleImageClick('2')} 
                      src={nytImage}
                      alt="New York Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">{title2}</div>
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
                  <div className="newsOutletText">{title3}</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img 
                      onClick={() => handleImageClick('4')} 
                      src={foxImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">{title4}</div>
                </div>
              </div>
            </li>
            <li>
              <div className="tooltip">
                <div className="newsOutletContainer">
                  <div className="newsOutletImage">
                    <img 
                      onClick={() => handleImageClick('5')} 
                      src={cnnImage}
                      alt="Washington Times"
                      className="image"
                    />
                  </div>
                  <div className="newsOutletText">{title5}</div>
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
  );
};

export default Main;
