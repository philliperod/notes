import React from 'react';
import logo from './images/macbook.png';
import './index.css';

function Header() {
  return (
    <header>
      <nav className='navbar'>
        <img className='logo' src={logo} alt='' />
        <ul className='nav-items'>
          <li>Pricing</li>
          <li>About</li>
          <li>Contact</li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
