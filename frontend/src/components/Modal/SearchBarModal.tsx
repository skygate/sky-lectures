import React from "react";
import { createPortal } from "react-dom";

import styles from "./SearchBarModal.module.scss";

type Props = {
  modalOpen: boolean;
};

const Modal: React.FC<Props> = ({ modalOpen, children }) => {
  if (!modalOpen) return null;

  return createPortal(
    <div className={styles["modal"]}>{children}</div>,
    document.getElementById("searchBarModal")!
  );
};

export default Modal;
