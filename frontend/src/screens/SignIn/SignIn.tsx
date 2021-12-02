import "../SignUp/SignUp.modules.scss";
import background from "../../assets/background.svg";
import PasswordInput from "../../components/Inputs/PasswordInput";
import TextInput from "../../components/Inputs/TextInput";
import { useFormik } from "formik";
import { Link } from "react-router-dom";
const SignUp = () => {
  const formik = useFormik({
    initialValues: {
      login: "",
      password: "",
    },

    onSubmit: async (values) => {
      console.log(values);
    },
  });
  return (
    <div className="main-container">
      <div className="sign-container">
        <div className="sign-fields">
          <div className="title">Hello!</div>
          <div className="subtitle">Let's study</div>
          <form onSubmit={formik.handleSubmit}>
            <TextInput
              placeholder="login"
              name="login"
              value={formik.values.login}
              onChange={formik.handleChange}
            ></TextInput>

            <PasswordInput
              placeholder="password"
              name="password"
              value={formik.values.password}
              onChange={formik.handleChange}
            />

            <button type="submit" className="submit-btn">
              Sign In
            </button>
          </form>
          <div className="redirect">
            Don't have an account yet? <Link to="/SignUp">Sign Up</Link>
          </div>
        </div>
      </div>
      <div className="background-container">
        <img src={background} className="background" alt="background" />
      </div>
    </div>
  );
};
export default SignUp;
