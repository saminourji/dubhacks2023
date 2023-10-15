import React from 'react';
// import TextDisplay from './TextDisplay';
import "./ImageContainer.css";

function App(props) {
  return (
    <div className="newsOutletContainer">
    <div className="newsOutletImage">
      <img
        src={"https://assets.stickpng.com/images/5842ab75a6515b1e0ad75b0b.png"}
        alt={props.media}
        className="image"
      />
    </div>
    <div className="newsOutletText">{props.media}</div>
    </div>
  );
}

export default App;