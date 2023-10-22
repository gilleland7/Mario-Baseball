import './StatsTable.css';

let stats = null;
let names = null;
let sortedNames = null;

function PitchingStatsTable({playerNames, playerStats}) {
    if (playerNames != null){
        names = playerNames;
        sortedNames = [...names];
        sortedNames.sort();       
    }

    if (playerStats != null){ 
        stats = playerStats;
    } 

    if (stats != null && names != null){
        return (
            <div className="StatsTableClass">
                <table className="StatsTable">
                    <tbody>
                        <tr className="StatsRow">
                            <th className="StatsHeader">Player</th>
                            <th className="StatsHeader">IP</th>
                            <th className="StatsHeader">G</th>
                            <th className="StatsHeader">BB</th>
                            <th className="StatsHeader">H</th>
                            <th className="StatsHeader">R</th>
                            <th className="StatsHeader">ER</th>
                            <th className="StatsHeader">HR</th>
                            <th className="StatsHeader">ERA</th>                          
                            <th className="StatsHeader">W</th>
                            <th className="StatsHeader">L</th>
                            <th className="StatsHeader">S</th>
                            <th className="StatsHeader">HLD</th>
                            <th className="StatsHeader">WHIP</th>
                            <th className="StatsHeader">K</th>
                            <th className="StatsHeader">HBP</th>
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
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    }
}
export default PitchingStatsTable;