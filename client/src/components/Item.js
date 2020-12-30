const Item = (props) => {

    return(
        <div className="item">
            <h2 style={{ 
                
                textAlign:"center",
                color:"White"
            
            }}>{props.item['name']}</h2>
            <h4 style={{
                color:"white"
            }}>Rs : {props.item['price']}</h4>
        </div>
    )


};

export default Item;