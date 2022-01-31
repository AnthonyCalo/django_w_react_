import React, {useState} from 'react';
import ReactDOM from 'react-dom';
import Table from "./Table"
import Dashboard from './leads/Dashboard';

const App=()=>{
    const [inputVal, setInputVal] = useState("")
    return ( 
        <div>

        <h1>React App</h1>
        <input value={inputVal} onChange={(e)=>setInputVal(e.target.value)} type="text"></input>
        <h2>{inputVal}</h2>
        <Table/>
        <Dashboard />
        </div>
    )
}

export default App