import React from 'react';
import logo from './logo.svg';
import './Navbar.css';

export default function Navbar() {
  return (
    <nav>
      <img className='logo' src={logo} alt='logo' />
      <h3>ReactFacts</h3>
      <h4>React Course - Project 1</h4>
    </nav>
  );
}
