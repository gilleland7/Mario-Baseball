import React, { useState, useEffect } from "react";
import InSeason from "./InSeason";
import './main.css';
 
function Main() {
    const [data, setdata] = useState({
        state: null,
        year: null,
        version: null
    });
 
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from
        // flask server it will be redirected to proxy
        fetch("/state").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    state: data.state,
                    version: data.version,
                    year: data.year
                });
            })
        );
    }, []);   

    function renderContent() {
        if (data.state != null){
            if (data.state === 0){
                console.log("preseason");
            } else if (data.state === 1){
                return <InSeason yearDB={data.year} versionDB={data.version}/>;
            } else if (data.state === 2){
                console.log("playoffs")
            } else if (data.state === 3){
                console.log("end of season")
            }   
        }
    }
    return (
        <div className='main'>{renderContent()}</div>        
    );
}
export default Main