import "./Inputs.modules.scss";
const TextInput = (props: {
  name: any;
  value: any;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder?: any;
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
