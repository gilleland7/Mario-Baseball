import './StandingsTable.css';

// Example of a data array that
// you might receive from an API
const data = [
    { Team: "Luigi Knights", W: 6, L: 0, GB: "-"},
    { Team: "Yoshi Eggs", W: 5, L: 1, GB: 1},
    { Team: "Mario Fireballs", W: 2, L: 4, GB: 4},
    { Team: "Peach Monarchs", W: 1, L: 5, GB: 5},
]

const division = "Mushroom";

function BattingStatsTable() {
    return (
        <div className="StatsTable">
            <table>
                <tr>
                    <th>{division}</th>
                    <th>W</th>
                    <th>L</th>
                    <th>GB</th>                
                </tr>
                {data.map((val, key) => {
                    return (
                        <tr key={key} className="rt-tr-group">
                            <td>{val.Team}</td>
                            <td>{val.W}</td>
                            <td>{val.L}</td>
                            <td>{val.GB}</td>
                        </tr>
                    )
                })}
            </table>
        </div>
    );
}
 
export default BattingStatsTable;