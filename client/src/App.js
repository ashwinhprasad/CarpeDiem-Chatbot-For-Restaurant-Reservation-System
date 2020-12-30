import './App.css';
import { useState  } from 'react';
import axios from "axios";
import Menu from "./pages/Menu";
import Form from "./pages/Form"
import {BrowserRouter as Router,Route,Link} from 'react-router-dom'
 


function App() {

  const [searchBar,setSearchBar] = useState("");
  const [response,setResponse] = useState("");
  const [responseTag,setResponseTag] = useState("");

  const onChange = (e) => {
    e.preventDefault();
    setSearchBar(e.target.value);
  }

  const onSearch = (e) => {
    e.preventDefault();
    axios.post("http://127.0.0.1:8000/api/",{
      "input":searchBar
    })
    .then(res => {
      setResponse(res.data['model_response'])
      setResponseTag(res.data['response_tag'])
      setSearchBar("")
    })
    .catch(err => console.log(err))
  }

  const form = (e) => {
    if (responseTag === "menu") return <Link style={{
      textDecoration:"none"
    }} to="/menu"><p className="link-para">Look at the Menu</p></Link>;
    else if (responseTag === "reservation") return <Link style={{
      textDecoration:"none"
    }} to="/Reservation"><p className="link-para">Fill up the form</p></Link>;
    else return "";
  }

  const linkButtonStyle = () => {
    if(responseTag !== "menu" && responseTag !== "reservation") {
      return {
        visibility:"hidden"
      }
    } else {
      return {
        visibility:"visible"
      }
    }
  }


  return (
    <Router>
      <Route exact path="/">
        <div className="App">
          <div className="header-back">
            <h1 style={{
              fontFamily: "Rajdhani, sans-serif"
            }}>Carpe Diem</h1>
          </div>
          <div className="response" >
            <h2 style={{
              fontFamily: "Oswald, sans-serif"
            }}>{response}</h2>
          </div>
          <div className="input-form">
            <input autoComplete="off" id="search-box" type='text' name="search-box" value={searchBar} onChange={onChange} />
            <button id="submit-button" onClick={onSearch} >Ask</button>
          </div>
          <button style={linkButtonStyle()} className="link-button" >{form()}</button>
        </div>
      </Route>
      <Route exact path="/menu">
        <Menu />
      </Route>
      <Route exact path="/Reservation">
        <Form />
      </Route>  
    </Router>
  );
}

export default App;
