import React from "react";
import Navbar from "../Navbar/Navbar";
import LatestBill from "../LatestBill/LatestBill";

import "./Home.css";

//const Link = require("react-router-dom").Link;

class Home extends React.Component{


    render(){
            return(
		    <div>
		    	<h2 className="title">State Of Congress</h2>
		    	<Navbar />
		    	<LatestBill />
		    </div>
            );
        };
}

export default Home;
