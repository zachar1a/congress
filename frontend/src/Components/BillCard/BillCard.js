import React from "react";
import styles from "./BillCard.css";

class BillCard extends React.Component{
	render(){
		/*
		 * This needs to be dynamic styling for 
		 * the result in props, red if failed,
		 * green if passed
		 *
		 */

		return (
			<div className="BillCard">
				<h2>[{this.props.sponsorParty}] {this.props.sponsor} {this.props.sponsorState}</h2>
				<h3>{this.props.billid} {this.props.title}</h3>
				<a href={this.props.infoUrl}>{this.props.slug} Info</a>
			</div>
		);
	}
}

export default BillCard;
