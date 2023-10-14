import React, { useState, useEffect } from "react";
import InSeason from "./InSeason";
 
function Main() {
    const [data, setdata] = useState({
        state: 0,
        teamName: ""
    });
 
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from
        // flask server it will be redirected to proxy
        fetch("/data").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    state : data.state,
                    teamName: data.teamName
                });
            })
        );
    }, []);   

    function renderContent() {
        console.log(data.teamName)
        if (data.state === 0){
            console.log("preseason");
        } else if (data.state === 1){
            console.log("season")
            return <InSeason/>;
        } else if (data.state === 2){
            console.log("playoffs")
        } else if (data.state === 3){
            console.log("end of season")
        }   
    }
    return (
        <div>{renderContent()}</div>        
    );
}
export default Main