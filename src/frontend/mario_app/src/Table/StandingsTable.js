import './StandingsTable.css';

// Example of a data array that
// you might receive from an API
const data = [
    { Team: "Luigi Knights", W: 6, L: 0, GB: "-"},
    { Team: "Yoshi Eggs", W: 5, L: 1, GB: 1},
    { Team: "Waluigi Spitballs", W: 2, L: 4, GB: 4},
    { Team: "Bowser Jr. Rookies", W: 111, L: 51, GB: 15},
]

const division = "Mushroom";

function BattingStatsTable() {
    return (
        <div className="StandingsTableClass">
            <table className="StandingsTable">
                <tbody>
                    <tr className="StandingsRow">
                        <th className="StandingsHeader">{division}</th>
                        <th className="StandingsHeader">W</th>
                        <th className="StandingsHeader">L</th>
                        <th className="StandingsHeader">GB</th>                
                    </tr>
                {data.map((val, key) => {
                    return (
                        <tr key={key} className="StandingsRow rt-tr-group">
                            <td className="StandingsData">{val.Team}</td>
                            <td className="StandingsData">{val.W}</td>
                            <td className="StandingsData">{val.L}</td>
                            <td className="StandingsData">{val.GB}</td>
                        </tr>
                    )
                })}
                 </tbody>
            </table>
        </div>
    );
}
 
export default BattingStatsTable;