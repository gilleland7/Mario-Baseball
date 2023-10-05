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
        <div class="StandingsTableClass">
            <table class="StandingsTable">
                <tr class="StandingsRow">
                    <th class="StandingsHeader">{division}</th>
                    <th class="StandingsHeader">W</th>
                    <th class="StandingsHeader">L</th>
                    <th class="StandingsHeader">GB</th>                
                </tr>
                {data.map((val, key) => {
                    return (
                        <tr key={key} class="StandingsRow rt-tr-group">
                            <td class="StandingsData">{val.Team}</td>
                            <td class="StandingsData">{val.W}</td>
                            <td class="StandingsData">{val.L}</td>
                            <td class="StandingsData">{val.GB}</td>
                        </tr>
                    )
                })}
            </table>
        </div>
    );
}
 
export default BattingStatsTable;