import './StatsTable.css';

let stats = null;
let names = null;
let sortedNames = null;

function DefensiveStatsTable({playerNames, playerStats}) {
    if (playerNames != null){
        names = playerNames;
        sortedNames = [...names];
        sortedNames.sort();       
    }

    if (playerStats != null){ 
        stats = playerStats;
    } 

    if (stats != null && war != null && names != null){
        return (
            <div className="StatsTableClass">
                <table className="StatsTable">
                    <tbody>
                        <tr className="StatsRow">
                            <th className="StatsHeader">Player</th>
                            <th className="StatsHeader">Put Outs</th>
                            <th className="StatsHeader">Nice Plays</th>
                            <th className="StatsHeader">Errors</th>
                        </tr>
                        {sortedNames.map((name, index) => (
                            <tr key={index} className="StatsRow stat-tr-group">
                                <td className="StatsData">{name}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][0]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][1]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][2]}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    }
}
export default DefensiveStatsTable;