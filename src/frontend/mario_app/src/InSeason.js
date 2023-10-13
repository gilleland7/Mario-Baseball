import React from 'react';
import './InSeason.css';
import BattingStatsTable from './Table/BattingStatsTable';
import StandingsTable from './Table/StandingsTable';

import teamLogo from "./Images/Teams/Luigi Knights logo.png"
import mzoneLogo from "./Images/lVl Logo.png"
import superSluggersLogo from "./Images/Mario Super Sluggers Logo.png"

function InSeason() {    
    return (
        <div class="body">
            <nav class="navbar background">
                <div class="nav-list">
                    <div class="logo">
                        <img src={teamLogo} alt="Team Logo"/>
                    </div>
                    <li><a>Luigi Knights</a></li>
                </div>
            </nav>
            <div class="container">
                    <div class="firstHalf">
                        <button class="text-big">
                            Play Game @ Bowser
                        </button>
                        <p class="text-small">
                            Last Game: <br/>
                            <div class = "lastGame">
                                <div class="topTeam"> 
                                    &nbsp; Mario 6 <br/>
                                </div>
                                <div class="bottomTeam">
                                    &nbsp; Luigi 7 &lt;
                                </div>
                            </div>
                        </p>
                        <div class="previous">
                            <button>Previous Seasons</button>
                        </div>
                        <div class="info">
                            <div class="year">2016</div>
                            <div class="version">v1.4</div>
                        </div>
                    </div>
                    <div class="secondHalf">
                        <div class="stats-container">
                            <div class = "team">
                                <button class="text-big">
                                    &lt; Luigi Knights &gt;
                                </button>
                            </div>
                            <div class = "stats">
                                <button class="text-big">
                                    &lt; Batting Stats &gt;
                                </button>
                            </div>
                        </div>
                        <BattingStatsTable/>
                        <div class="standingsText"> Standings </div>
                        <div class="standings">
                            <div class="division division-border division-border-right">
                                <StandingsTable/>
                            </div>
                            <div class="division division-border">
                                <StandingsTable/>
                            </div>
                        </div>
                    </div>
            </div>
            <nav class="navbar background">
                <ul class="nav-list">
                    <div class="bottomLogo">
                        <img src={mzoneLogo} alt="mzone"/>
                    </div>
                    <div class="bottomLogo bottomRight">
                        <img src={superSluggersLogo} alt="Mario Super Sluggers"/>
                    </div>
                </ul>
            </nav>
        </div>
    )
}
  
export default InSeason