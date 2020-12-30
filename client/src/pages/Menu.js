import Item from "../components/Item"
import axios from "axios"
import { useEffect,useState } from "react";


const Menu = () => {

    const [items,setItems] = useState([])

    useEffect(() => {
        axios.get("http://localhost:8000/api/foods")
         .then((res) => {
            setItems(res.data.foods)
            console.log(items)
         })
         .catch(err => console.log(err))
    },[])


    if(items.length !== 0){
        return (
            <div>
                <h1 style={{ 
                    color:"black",
                    marginTop:"4%",
                    backgroundColor:"rgba(0,255,255,1)",
                    padding:"5px"
                }}> Menu Contains</h1>
                {
                items.map((item) => {
                return (
                    <Item key={item['id']} item={item} />
                )
                })}
            </div>    
        )
    } else {
        return <h1>No Items Available</h1>
    }
};

export default Menu;