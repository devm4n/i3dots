import React, { useEffect, useState } from 'react'
import axios from 'axios'
function App() {
   const [data,setData] = useState({})
  useEffect(()=>{
    const getData = async () => {
      const response = await axios.get('http://127.0.0.1:8000/api/snippet')
      setData(response.data)
      return response.data
    }
  })
  return (
    <>
    {
      console.log(data)
    }
    <div>App</div>
    </>
  )
}

export default App