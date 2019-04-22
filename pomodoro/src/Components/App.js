import React, { Component } from 'react';
import Timer from './Timer'
import TimerControllers from './TimerControllers'
import Sound from './Sound'
import '../App.css'



class App extends Component {
  render() {
    return (
      <div className="main">
        <h1>Pomodoro Timer</h1>
        <Timer />
        <TimerControllers />
        <Sound />
      </div>
    );
  }
}

// export default class App extends Component{
//   constructor () {
//     super()
//     this.state = {
//       cycle: "Session",
//       workTime: 25,
//       breakTime: 5,
//       sound: "on"
//     }
//   }
// }

export default App;
