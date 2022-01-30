/*
const h1 = document.createElement('h1');
h1.textContent = 'Hello world';
h1.className = 'header';
console.log(h1);

const element = (
  <div>
    <h1 className='header'>This is React</h1>`<p>We're using JSX</p>
  </div>
);

ReactDOM.render(element, document.getElementById('root'));
*/

/*
Challenge: 

Create a navbar in JSX:
    - Use the semantic `nav` element as the parent wrapper
    - Have an h1 element with the brand name of your "website"
    - Insert an unordered list for the other nav elements
        - Inside the `ul`, have three `li`s for "Pricing",
        "About", and "Contact"
    - Don't worry about styling yet - it'll just be plain-looking HTML for now
*/

const navbar = (
  <nav>
    <h1>Scrimba Womba</h1>
    <ul>
      <li>Pricing</li>
      <li>About</li>
      <li>Contact</li>
    </ul>
  </nav>
);

ReactDOM.render(navbar, document.getElementById('root'));
