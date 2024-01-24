'use client'
import { useEffect, useState } from "react"

export default function Beers({ url = 'https://api.punkapi.com/v2/beers' }) {

    const [data, setData] = useState(null);
    const [error, setError] = useState(null);
    const [filter, setFilter] = useState('')
    
    const fetchData = async (filter) => {
        try {
            // https://api.punkapi.com/v2/beers?name=buzz

            // const queryUrl = url
            let queryUrl = url 
            if (filter) {
            queryUrl = url + '?beer_name=' + filter
        }
            console.log('queryUrl: ', queryUrl);
            const response = await fetch(queryUrl);
            const result = await response.json();
            console.log('result: ', result);
            setData(result);
        } catch (err) {
            console.log('there is an error')
            console.error(error)
            setError(err);
        }
    };

    const changeFilter = (e) => {
        console.log(e.target.value)
        setFilter(e.target.value)
        console.log(filter)
    }

    useEffect(() => {
        console.log('test')
        fetchData(filter)

    },[filter])
    
    return (
        <main className="h-1/1, w1/1">
            <div>test</div>
            {/* header */}
            {/* Search Bar */}
            <input type="text" onChange={changeFilter}></input>
            {/* List of Beers */}
            {/*  */}
            {data && data.map((beer) => 
            <div>{beer.name}</div>
            )}
        </main>
    )
}