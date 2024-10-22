// importing the modules
import { useState } from "react";
import axios from "axios"

// form page component
const Form = () => {

    // state varaibles
    const [fields,setFields] = useState({
        time:"",
        date:"",
        success:"",
        phone:""
    })

    // onchanging time field
    const timeChange = (e) => {
        e.preventDefault();
        setFields({
            time:e.target.value,
            date:fields.date,
            success:fields.success,
            phone:fields.phone
        })
    }

    // onchanging date field
    const dateChange = (e) => {
        e.preventDefault();
        setFields({
            time:fields.time,
            date:e.target.value,
            success:fields.success,
            phone:fields.phone
        })
    }

    // onchanging phone field
    const phoneChange = (e) => {
        e.preventDefault();
        setFields({
            time:fields.time,
            date:fields.date,
            success:fields.success,
            phone:e.target.value
        })
    }

    // on submitting the form
    const onSubmit = (e) => {
        e.preventDefault();

        // post request to the server
        axios.post("http://localhost:8000/api/reservation/",{
            time: fields.date.toString().concat(" "+fields.time.toString()),
            phone_no: fields.phone
        })
         .then(res => console.log(res.data))
         .catch(err => console.log(err))

        // set fields to blank
        if(fields.time !== "" && fields.date !== ""){
            setFields({
                time:"",
                date:"",
                phone:"",
                success:"Reservation Succesfully made"
            })
        }
    }

    
    // on successfuly making the reservation
    const successResponse = () => {
        
        if(fields.success === "Reservation Succesfully made"){
        return (
            <div className="success-response">
                <p>{fields.success}</p>
                <img style={{ marginLeft:"5px" }} width="30px" height="30px" src="https://www.kindpng.com/picc/m/136-1366226_green-thumbs-up-png-black-and-white-stock.png" alt="thumbs up" />
            </div>
        )
        }
        else {
            return <div></div>
        }
    }

    return(
        <div className="form-div">
            <form className="reservation-form">
            <input style={{
                marginTop:"10px",
                "borderRadius":"2px",
            }} value={fields.time} onChange={timeChange} type='time' />
            <input style={{
                marginTop:"10px",
                "borderRadius":"2px",
            }} value={fields.date} onChange={dateChange} type="date" />
            <input style={{
                marginTop:"10px",
                "borderRadius":"2px",
                padding:"5px"
            }} placeholder="Phone Number" value={fields.phone} onChange={phoneChange} type="text" />
            <button style={{
                borderRadius:"10px",
                padding:"5px",
                marginTop:"10px",
                width:"80%",
                border:"none",
                marginBottom:"10px",
                marginLeft:"10%"  
            }} onClick={onSubmit}>Make Reservation</button>
            </form>
            {successResponse()}
        </div>
    )
}

// exports
export default Form;
