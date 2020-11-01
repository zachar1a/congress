import React from "react";
import Navbar from "../Navbar/Navbar";

import "./Home.css";

const Link = require("react-router-dom").Link;

class Home extends React.Component{


    render(){
            return(
		    <div>
		    	<h2 className="title">State Of Congress</h2>
		    	<Navbar />
		    </div>
            );
        };
}

export default Home;
