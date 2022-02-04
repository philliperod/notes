import React from 'react';
import ReactDOM from 'react-dom';

const navbar = (
  <nav>
    <h1>Scrimba Womba</h1>
    <ul>
      <li>Pricing</li>
      <li>About</li>
      <li>Contact</li>
      <li>Profile</li>
    </ul>
  </nav>
);

ReactDOM.render(navbar, document.getElementById('root'));
