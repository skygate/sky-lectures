import "./SearchBarModalContent.modules.scss";

function ModalContent({ clickHandler }: { clickHandler: () => void }) {
  return <div onClick={clickHandler} className="modalContent"></div>;
}

export default ModalContent;
