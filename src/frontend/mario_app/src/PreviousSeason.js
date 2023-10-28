import React, { useState, useEffect } from "react";
import './PreviousSeason.css';

const PreviousSeason = ({ closeModal }) => {
        return(
                <div className='modal'>
                        <div className='topRow'>
                                <h2 className='text'>Previous Seasons</h2>
                                <button className = 'xButton' onClick={closeModal}>X</button>
                        </div>
                        <div className='previousTable'>
                                
                        </div>
                </div>
        );
};
export default PreviousSeason;