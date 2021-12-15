import React from "react";
import styles from "./NextButton.module.scss";
const NextButton = (props: {
  onClick?: (event: React.MouseEvent<HTMLButtonElement>) => void;
}) => {
  return (
    <div>
      <button
        type="submit"
        className={styles["next__btn"]}
        onClick={props.onClick}
      >
        continue
      </button>
    </div>
  );
};
export default NextButton;
