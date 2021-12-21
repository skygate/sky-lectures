import axios from "axios";
const Register = ()=>{
    axios.post('http://localhost:8000/api/register/', {
        
        
            "username": "asd",
            "password": "asd",
            "password2": "asd",
            "email": "asd",
            "first_name": "asd",
            "last_name": "asd"
        
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (response) {
        console.log(response);
      });
}
export default Register