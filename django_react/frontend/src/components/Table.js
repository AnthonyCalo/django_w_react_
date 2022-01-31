import React, {useState, useEffect} from 'react'

const Table =()=>{
    useEffect(()=>{
        console.log("The table component has mounted succescfully")
    }, [])
    return ( 
        <div>
            This is a table component
        </div>
     )
}


export default Table;