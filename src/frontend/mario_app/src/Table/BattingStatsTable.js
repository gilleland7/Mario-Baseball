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
        <div class="StatsTableClass">
            <table class="StatsTable">
                <tr class="StatsRow">
                    <th class="StatsHeader">Player</th>
                    <th class="StatsHeader">PA</th>
                    <th class="StatsHeader">AB</th>
                    <th class="StatsHeader">H</th>
                    <th class="StatsHeader">2B</th>
                    <th class="StatsHeader">3B</th>
                    <th class="StatsHeader">HR</th>
                    <th class="StatsHeader">RBI</th>
                    <th class="StatsHeader">SH</th>
                    <th class="StatsHeader">SO</th>
                    <th class="StatsHeader">BB</th>
                    <th class="StatsHeader">HBP</th>
                    <th class="StatsHeader">BA</th>
                    <th class="StatsHeader">OBP</th>
                    <th class="StatsHeader">SLG</th>
                    <th class="StatsHeader">OPS</th>
                    <th class="StatsHeader">SB</th>
                    <th class="StatsHeader">CS</th>
                    <th class="StatsHeader">WAR</th>
                </tr>
                {data.map((val, key) => {
                    return (
                        <tr key={key} class="StatsRow rt-tr-group">
                            <td class="StatsData">{val.Player}</td>
                            <td class="StatsData">{val.PA}</td>
                            <td class="StatsData">{val.AB}</td>
                            <td class="StatsData">{val.H}</td>
                            <td class="StatsData">{val['2B']}</td>
                            <td class="StatsData">{val['3B']}</td>
                            <td class="StatsData">{val.HR}</td>
                            <td class="StatsData">{val.RBI}</td>
                            <td class="StatsData">{val.SH}</td>
                            <td class="StatsData">{val.SO}</td>
                            <td class="StatsData">{val.BB}</td>
                            <td class="StatsData">{val.HBP}</td>
                            <td class="StatsData">{val.BA}</td>
                            <td class="StatsData">{val.OBP}</td>
                            <td class="StatsData">{val.SLG}</td>
                            <td class="StatsData">{val.OPS}</td>
                            <td class="StatsData">{val.SB}</td>
                            <td class="StatsData">{val.CS}</td>
                            <td class="StatsData">{val.WAR}</td>
                        </tr>
                    )
                })}
            </table>
        </div>
    );
}
 
export default BattingStatsTable;