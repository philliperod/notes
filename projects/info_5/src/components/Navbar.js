import React from 'react';
import logo from './logo.svg';
import './Navbar.css';

export default function Navbar() {
  return (
    <div className='navbar'>
      <ul className='nav-items'>
        <li className='nav-item'>
          <img className='logo' src={logo} alt='logo' />
          <h3>ReactFacts</h3>
        </li>
        <li className='nav-item'>
          <h4>React Course - Project 1</h4>
        </li>
      </ul>
    </div>
  );
}
