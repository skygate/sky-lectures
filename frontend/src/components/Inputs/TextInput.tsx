import "./Inputs.modules.scss";
const TextInput = (props: {
  name: string;
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder?: string;
}): JSX.Element => {
  return (
    <div>
      <div className="container">
        <input
          name={props.name}
          placeholder={props.placeholder}
          value={props.value}
          onChange={props.onChange}
          className="container-input"
        />
      </div>
    </div>
  );
};

export default TextInput;
