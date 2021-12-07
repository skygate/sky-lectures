import React from "react";

import "./CustomButton.modules.scss";

interface Props {
  children: string;
  value?: string;
  filter: string;
  handleClick: (e: React.MouseEvent<HTMLButtonElement>) => void;
}

function CustomButton({ children, value = "", filter, handleClick }: Props) {
  return (
    <button
      className={`customButton ${filter === value && "active"}`}
      onClick={handleClick}
      value={value}
    >
      {children}
    </button>
  );
}

export default CustomButton;
