'use client'
import { useState, useEffect } from 'react';

type Props = {
    url: string;
};

const Comp = ({ url = 'https://dummyjson.com/products' }: Props) => {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);
    const fetchData = async () => {
        try {
            const response = await fetch(url);
            const result = await response.json();
            setData(result);
        } catch (err) {
            setError(err);
        }
    };

    useEffect(() => {
        
        fetchData();
    }, [url]);

    if (error) {
        return <div>{error.message}</div>;
    }

    if (!data) {
        return <div>Loading...</div>;
    }

    return <div>{JSON.stringify(data)}</div>;
};

export default Comp;