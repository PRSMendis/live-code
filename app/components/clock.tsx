'use client'
import React, { useState, useEffect } from 'react';

const Clock = () => {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const intervalId = setInterval(() => {
      Promise.resolve(new Date()).then(setTime);
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <h1>Current Time:</h1>
      <h2>{time.toLocaleTimeString()}</h2>
    </div>
  );
};

export default Clock;
