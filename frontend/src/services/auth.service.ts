import axios from "axios";

const API_URL = "http://localhost:8000/api/";


const loginAuth = (username:string, password:string) => {
  return axios
    .post(API_URL +  {
      username,
      password,
    })
    .then((response) => {
      if (response.data.accessToken) {
        localStorage.setItem("user", JSON.stringify(response.data));
      }

      return response.data;
    });
};
export default loginAuth