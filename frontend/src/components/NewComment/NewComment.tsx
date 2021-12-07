import { ReactComponent as Person } from "../../assets/icons/person.svg";
import styles from "./NewComment.module.scss";
const NewComment = () => {
  return (
    <div className={styles["comments-container"]}>
      <form>
        <div className={styles["new-comment"]}>
          <Person />
          <input
            type="text"
            className={styles["comment-input"]}
            placeholder="type something nice"
          />
        </div>
        <button type="submit" className={styles["submit-comment-btn"]}>
          Comment
        </button>
      </form>
    </div>
  );
};
export default NewComment;
