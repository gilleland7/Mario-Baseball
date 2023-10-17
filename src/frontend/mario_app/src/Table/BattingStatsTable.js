import './StatsTable.css';

let stats = null;
let war = null;
let names = null;
let sortedNames = null;

function BattingStatsTable({playerNames, playerStats, playerWar}) {
    if (playerNames != null){
        names = playerNames;
        sortedNames = [...names];
        sortedNames.sort();       
        console.log(names);
    }

    if (playerStats != null){ 
        stats = playerStats;
        console.log(stats);
    } 

    if (playerWar != null){
        war = playerWar;
        console.log(war);
    }

    if (stats != null && war != null && names != null){
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
                            <th className="StatsHeader">R</th>                          
                            <th className="StatsHeader">SO</th>
                            <th className="StatsHeader">BB</th>
                            <th className="StatsHeader">HBP</th>
                            <th className="StatsHeader">SH</th>
                            <th className="StatsHeader">BA</th>
                            <th className="StatsHeader">OBP</th>
                            <th className="StatsHeader">SLG</th>
                            <th className="StatsHeader">OPS</th>
                            <th className="StatsHeader">SB</th>
                            <th className="StatsHeader">CS</th>
                            <th className="StatsHeader">WAR</th>
                        </tr>
                        {sortedNames.map((name, index) => (
                            <tr key={index} className="StatsRow stat-tr-group">
                                <td className="StatsData">{name}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][0]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][1]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][2]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][3]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][4]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][5]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][6]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][7]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][8]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][9]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][10]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][11]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][12]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][13]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][14]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][15]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][16]}</td>
                                <td className="StatsData">{stats[names.indexOf(name)][17]}</td>
                                <td className="StatsData">{war[names.indexOf(name)]}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    }
}
export default BattingStatsTable;