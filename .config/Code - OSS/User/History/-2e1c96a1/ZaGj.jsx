import React, { useEffect, useState } from 'react'
import axios from 'axios'
function App() {
  const [data, setData] = useState()
  useEffect(() => {
    const getData = async () => {
      const response = await axios.get('http://localhost:8000/api/snippet')
      setData(response.data)
      return response.data
    }
    getData()
  }, [])
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