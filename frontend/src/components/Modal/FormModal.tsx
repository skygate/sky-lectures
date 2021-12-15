import React from "react";
import { createPortal } from "react-dom";

import styles from "./FormModal.module.scss";

type Props = {
  modalOpen: boolean;
  handleClick: () => void;
};

const FormModal: React.FC<Props> = ({ modalOpen, handleClick, children }) => {
  if (!modalOpen) return null;

  return createPortal(
    <div onClick={handleClick} className={styles.modal}>
      {children}
    </div>,
    document.getElementById("formModal")!
  );
};

export default FormModal;
