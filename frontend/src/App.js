import React from "react";
import BillInfo from './Components/BillInfo/BillInfo'
import VoteResults from './Components/VoteResults/VoteResults'
import Home from './Components/Home/Home'
import './App.css';


const Route = require("react-router-dom").Route;
const Switch = require("react-router-dom").Switch;


function App() {
	/*
	const voteTitleStyle={
		width:"40%",
		margin:"auto"
	};
	const BillTitleStyle={
		width:"40%",
		margin:"auto"
	};
	*/
  return (
    <div className="App">
	  <main>
	  <Switch>
	 	<Route path="/" component={Home} exact/>
	 	<Route path="/Bills" component={BillInfo} exact/>
	 	<Route path="/votes" component={VoteResults} exact/>
	  </Switch>
	  </main>
    </div>
  );
}

export default App;
