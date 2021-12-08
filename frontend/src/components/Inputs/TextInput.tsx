import styles from "./Inputs.module.scss";
const TextInput = (props: {
  name: string;
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder?: string;
}): JSX.Element => {
  return (
    <div>
      <div className={styles["container"]}>
        <input
          name={props.name}
          placeholder={props.placeholder}
          value={props.value}
          onChange={props.onChange}
          className={`${styles.container_input} ${styles.eye}`}
        />
      </div>
    </div>
  );
};

export default TextInput;
