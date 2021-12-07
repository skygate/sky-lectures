import React from "react";
import { createPortal } from "react-dom";

import "./SearchBarModal.modules.scss";

type Props = {
  modalOpen: boolean;
};

const Modal: React.FC<Props> = ({ modalOpen, children }) => {
  if (!modalOpen) return null;

  return createPortal(
    <div className="modal">{children}</div>,
    document.getElementById("searchBarModal")!
  );
};

export default Modal;
