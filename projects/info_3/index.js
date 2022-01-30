// const h1 = document.createElement('h1');
// h1.textContent = 'Hello world';
// h1.className = 'header';
// console.log(h1);

const element = (
  <div>
    <h1 className='header'>This is React</h1>
    <p>We're using JSX</p>
  </div>
);

ReactDOM.render(element, document.getElementById('root'));
