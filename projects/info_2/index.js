/*
second assignment

function Navbar() {
  return (
    <nav className='navbar navbar-expand-lg navbar-light bg-light'>
      <a className='navbar-brand' href='#'>
        Navbar
      </a>
      <button
        className='navbar-toggler'
        type='button'
        data-toggle='collapse'
        data-target='#navbarSupportedContent'
        aria-controls='navbarSupportedContent'
        aria-expanded='false'
        aria-label='Toggle navigation'
      >
        <span className='navbar-toggler-icon'></span>
      </button>

      <div className='collapse navbar-collapse' id='navbarSupportedContent'>
        <ul className='navbar-nav mr-auto'>
          <li className='nav-item active'>
            <a className='nav-link' href='#'>
              Home <span className='sr-only'>(current)</span>
            </a>
          </li>
          <li className='nav-item'>
            <a className='nav-link' href='#'>
              Link
            </a>
          </li>
          <li className='nav-item dropdown'>
            <a
              className='nav-link dropdown-toggle'
              href='#'
              id='navbarDropdown'
              role='button'
              data-toggle='dropdown'
              aria-haspopup='true'
              aria-expanded='false'
            >
              Dropdown
            </a>
            <div className='dropdown-menu' aria-labelledby='navbarDropdown'>
              <a className='dropdown-item' href='#'>
                Action
              </a>
              <a className='dropdown-item' href='#'>
                Another action
              </a>
              <div className='dropdown-divider'></div>
              <a className='dropdown-item' href='#'>
                Something else here
              </a>
            </div>
          </li>
          <li className='nav-item'>
            <a className='nav-link disabled' href='#'>
              Disabled
            </a>
          </li>
        </ul>
        <form className='form-inline my-2 my-lg-0'>
          <input
            className='form-control mr-sm-2'
            type='search'
            placeholder='Search'
            aria-label='Search'
          />
          <button className='btn btn-outline-success my-2 my-sm-0' type='submit'>
            Search
          </button>
        </form>
      </div>
    </nav>
  );
}

function MainContent() {
  return (
    <div>
      <h1>This is your header</h1>
      <p>This is the content. That's it. Not much...</p>
    </div>
  );
}

ReactDOM.render(
  <div>
    <Navbar />
    <MainContent />
  </div>,
  document.getElementById('root')
);
*/

/*
third assignment

const root = document.getElementById('root');
const heading = document.createElement('p');
let content = 'Using javascript to append content into the root element';

heading.append(content);
root.append(heading);
*/

/*
totally didn't read the instructions clearly

ReactDOM.render(<h1>Hello, React!</h1>, document.getElementById("root"))

Challenge - recreate the above line of code in vanilla JS by creating and
appending an h1 to our div#root (without using innerHTML).

- Create a new h1 element
- Give it some textContent
- Give it a class name of "header"
- append it as a child of the div#root    
*/

const h1 = document.createElement('h1');
h1.textContent = 'Utilizing javascript in an imperative way.';
h1.cllassName = 'header';
document.getElementById('root').append(h1);
