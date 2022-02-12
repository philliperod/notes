// This will include all challenges and the end project

/*
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
*/

/*
import React from 'react';

Challenge: find out what happens if we try to append JSX
to our div#root using .append() instead of ReactDOM

1. Create a sample page in JSX (≥ 4 elements) and save them in a variable
2. Select the div with the ID of "root" and use `.append()` to append
   your JSX
3. See if you can guess what will show up in the browser before running
   the code
4. See if you can explain what actually shows up in the browser

const sample = (
  <main>
    <h3>Scrimba Header</h3>
    <p>
      This is going to be cool to learn React by doing more than watching videos.
    </p>
    <p>
      I think that is what I am missing plus he makes you try to figure it out on
      your own prior to giving you directions on what to do.
    </p>
  </main>
);

document.getElementById('root').append(sample);
*/

/*
import React from 'react';
import ReactDOM from 'react-dom';

Guess what will happen prior to running this code.

I guess without ReactDOM that maybe it will return an error? 
Next question I should ask - do I use Live Server and see if it will run it or do I use npm run start?
That I'm not too sure, but I am about to find out.

Ran live server and nothing showed up.
npm run start - this opened and on the page it says [object Object]
Now, I'm curious to know why it shows that. Is this because ReactDOM is missing and JSX is essentially an object?

Redoing the code I did because he did not create another variable and assign it a value of document.getElementById('root).
Remove the variable and use the assigned value instead then append to it. Now it will be a single line of code.


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
*/
/*

Stringify the code to see the output on the page.

import React from 'react';

const sample = (
  <main>
    <h3>Scrimba Header</h3>
    <p>
      This is going to be cool to learn React by doing more than watching videos.
    </p>
    <p>
      I think that is what I am missing plus he makes you try to figure it out on
      your own prior to giving you directions on what to do.
    </p>
  </main>
);

document.getElementById('root').append(JSON.stringify(sample));
*/

/*
import React from 'react';
import ReactDOM from 'react-dom';

Challenge: fix our code!

Don't forget, you're not using CDNs anymore, so there's no
global "ReactDOM" variable to use anymore.


const sample = (
  <main>
    <h3>Scrimba Header</h3>
    <p>
      This is going to be cool to learn React by doing more than watching videos.
    </p>
    <p>
      I think that is what I am missing plus he makes you try to figure it out on
      your own prior to giving you directions on what to do.
    </p>
  </main>
);

ReactDOM.render(sample, document.getElementById('root'));
*/

/*
import React from 'react';
import ReactDOM from 'react-dom';

Challenge: Starting from scratch, build and render the 
HTML for our section project. Check the Google slide for 
what you're trying to build.

We'll be adding styling to it later.

Hints:
* The React logo is a file in the project tree, so you can
  access it by using `src="./react-logo.png" in your image
  element
* You can also set the `width` attribute of the image element
  just like in HTML. In the slide, I have it set to 40px
 

const markup = (
  <div>
    <header>
      <img src='../Notes/projects/info_4/index.js' alt='mac' />
      <h1>Fun facts about React</h1>
    </header>
    <ul>
      <li>Was first released in 2013</li>
      <li>Was originally created by Jordan Walke</li>
      <li>Has well over 100k stars on Github</li>
      <li>Is maintained by Facebook</li>
      <li>Power thousands of enterprise apps, including mobile apps</li>
    </ul>
  </div>
);

ReactDOM.render(markup, document.getElementById('root'));
*/

/*
import React from 'react';
import ReactDOM from 'react-dom';

Challenge: 

Part 1: Create a page of your own using a custom Page component

It should return an ordered list with the reasons why you're
excited to be learning React :)

Render your list to the page


function Reason() {
  return (
    <div>
      <h2>Reasons Why I Like React</h2>
      <ul>
        <li>Hireable skills</li>
        <li>Pretty fun code to learn, honestly</li>
        <li>
          Somehow it's easier to learn? Or maybe the code makes more sense when
          reading
        </li>
        <li>Its performance is awesome when interacting with it</li>
        <li>
          I'm trying to build something work related to see if I can do it on my own
        </li>
      </ul>
    </div>
  );
}

ReactDOM.render(<Reason />, document.getElementById('root'));
*/

import React from 'react';
import ReactDOM from 'react-dom';
import logo from './images/macbook.png';

/**
Challenge: 

Part 2: 
- Add a `header` element with a nested `nav` element. Inside the `nav`,
  include a `img` element with the image of the React logo inside
  (src="./react-logo.png") and make sure to set the width to something
  more manageable so it doesn't take up the whole screen
- Add an `h1` with some text describing the page. (E.g. "Reasons
  I'm excited to learn React"). Place it above the ordered list.
- Add a `footer` after the list that says: 
    "© 20xx <last name here> development. All rights reserved."

 */

function Reason() {
  return (
    <div>
      <header>
        <nav>
          <img src={logo} alt='' />
        </nav>
      </header>
      <h2>Reasons Why I Like React</h2>
      <ol>
        <li>Hireable skills</li>
        <li>Pretty fun code to learn, honestly</li>
        <li>
          Somehow it's easier to learn? Or maybe the code makes more sense when
          reading
        </li>
        <li>Its performance is awesome when interacting with it</li>
        <li>
          I'm trying to build something work related to see if I can do it on my own
        </li>
      </ol>
    </div>
  );
}

ReactDOM.render(<Reason />, document.getElementById('root'));
