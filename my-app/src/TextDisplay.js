import React, { useState, useEffect } from 'react';

function TextDisplay() {
  const [text, setText] = useState('');

  useEffect(() => {
    // Make an API request to the backend
    fetch('/get_text') // Update with the actual backend URL
      .then((response) => response.text())
      .then((data) => setText(data))
      .catch((error) => console.error('Error:', error));
  }, []);

  return (
    <div>
      <h1>Text from the Backend</h1>
      <p>{text}</p>
    </div>
  );
}

export default TextDisplay;