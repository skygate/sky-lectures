import { useState } from "react";
import eye from "../../assets/showPassword.svg";
import "./Inputs.modules.scss";
const PasswordInput = (props: {
  name: any;
  value: any;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder?: any;
}): JSX.Element => {
  const [passwordShown, setPasswordShown] = useState(false);

  return (
    <div>
      <div className="container">
        <input
          name={props.name}
          type={passwordShown ? "text" : "password"}
          placeholder={props.placeholder ? props.placeholder : "Password"}
          value={props.value}
          onChange={props.onChange}
          className="container-input"
        />
        <div>
          <img
            className="container-eye"
            draggable="false"
            src={eye}
            onClick={() => setPasswordShown(!passwordShown)}
          />
        </div>
      </div>
    </div>
  );
};

export default PasswordInput;
