import React, { useState, useEffect } from "react";
import './PlayGame.css';

const PlayGame = ({ closeModal }) => {
        const [isLoading, setIsLoading] = useState(false);

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