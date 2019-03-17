import React, { Component } from 'react';
// import logo from './logo.svg';
// import './App.css';
import { BrowserRouter, Route } from 'react-router-dom';

import Home from "./components/Home";

// const NewRoute = () => {
//   return (
//     <div>
//       <p>New Route</p>
//     </div>
//   );
// }

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        {/*<Route path="/new" component={NewRoute}>*/}
        <Route path="/" component={"Home"}/>
      </BrowserRouter>
    );
  }
}

// function App() {
//   return (
//     <div>
//       <Header />
//       <Main />
//     </div>
//   );
// }

export default App;
