import './StandingsTable.css';

let division = null;
let divisionTeams = null;

function DivisionTable({div, divTeams}) {
    if (div != null){
        division = div;
        divisionTeams = divTeams;
        console.log(divisionTeams);

        return (
            <div className="StandingsTableClass">
                <table className="StandingsTable">
                    <tbody>
                        <tr className="StandingsRow">
                            <th className="StandingsHeader">{division}</th>
                            <th className="StandingsHeader">W</th>
                            <th className="StandingsHeader">L</th>
                            <th className="StandingsHeader">Ties</th>
                            <th className="StandingsHeader">GB</th>                
                        </tr>
                    {divisionTeams.map((row, index) =>  {
                        return (
                            <tr key={index} className="StandingsRow rt-tr-group">
                                <td className="StandingsData StandingsTeam">{row[0]}</td>
                                <td className="StandingsData">{row[1]}</td>
                                <td className="StandingsData">{row[2]}</td>
                                <td className="StandingsData">{row[3]}</td>
                                <td className="StandingsData">{row[4]}</td>
                            </tr>
                        )
                    })}
                    </tbody>
                </table>
            </div>
        );
    }
}
 
export default DivisionTable;