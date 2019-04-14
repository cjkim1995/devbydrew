import React, { Component } from 'react';
import logo from './logo.svg';
import './App.scss';

import Link from 'components/Link';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p className="App-text">
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <p className="App-text">
            This app was created with <code>create-react-app</code> and includes
            <ul>
              <li>Bootstrap via <code>react-bootstrap</code>,</li>
              <li>SCSS via <code>node-sass</code>,</li>
              <li>classNames via <code>classnames</code>,</li>
              <li>React Router via <code>react-router-dom</code>, and</li>
              <li>PropTypes via <code>prop-types</code>.</li>
            </ul>
          </p>
          <Link href="https://reactjs.org" target="_blank" className="App-link" underline={false}>
            Learn React
          </Link>
        </header>
      </div>
    );
  }
}

export default App;
