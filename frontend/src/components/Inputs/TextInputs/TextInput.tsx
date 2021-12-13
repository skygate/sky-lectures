import styles from "./Inputs.module.scss";
const TextInput = (props: {
  name: string;

  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder?: string;
  inputStyle?: string;
  containerStyles?: string;
}): JSX.Element => {
  return (
    <div className={`${styles.container} ${props.containerStyles}`}>
      <input
        name={props.name}
        placeholder={props.placeholder}
        value={props.value}
        onChange={props.onChange}
        className={`${styles.container_input} ${props.inputStyle}`}
      />
    </div>
  );
};

export default TextInput;
