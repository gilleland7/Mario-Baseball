import React, { useState, useEffect } from "react";
import './InSeason.css';
import BattingStatsTable from './Table/BattingStatsTable';
import StandingsTable from './Table/StandingsTable';

function InSeason() {    
    const [userTeamData, setuserteamdata] = useState({
        teamLogo: null,
        teamName: null
    });

    const [teamsData, setteamsdata] = useState({
        teams: null,
        playerValues: null
    });
    
    const images = require.context('../public/Images/', true);

    const mzoneLogo = images('./lVl Logo.png');
    const superSluggersLogo = images('./Mario Super Sluggers Logo.png');

    let teamLogo = "";
    let teamName = "";
    let teamsIndex = 0;

    const statsLabels = ["Batting Stats", "Pitching Stats", "Defensive Stats"];
    let statsIndex = 0; 

    let playerIndex = 0;
    const playerStatsIndex = 11;
    const hitterStatsIndex = 1;
    const pitcherStatsIndex = 2;
    const defenseStatsIndex = 3;

    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from
        // flask server it will be redirected to proxy
        fetch("/userteam").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setuserteamdata({
                    teamLogo: data.teamLogo,
                    teamName: data.teamName
                });               
            })
        )

        fetch("/teams").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setteamsdata({
                    teams: data.teams,
                    playerValues: data.playerValues
                });               
            })
        );
    }, []);   

    function setUserTeamIndex(item, index){
        if (item === userTeamData.teamName){
            teamsIndex = index;
        }
    }

    function renderContent() {       
        if (userTeamData.teamLogo != null){
            teamLogo = images("./Teams/"+userTeamData.teamLogo);
        }

        if (teamsData.teams != null) {
            teamsData.teams.forEach(setUserTeamIndex);
            teamName = teamsData.teams[teamsIndex];
        }

        if (teamsData.playerValues != null){
            console.log(teamsData.playerValues);
        }

        return(
            <div className="body">
                <nav className="navbar background">
                    <div className="nav-list">
                        <div className="logo">
                            <img src={teamLogo} alt="Team Logo"/>
                        </div>
                    </div>
                </nav>
                <div className="container">
                        <div className="firstHalf">
                            <button className="text-big">
                                Play Game @ Bowser
                            </button>
                            <div className="text-small">
                                Last Game: <br/>
                                <div className = "lastGame">
                                    <div className="topTeam"> 
                                        &nbsp; Mario 6 <br/>
                                    </div>
                                    <div className="bottomTeam">
                                        &nbsp; Luigi 7 &lt;
                                    </div>
                                </div>
                            </div>
                            <div className="previous">
                                <button>Previous Seasons</button>
                            </div>
                            <div className="info">
                                <div className="year">2016</div>
                                <div className="version">v1.4</div>
                            </div>
                        </div>
                        <div className="secondHalf">
                            <div className="stats-container">
                                <div className = "team">
                                    <button className="text-big">
                                        &lt; {teamName} &gt;
                                    </button>
                                </div>
                                <div className = "stats">
                                    <button className="text-big">
                                        &lt; {statsLabels[statsIndex]} &gt;
                                    </button>
                                </div>
                            </div>
                            <BattingStatsTable/>
                            <div className="standingsText"> Standings </div>
                            <div className="standings">
                                <div className="division division-border division-border-right">
                                    <StandingsTable/>
                                </div>
                                <div className="division division-border">
                                    <StandingsTable/>
                                </div>
                            </div>
                        </div>
                </div>
                <nav className="navbar background">
                    <ul className="nav-list">
                        <div className="bottomLogo">
                            <img src={mzoneLogo} alt="mzone"/>
                        </div>
                        <div className="bottomLogo bottomRight">
                            <img src={superSluggersLogo} alt="Mario Super Sluggers"/>
                        </div>
                    </ul>
                </nav>
            </div>
        );
    }
    return ( 
        <div>{renderContent()}</div>
    );
}
export default InSeason