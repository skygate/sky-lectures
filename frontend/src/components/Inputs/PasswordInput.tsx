import { useState } from "react";
import eye from "../../assets/icons/showPassword.svg";
import styles from "./Inputs.module.scss";
const PasswordInput = (props: {
  name: string;
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder?: string;
}): JSX.Element => {
  const [passwordShown, setPasswordShown] = useState(false);

  return (
    <div>
      <div className={styles["container"]}>
        <input
          name={props.name}
          type={passwordShown ? "text" : "password"}
          placeholder={props.placeholder ? props.placeholder : "Password"}
          value={props.value}
          onChange={props.onChange}
          className={styles["container-input"]}
        />
        <div>
          <img
            className={styles["container-eye"]}
            draggable="false"
            src={eye}
            onClick={() => setPasswordShown(!passwordShown)}
            alt="img"
          />
        </div>
      </div>
    </div>
  );
};

export default PasswordInput;
