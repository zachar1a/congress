import React from "react"


class BillData extends React.Component{

	constructor(props){
		super(props);
		this.state={
			billData:[],
		};
	}

	componentDidMount(){
		console.log("mounting");
	}

	render(){
		return(
			<div className="BillData">
			<h2>Hello world this is the bill data</h2>
			</div>
		);
	};
}

export default BillData;
