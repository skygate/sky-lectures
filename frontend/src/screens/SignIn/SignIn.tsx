import styles from "../SignUp/SignUp.module.scss";
import background from "../../assets/icons/background.svg";
import PasswordInput from "../../components/Inputs/TextInputs/PasswordInput";
import TextInput from "../../components/Inputs/TextInputs/TextInput";
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
    <div className={styles["main-container"]}>
      <div className={styles["sign-container"]}>
        <div className={styles["sign-fields"]}>
          <div className={styles["title"]}>Hello!</div>
          <div className={styles["subtitle"]}>Let's study</div>
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

            <button type="submit" className={styles["submit-btn"]}>
              Sign In
            </button>
          </form>
          <div className={styles["redirect"]}>
            Don't have an account yet? <Link to="/SignUp">Sign Up</Link>
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
