import React from "react";

import styles from "./CustomButton.module.scss";

interface Props {
  children: string;
  value?: string;
  filter: string;
  handleClick: (e: React.MouseEvent<HTMLButtonElement>) => void;
}

function CustomButton({ children, value = "", filter, handleClick }: Props) {
  return (
    <button
      className={`${styles["customButton"]} ${
        filter === value && styles["active"]
      }`}
      onClick={handleClick}
      value={value}
    >
      {children}
    </button>
  );
}

export default CustomButton;
