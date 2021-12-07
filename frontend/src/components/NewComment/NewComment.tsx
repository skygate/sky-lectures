import { ReactComponent as Person } from "../../assets/icons/person.svg";
import "./NewComment.modules.scss";
const NewComment = () => {
  return (
    <div className="comments-container">
      <form>
        <div className="new-comment">
          <Person />
          <input
            type="text"
            className="comment-input"
            placeholder="type something nice"
          />
        </div>

        <button type="submit" className="submit-comment-btn">
          Comment
        </button>
      </form>
    </div>
  );
};
export default NewComment;
