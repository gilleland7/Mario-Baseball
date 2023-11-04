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
                        return(
                                <div className='modal'>
                                        <div className='topRow'>
                                                <h2 className='text'>Previous Seasons</h2>
                                                <button className='xButton' onClick={closeModal}>X</button>
                                        </div>
                                        <div className="StatsTableClass Previous">
                                                <table className="StatsTable">
                                                        <tbody>
                                                                <tr className="StatsRow">
                                                                        <th className="StatsHeader PreviousHeader">Year</th>
                                                                        <th className="StatsHeader PreviousHeader">Champion</th>
                                                                        <th className="StatsHeader PreviousHeader">Runner Up</th>
                                                                        <th className="StatsHeader PreviousHeader">Mushroom Runner Up</th>
                                                                        <th className="StatsHeader PreviousHeader">Flower Runner Up</th>
                                                                        <th className="StatsHeader PreviousHeader">MVP</th>
                                                                        <th className="StatsHeader PreviousHeader">Cy Young</th>
                                                                        <th className="StatsHeader PreviousHeader">Silver Slugger</th>
                                                                        <th className="StatsHeader PreviousHeader">Gold Glove</th>                          
                                                                        <th className="StatsHeader PreviousHeader">Reliever of the Year</th>
                                                                        <th className="StatsHeader PreviousHeader">Comeback Player of the Year</th>
                                                                </tr>
                                                                {previousData.seasons.map((season, index) => (
                                                                <tr key={index} className="StatsRow stat-tr-group">
                                                                        <td className="StatsData">{season[0]}</td>
                                                                        <td className="StatsData">{season[1]}</td>
                                                                        <td className="StatsData">{season[2]}</td>
                                                                        <td className="StatsData">{season[3]}</td>
                                                                        <td className="StatsData">{season[4]}</td>
                                                                        <td className="StatsData">{season[5][0]}</td>
                                                                        <td className="StatsData">{season[5][1]}</td>
                                                                        <td className="StatsData">{season[5][2]}</td>
                                                                        <td className="StatsData">{season[5][3]}</td>
                                                                        <td className="StatsData">{season[5][4]}</td>
                                                                        <td className="StatsData">{season[5][5]}</td>
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