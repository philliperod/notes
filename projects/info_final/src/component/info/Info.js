import React from 'react';
import { Envelope } from 'phosphor-react';
import './info.css';

export default function Info() {
  return (
    <div className='info'>
      <img className='info--picture' src='' alt='' />
      <h2 className='info--name'>DMX</h2>
      <h3 className='info--title'>Rapper / Actor / Dog Whisperer</h3>
      <p className='info--email'>dmx.woofwoof</p>
      <ul className='buttons'>
        <button className='button--email'>
          <Envelope className='button--email_icon' size={20} weight='fill' />
          <p className='button--email_text'>Email</p>
        </button>
        <button className='button--social'>LinkedIn</button>
      </ul>
    </div>
  );
}

/*

structure:

Profile Picture
-  takes about 75% of the height of the component
- center face picture
- top rounded corners, flat bottom corners

First & Last Name
- biggest text size
- soft white text
- sans-serif type text
- bold (600) font weight

Title
- colored text that matches a background color from the profile picture
- thin (400) font weight
- medium small text size

Email Address
- gray color text or darker than the name text
- smaller text size


Email button
- flat color background
- email icon
- spelled as "Email"
- rounded corners
- left alignment

Linkedin button
- flat color background
- linkdedin icon
- spelled as "LinkedIn"
- rounded corners
- right alignment


- overall background matches to components below

*/
