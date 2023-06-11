import { useState, useEffect } from 'react'
import {LoginScreen} from "./screns/login"
import { ListScreen } from './screns/list'
import { API } from './api'
 
function App() {
  
  const [isLogin, setIsLogin] = useState(false)

  useEffect(() => {
    try{
      API.get("/me").then((res) => {
        setIsLogin(true)
      })
    }catch{}
  }, [])

  if(isLogin){
    return <ListScreen/>
  }
  return <LoginScreen/>
}

export default App
