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
Challenge: find out what happens if we try to append JSX
to our div#root using .append() instead of ReactDOM

1. Create a sample page in JSX (≥ 4 elements) and save them in a variable
2. Select the div with the ID of "root" and use `.append()` to append
   your JSX
3. See if you can guess what will show up in the browser before running
   the code
4. See if you can explain what actually shows up in the browser
 */

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

document.getElementById('root').append(sample);

/*
Guess what will happen prior to running this code.

I guess without ReactDOM that maybe it will return an error? 
Next question I should ask - do I use Live Server and see if it will run it or do I use npm run start?
That I'm not too sure, but I am about to find out.

Ran live server and nothing showed up.
npm run start - this opened and on the page it says [object Object]
Now, I'm curious to know why it shows that. Is this because ReactDOM is missing and JSX is essentially an object?

Redoing the code I did because he did not create another variable and assign it a value of document.getElementById('root).
Remove the variable and use the assigned value instead then append to it. Now it will be a single line of code.
*/
