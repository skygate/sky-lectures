import styles from "./SignUp.module.scss";
import background from "../../assets/icons/background.svg";
import PasswordInput from "../../components/Inputs/PasswordInput";
import TextInput from "../../components/Inputs/TextInput";
import { useFormik } from "formik";
import { Link } from "react-router-dom";
import { Register } from "../../services/Register";
import * as Yup from "yup";
import { useState } from "react";
const SignUp = () => {
  const [passwordValidation, showPasswordValidation] = useState(false);
  const validationSchema = Yup.object({
    username: Yup.string().required("required"),
    email: Yup.string().required("required").email("isnt email"),
    // .matches(
    //   /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/,
    //   "Must Contain 8 Characters, One Uppercase, One Lowercase, One Number and One Special Case Character"
    password: Yup.string()
      .matches(/^(?=.*[a-z])/, "Must Contain One Lowercase Character")
      .matches(/^(?=.*[A-Z])/, "Must Contain One Uppercase Character")
      .matches(/^(?=.*[0-9])/, "Must Contain a number")
      .matches(/^(?=.*[!@#\$%\^&\*])/, "Must Contain a special character")
      .required("required"),

    confirmedPassword: Yup.string()
      .required("required")
      .oneOf([Yup.ref("password"), null], "Passwords must match"),

    firstName: Yup.string(),
    lastName: Yup.string(),
  });

  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
      confirmedPassword: "",
      firstName: "",
      lastName: "",
    },
    validationSchema: validationSchema,

    onSubmit: async (values) => {
      console.log(formik.errors);
      //Register(values)
    },
  });
  const onFocus = () => {
    showPasswordValidation(true);
  };
  return (
    <div className={styles["main-container"]}>
      <div className={styles["sign-container"]}>
        <div className={styles["sign-fields"]}>
          <div className={styles["title"]}>Let's get started!</div>
          <div className={styles["subtitle"]}>It's pleasure to meet you</div>
          <form
            onSubmit={formik.handleSubmit}
            className={styles["form__fields"]}
          >
            <TextInput
              placeholder="username"
              name="username"
              value={formik.values.username}
              onChange={formik.handleChange}
            ></TextInput>
            {formik.errors.username && (
              <div className={styles["field-error"]}>
                {formik.errors.username}
              </div>
            )}
            <TextInput
              placeholder="email"
              name="email"
              value={formik.values.email}
              onChange={formik.handleChange}
            ></TextInput>
            {formik.errors.email && (
              <div className={styles["field-error"]}>{formik.errors.email}</div>
            )}
            <TextInput
              placeholder="first name"
              name="firstName"
              value={formik.values.firstName}
              onChange={formik.handleChange}
            ></TextInput>
            <TextInput
              placeholder="last name"
              name="lastName"
              value={formik.values.lastName}
              onChange={formik.handleChange}
            ></TextInput>
            <PasswordInput
              placeholder="password"
              name="password"
              value={formik.values.password}
              onChange={formik.handleChange}
              onFocus={onFocus}
            />
            {passwordValidation && (
              <ul className={styles["errors_list"]}>
                <li
                  className={
                    formik.errors.password ==
                    "Must Contain One Lowercase Character"
                      ? styles["field-error-active"]
                      : styles["field-error"]
                  }
                >
                  Must Contain One Lowercase Character
                </li>
                <li
                  className={
                    formik.errors.password ==
                    "Must Contain One Uppercase Character"
                      ? styles["field-error-active"]
                      : styles["field-error"]
                  }
                >
                  Must Contain One Uppercase Character
                </li>
                <li
                  className={
                    formik.errors.password == "Must Contain a special character"
                      ? styles["field-error-active"]
                      : styles["field-error"]
                  }
                >
                  Must Contain a special character
                </li>
                <li
                  className={
                    formik.errors.password == "Must Contain a number"
                      ? styles["field-error-active"]
                      : styles["field-error"]
                  }
                >
                  Must Contain a number
                </li>
              </ul>
            )}

            <PasswordInput
              placeholder="confirm password"
              name="confirmedPassword"
              value={formik.values.confirmedPassword}
              onChange={formik.handleChange}
            />
            {formik.errors.confirmedPassword && (
              <div className={styles["field-error"]}>
                {formik.errors.confirmedPassword}
              </div>
            )}

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
