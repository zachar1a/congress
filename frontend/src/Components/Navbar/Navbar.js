import React from "react";
import "./Navbar.css";

import { Link } from "react-router-dom"



class Navbar extends React.Component{
	render(){
		return(
			<div>
				<ul className="navbar">
					<li><Link to="/">Home</Link></li>
					<li><Link to="/Bills">Bills</Link></li>
					<li><Link to="/Votes">Votes</Link></li>
				</ul>
			</div>
		);
	};
}

export default Navbar;
