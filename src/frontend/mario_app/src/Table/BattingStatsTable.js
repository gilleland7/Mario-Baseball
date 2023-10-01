import './StatsTable.css';

// Example of a data array that
// you might receive from an API
const data = [
    { Player: "Luigi", PA: 23, AB: 50, '3B': 1, WAR: 10.1},
    { Player: "Mario", PA: 3, AB: 1, '2B': 1, SLG: '.156%', WAR: 11},
    { Player: "Bowser", PA: 3, AB: 1, '2B': 1, SLG: '.156%', WAR: 11},
    { Player: "Peach", PA: 3, AB: 1, '2B': 1, SLG: '.156%', WAR: 11},
    { Player: "Birdo", PA: 3, AB: 1, '2B': 1, SLG: '.156%', WAR: 11},
    { Player: "Yoshi", PA: 3, AB: 1, '2B': 1, SLG: '.156%', WAR: 11},
    { Player: "Wario", PA: 3, AB: 1, '2B': 1, SLG: '.156%', WAR: 11},
    { Player: "Diddy Kong", PA: 3, AB: 1, '2B': 1, SLG: '.156%', WAR: 11},
    { Player: "King K. Ruel", PA: 3, AB: 1, '2B': 1, SLG: '.156%', WAR: 11},
]

function BattingStatsTable() {
    return (
        <div className="StatsTable">
            <table>
                <tr>
                    <th>Player</th>
                    <th>PA</th>
                    <th>AB</th>
                    <th>H</th>
                    <th>2B</th>
                    <th>3B</th>
                    <th>HR</th>
                    <th>RBI</th>
                    <th>SH</th>
                    <th>SO</th>
                    <th>BB</th>
                    <th>HBP</th>
                    <th>BA</th>
                    <th>OBP</th>
                    <th>SLG</th>
                    <th>OPS</th>
                    <th>SB</th>
                    <th>CS</th>
                    <th>WAR</th>
                </tr>
                {data.map((val, key) => {
                    return (
                        <tr key={key} className="rt-tr-group">
                            <td>{val.Player}</td>
                            <td>{val.PA}</td>
                            <td>{val.AB}</td>
                            <td>{val.H}</td>
                            <td>{val['2B']}</td>
                            <td>{val['3B']}</td>
                            <td>{val.HR}</td>
                            <td>{val.RBI}</td>
                            <td>{val.SH}</td>
                            <td>{val.SO}</td>
                            <td>{val.BB}</td>
                            <td>{val.HBP}</td>
                            <td>{val.BA}</td>
                            <td>{val.OBP}</td>
                            <td>{val.SLG}</td>
                            <td>{val.OPS}</td>
                            <td>{val.SB}</td>
                            <td>{val.CS}</td>
                            <td>{val.WAR}</td>
                        </tr>
                    )
                })}
            </table>
        </div>
    );
}
 
export default BattingStatsTable;