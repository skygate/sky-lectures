import styles from "./SignUp.module.scss";
import background from "../../assets/icons/background.svg";
import PasswordInput from "../../components/Inputs/PasswordInput";
import TextInput from "../../components/Inputs/TextInput";
import { useFormik } from "formik";
import { Link } from "react-router-dom";
import {Register} from "../../services/Register";
import * as Yup from "yup"
import { useState } from "react";
const SignUp = () => {
  const [passwordValidation, showPasswordValidation]=useState(false)
  const validationSchema = Yup.object({
    username: Yup.string(),
    email: Yup.string().required("required"),
    password: Yup.string(),
    confirmedPassword:Yup.string(),
    firstName:Yup.string(),
    lastName:Yup.string()
  })
  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
      confirmedPassword:"",
      firstName:"",
      lastName:""
    },
    validationSchema:validationSchema,

    onSubmit: async (values) => {
      console.log(values)
     Register(values)
    },
  });
  const onFocus = ()=>{
    showPasswordValidation(true)
  }
  return (
    <div className={styles["main-container"]}>
      <div className={styles["sign-container"]}>
        <div className={styles["sign-fields"]}>
          <div className={styles["title"]}>Let's get started!</div>
          <div className={styles["subtitle"]}>It's pleasure to meet you</div>
          <form onSubmit={formik.handleSubmit}>
            <TextInput
              placeholder="username"
              name="username"
              value={formik.values.username}
              onChange={formik.handleChange}
            ></TextInput>
            <TextInput
              placeholder="email"
              name="email"
              value={formik.values.email}
              onChange={formik.handleChange}
            ></TextInput>
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
            {passwordValidation&& <ul><li>must</li></ul>}
            <PasswordInput
              placeholder="confirm password"
              name="confirmedPassword"
              value={formik.values.confirmedPassword}
              onChange={formik.handleChange}
            />

            <button type="submit" className={styles["submit-btn"]}>
              Sign Up
            </button>
          </form>
          <div className={styles["redirect"]}>
            Already have an account <Link to="/SignIn">Sign In</Link>
          </div>
          {formik.errors.email}
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
