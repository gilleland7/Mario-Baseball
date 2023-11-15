import React, { useState, useEffect } from "react";
import './PlayGame.css';

const [teams, setteamsdata] = useState({
    home: null,
    homeCharacters: null,
    away: null,
    awayCharacters: null
});

const PlayGame = ({ closeModal, awayTeam, homeTeam }) => {
        const [isLoading, setIsLoading] = useState(true);

        // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from
        // flask server it will be redirected to proxy
       const fetchUser = fetch("/teambyname").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setteamsdata({
                    home: data.team,
                    homeCharacters: data.characterValues
                });               
            })
        );

        // Use Promise.all to wait for all fetch requests to complete
        Promise.all([fetchUser, fetchTeams, fetchDivision, fetchPrevious, fetchNextGame])
        .then(() => {
          setIsLoading(false);
        })
    }, []); 
        
        setteamsdata({
            away: awayTeam,
            home: homeTeam
        });

        setIsLoading(true);

        function renderContent() {                      
                if (!isLoading) {            
                        return(
                                <div className='modalPlayGame'>
                                    <div className='topRow'>
                                            <button className='xButtonPlayGame' onClick={closeModal}>X</button>
                                    </div>
                                    <div className="stats">
                                        <div className='awayTeam'>
                                            <div className='teamHeader'></div>
                                            <div className='statsTable'></div>
                                            <div className='score'></div>
                                        </div>
                                        <div className='homeTeam'>
                                            <div className='teamHeader'></div>
                                            <div className='statsTable'></div>
                                            <div className='score'></div>
                                        </div>
                                    </div>
                                    <div className='submitRow'>
                                        <button className='submitButton'>Finish Game</button>
                                    </div>
                                </div>
                        );
                }
        }
        return ( 
                <div>{renderContent()}</div>
            );
};
export default PlayGame;