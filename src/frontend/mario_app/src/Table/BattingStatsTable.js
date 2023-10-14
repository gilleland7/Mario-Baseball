import './StatsTable.css';

// Example of a data array that
// you might receive from an API
const data = [
    { Player: "Luigi", PA: 23, AB: 50, H:1, '2B':2, '3B': 1, HR:5, RBI:10, SH:0, SO:0, BB:1, HBP:0, BA:.256, OBP:1.000, SLG: 0.000, OPS: 0.123, SB:10, CS:1, WAR: 10.1},
    { Player: "Mario", PA: 3, AB: 1, '2B': 1, SLG: '.156', WAR: 11},
    { Player: "Bowser", PA: 3, AB: 1, '2B': 1, SLG: '.156', WAR: 11},
    { Player: "Peach", PA: 3, AB: 1, '2B': 1, SLG: '.156', WAR: 11},
    { Player: "Birdo", PA: 3, AB: 1, '2B': 1, SLG: '.156', WAR: 11},
    { Player: "Yoshi", PA: 3, AB: 1, '2B': 1, SLG: '.156', WAR: 11},
    { Player: "Wario", PA: 3, AB: 1, '2B': 1, SLG: '.156', WAR: 11},
    { Player: "Diddy Kong", PA: 3, AB: 1, '2B': 1, SLG: '.156', WAR: 11},
    { Player: "King K. Ruel", PA: 3, AB: 1, '2B': 1, SLG: '.156', WAR: 11},
]

function BattingStatsTable() {
    return (
        <div className="StatsTableClass">
            <table className="StatsTable">
                <tbody>
                    <tr className="StatsRow">
                        <th className="StatsHeader">Player</th>
                        <th className="StatsHeader">PA</th>
                        <th className="StatsHeader">AB</th>
                        <th className="StatsHeader">H</th>
                        <th className="StatsHeader">2B</th>
                        <th className="StatsHeader">3B</th>
                        <th className="StatsHeader">HR</th>
                        <th className="StatsHeader">RBI</th>
                        <th className="StatsHeader">SH</th>
                        <th className="StatsHeader">SO</th>
                        <th className="StatsHeader">BB</th>
                        <th className="StatsHeader">HBP</th>
                        <th className="StatsHeader">BA</th>
                        <th className="StatsHeader">OBP</th>
                        <th className="StatsHeader">SLG</th>
                        <th className="StatsHeader">OPS</th>
                        <th className="StatsHeader">SB</th>
                        <th className="StatsHeader">CS</th>
                        <th className="StatsHeader">WAR</th>
                    </tr>
                {data.map((val, key) => {
                    return (
                        <tr key={key} className="StatsRow stat-tr-group">
                            <td className="StatsData">{val.Player}</td>
                            <td className="StatsData">{val.PA}</td>
                            <td className="StatsData">{val.AB}</td>
                            <td className="StatsData">{val.H}</td>
                            <td className="StatsData">{val['2B']}</td>
                            <td className="StatsData">{val['3B']}</td>
                            <td className="StatsData">{val.HR}</td>
                            <td className="StatsData">{val.RBI}</td>
                            <td className="StatsData">{val.SH}</td>
                            <td className="StatsData">{val.SO}</td>
                            <td className="StatsData">{val.BB}</td>
                            <td className="StatsData">{val.HBP}</td>
                            <td className="StatsData">{val.BA}</td>
                            <td className="StatsData">{val.OBP}</td>
                            <td className="StatsData">{val.SLG}</td>
                            <td className="StatsData">{val.OPS}</td>
                            <td className="StatsData">{val.SB}</td>
                            <td className="StatsData">{val.CS}</td>
                            <td className="StatsData">{val.WAR}</td>
                        </tr>
                    )
                })}
                </tbody>
            </table>
        </div>
    );
}
 
export default BattingStatsTable;