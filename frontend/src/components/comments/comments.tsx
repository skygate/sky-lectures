import TextInput from "../Inputs/TextInput";
import person from "../../assets/icons/person.svg";
import "./comments.modules.scss";
const Comments = () => {
  return (
    <div className="comments-container">
      <div className="new-comment">
        <img src={person} alt="person" />
        <input
          type="text"
          className="comment-input"
          placeholder="type something nice"
        />
      </div>
      <div className="buttons-container">
        <a>Cancel</a>
        <a>Comment</a>
      </div>
    </div>
  );
};
export default Comments;
