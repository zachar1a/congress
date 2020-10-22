import React , { Component } from "react";
import logo from './logo.svg';
import './App.css';

function Welcome(props){
	return <h1>Hello, {props.name}</h1>
}

function App() {
  return (
    <div className="App">
	  <Welcome name="zachary"/>
	  <h2>Hello world</h2>
    </div>
  );
}

export default App;
