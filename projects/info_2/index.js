// second assignment
function Navbar() {
  return (
    <nav className='navbar navbar-expand-lg navbar-light bg-light'>
      <a href='#' className='navbar-brand'>
        Navbar
      </a>
      <button
        type='button'
        className='navbar-toggler'
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
            <a className='nav-link' href='#'></a>
          </li>
          <li className='nav-item dropdown'>
            <a
              className='nav-link dropdown-toggle'
              id='navbarDropdown'
              href='#'
              role='button'
              data-toggle='dropdown'
              aria-haspopup='true'
              aria-expanded='false'
            >
              Dropdown
            </a>
            <div className='dropdown-menu' aria-labelledy='navbarDropdown'>
              <a className='dropdown-item' href='#'>
                Action
              </a>
              <a className='dropdown-item' href='#'>
                Another action
              </a>
              <div className='dropdown-divider'></div>
              <a id='' className='dropdown-item'>
                Something else here
              </a>
            </div>
          </li>
          <li className='nav-item'>
            <a className='nav-link' href='#'>
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

ReactDOM.render(
  <div>
    <Navbar />
  </div>,
  document.getElementById('root')
);
