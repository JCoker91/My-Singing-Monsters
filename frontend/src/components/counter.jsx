import React from 'react'

const Counter = () => {
    const [count, setCount] = useState(0);
    setCount () => {count++};
  return (
    <>
        <h1>Hi There!</h1>
    </>
  )
}

export default Counter
