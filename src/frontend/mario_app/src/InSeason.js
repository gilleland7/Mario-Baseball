import React, { useState, useEffect } from "react";
import './InSeason.css';
import BattingStatsTable from './Table/BattingStatsTable';
import StandingsTable from './Table/StandingsTable';

let year = 2023;
let version = "v1.0";

function InSeason({yearDB, versionDB}) { 
 
    if (yearDB != null && versionDB != null){
        year = yearDB;
        version = "v"+versionDB.toString();
    }
    
    const [userTeamData, setuserteamdata] = useState({
        teamLogo: null,
        teamName: null
    });

    const [teamsData, setteamsdata] = useState({
        teams: null,
        playerValues: null
    });

    const [statsData] = useState({
        warStats: null,
        batterStats: null,
        pticherStats: null,
        defenseStats: null,
        names: null
    });
    
    const [divisionData, setdivisiondata] = useState({
        divisions: null,
        divisionOne: null,
        divisionTwo: null
    });

    const images = require.context('../public/Images/', true);

    const mzoneLogo = images('./lVl Logo.png');
    const superSluggersLogo = images('./Mario Super Sluggers Logo.png');

    let teamLogo = "";
    let teamName = "";
    let teamsIndex = 0;
    let divisions = [];
    let divisionOneData = [];
    let divisionTwoData = [];

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
        )

        fetch("/divisions").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdivisiondata({
                    divisions: data.divisions,
                    divisionOne: data.divisionOneTeams,
                    divisionTwo: data.divisionTwoTeams
                });               
            })
        );
    }, []);   

    function setUserTeamIndex(item, index) {
        if (item === userTeamData.teamName){
            teamsIndex = index;
        }
    }

    function changeTeam(direction) {
        console.log("HERE " + direction);
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
            let team = teamsData.playerValues[teamName];
            let length = team.length;

            statsData.warStats = [];
            statsData.batterStats = [];
            statsData.pitcherStats = [];
            statsData.defenseStats = [];
            statsData.names = [];

            while(playerIndex < length){                
                statsData.warStats.push(team[playerIndex][playerStatsIndex][0]); //WAR
                statsData.batterStats.push(team[playerIndex][playerStatsIndex][hitterStatsIndex]);
                statsData.pitcherStats.push(team[playerIndex][playerStatsIndex][pitcherStatsIndex]);
                statsData.defenseStats.push(team[playerIndex][playerStatsIndex][defenseStatsIndex]);
                statsData.names.push(team[playerIndex][0]);

                playerIndex++;
            }

            playerIndex = 0;
            console.log(teamsData.playerValues);
        }

        if (divisionData.divisions != null){
            divisions = divisionData.divisions;
            divisionOneData = divisionData.divisionOne;
            divisionTwoData = divisionData.divisionTwo;
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
                                <div className="year">{year}</div>
                                <div className="version">{version}</div>
                            </div>
                        </div>
                        <div className="secondHalf">
                            <div className="stats-container">
                                <div className = "team">
                                    <div className="flexContainer">
                                        <div className="text-big arrowLeft" onClick={() => changeTeam(-1)}>&lt;</div>
                                        <div className="text-big teamName">{teamName}</div>
                                        <div className="text-big arrowRight" onClick={() => changeTeam(1)}>&gt;</div>
                                    </div>
                                </div>
                                <div className = "stats">
                                    <div className="flexContainer">
                                        <div className="text-big arrowLeftStats">&lt;</div>
                                        <div className="text-big statsName">{statsLabels[statsIndex]}</div>
                                        <div className="text-big arrowRightStats">&gt;</div>
                                    </div>
                                </div>
                            </div>
                            <BattingStatsTable playerNames={statsData.names} playerStats={statsData.batterStats} playerWar={statsData.warStats} />
                            <div className="standingsText"> Standings </div>
                            <div className="standings">
                                <div className="division division-border division-border-right">
                                    <StandingsTable div={divisions[0]} divTeams={divisionOneData} />
                                </div>
                                <div className="division division-border">
                                    <StandingsTable div={divisions[1]} divTeams={divisionTwoData}/>
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