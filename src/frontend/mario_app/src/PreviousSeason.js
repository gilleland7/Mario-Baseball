import React, { useState, useEffect } from "react";
import './PreviousSeason.css';
import './Table/StandingsTable.css';

const PreviousSeason = ({ closeModal }) => {
        const [isLoading, setIsLoading] = useState(true);

        const [previousData, setpreviousdata] = useState({
                seasons: null
         });

        // Using useEffect for single rendering
        useEffect(() => {
                // Using fetch to fetch the api from
                // flask server it will be redirected to proxy
                fetch("/previous").then((res) =>
                res.json().then((data) => {
                        // Setting a data from api
                        setpreviousdata({
                                seasons: data.seasons
                        }); 
                        
                        setIsLoading(false);
                })
                );
        }, []);   


        function renderContent() {                      
                if (!isLoading) {  
                        console.log(previousData.seasons);           
                        return(
                                <div className='modal'>
                                        <div className='topRow'>
                                                <h2 className='text'>Previous Seasons</h2>
                                                <button className = 'xButton' onClick={closeModal}>X</button>
                                        </div>
                                        <div className="StatsTableClass">
                                                <table className="StatsTable">
                                                        <tbody>
                                                                <tr className="StatsRow">
                                                                <th className="StatsHeader">Year</th>
                                                                <th className="StatsHeader">Champion</th>
                                                                <th className="StatsHeader">Runner Up</th>
                                                                <th className="StatsHeader">Mushroom Runner Up</th>
                                                                <th className="StatsHeader">Flower Runner Up</th>
                                                                <th className="StatsHeader">MVP</th>
                                                                <th className="StatsHeader">Cy Young</th>
                                                                <th className="StatsHeader">Silver Slugger</th>
                                                                <th className="StatsHeader">Gold Glove</th>                          
                                                                <th className="StatsHeader">Reliever of the Year</th>
                                                                <th className="StatsHeader">Comeback Player of the Year</th>
                                                                </tr>
                                                                {previousData.seasons.map((year, index) => (
                                                                <tr key={index} className="StatsRow stat-tr-group">
                                                                        <td className="StatsData">{year}</td>
                                                                        <td className="StatsData">{previousData.seasons[1]}</td>
                                                                        <td className="StatsData">{previousData.seasons[2]}</td>
                                                                        <td className="StatsData">{previousData.seasons[3]}</td>
                                                                        <td className="StatsData">{previousData.seasons[4]}</td>
                                                                        <td className="StatsData">{previousData.seasons[5][0]}</td>
                                                                        <td className="StatsData">{previousData.seasons[5][1]}</td>
                                                                        <td className="StatsData">{previousData.seasons[5][2]}</td>
                                                                        <td className="StatsData">{previousData.seasons[5][3]}</td>
                                                                        <td className="StatsData">{previousData.seasons[5][4]}</td>
                                                                        <td className="StatsData">{previousData.seasons[5][5]}</td>
                                                                </tr>
                                                                ))}
                                                        </tbody>
                                                </table>
                                        </div>
                                </div>
                        );
                }
        }
        return ( 
                <div>{renderContent()}</div>
            );
};
export default PreviousSeason;