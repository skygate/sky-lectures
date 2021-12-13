import styles from "./SignUp.module.scss";
import background from "../../assets/icons/background.svg";
import PasswordInput from "../../components/Inputs/TextInputs/PasswordInput";
import TextInput from "../../components/Inputs/TextInputs/TextInput";
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
    <div className={styles["main-container"]}>
      <div className={styles["sign-container"]}>
        <div className={styles["sign-fields"]}>
          <div className={styles["title"]}>Let's get started!</div>
          <div className={styles["subtitle"]}>It's pleasure to meet you</div>
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
              placeholder="password"
              name="password"
              value={formik.values.password}
              onChange={formik.handleChange}
            />

            <button type="submit" className={styles["submit-btn"]}>
              Sign Up
            </button>
          </form>
          <div className={styles["redirect"]}>
            Already have an account <Link to="/SignIn">Sign In</Link>
          </div>
        </div>
      </div>
      <div className={styles["background-container"]}>
        <img
          src={background}
          className={styles["background"]}
          alt="background"
        />
      </div>
    </div>
  );
};
export default SignUp;
