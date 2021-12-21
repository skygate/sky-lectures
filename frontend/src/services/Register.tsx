import axios from "axios";
const Register = (values:any)=>{
  const {username, password,confirmedPassword,email,firstName,lastName}= values
    axios.post('http://localhost:8000/api/register/', {
        
        
            username,
            password,
            password2:confirmedPassword,
            email,
            first_name:firstName,
            last_name:lastName
        
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error.response);
      });
}


const LogIn = ()=> {
    axios.get('http://localhost:8000/presentations'

    
  )
  .then(function (response) {
    console.log(response);
  })
  .catch(function (response) {
    console.log(response);
  });
}
export {Register, LogIn}