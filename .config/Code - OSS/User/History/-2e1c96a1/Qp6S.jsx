import React, { useEffect, useState } from 'react'
import axios from 'axios'
function App() {
   const [data,setData] = useState({})
  useEffect(()=>{
    const getData = await () => {
      const response = async axios.get('http://localhost:8000/api/snippet')
      setData(response.data)
      return response.data
    }
  },[])
  return (
    <div>App</div>
  )
}

export default App