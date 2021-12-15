import styles from "./SearchBarModalContent.module.scss";

function ModalContent({ clickHandler }: { clickHandler: () => void }) {
  return <div onClick={clickHandler} className={styles["modalContent"]}></div>;
}

export default ModalContent;
