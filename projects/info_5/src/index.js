import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

/* 
Challenge: Place the gray react logo in the background

Don't use an `img` element, but rather set it as the
`background-image` of the `main` element.

Hint: you'll need to use the following properties:
- background-image
- background-repeat
- background-position

(Or the shorthand `background` property with values for all
those other properties)
*/

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
