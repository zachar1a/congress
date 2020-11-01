import React from "react";
import styles from "./Card.css";

class Card extends React.Component{
	render(){
		/*
		 * This needs to be dynamic styling for 
		 * the result in props, red if failed,
		 * green if passed
		 *
		 */

		const resultStyle={
			color:"green"
		};

		return (
			<div className="card">
				<h2>{this.props.chamber} {this.props.name}</h2>
				<h4>{this.props.title}</h4>
				<h3><span style={resultStyle}>{this.props.result}</span> {this.props.action}</h3>
			</div>
		);
	}
}

export default Card;
