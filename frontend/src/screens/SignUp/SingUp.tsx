import "./SignUp.modules.scss";
import background from "../../assets/background.svg";
import PasswordInput from "../../components/Inputs/PasswordInput";
import TextInput from "../../components/Inputs/TextInput";
import { useFormik } from "formik";
import { Link } from "react-router-dom";
const SignUp = () => {
  const formik = useFormik({
    initialValues: {
      login: "",
      email: "",
      password: "",
    },

    onSubmit: async (values) => {
      console.log(values);
    },
  });
  return (
    <div className="main-container">
      <div className="sign-container">
        <div className="title">Let's get started!</div>
        <div className="subtitle">It's pleasure to meet you</div>
        <form onSubmit={formik.handleSubmit}>
          <TextInput
            placeholder="login"
            name="login"
            value={formik.values.login}
            onChange={formik.handleChange}
          ></TextInput>
          <TextInput
            placeholder="email"
            name="email"
            value={formik.values.email}
            onChange={formik.handleChange}
          ></TextInput>
          <PasswordInput
            name="password"
            value={formik.values.password}
            onChange={formik.handleChange}
          />

          <button type="submit" className="submit-btn">
            Sign Up
          </button>
        </form>
        <div>
          Already have an account <Link to="/SignIn">Sign In</Link>
        </div>
      </div>
      <div className="background-container">
        <img src={background} className="background" alt="background" />
      </div>
    </div>
  );
};
export default SignUp;
