import Sidebar from "../../components/Sidebar/Sidebar";
import styles from "./UploadVideo.module.scss";
import { useState } from "react";
import DescribeVideo from "./DescribeVideo";
import AddTags from "./AddTags";
import { ReactComponent as CloseBtn } from "../../assets/icons/close.svg";
import Dropzone from "../../components/Inputs/FileInputs/DragAndDropFileInput";
const UploadVideo = () => {
  function nextPage(): void {
    if (UploadStep === 1) {
      setModalVisibility(true);
    } else {
      setUploadStep(UploadStep + 1);
    }
  }

  const [isVisible, setModalVisibility] = useState(false);
  const [UploadStep, setUploadStep] = useState(0);
  return (
    <div className={styles["main-content"]}>
      <div
        className={
          isVisible
            ? `${styles.modal} ${styles.modal_opened}`
            : `${styles.modal} ${styles.modal_closed}`
        }
      >
        <div className={styles["modal-content"]}>
          <AddTags />
          <CloseBtn
            className={styles["modal-exit_button"]}
            onClick={() => setModalVisibility(!isVisible)}
          ></CloseBtn>
        </div>
      </div>
      <Sidebar />

      <div className={styles["upload"]}>
        <div className={styles["upload-info"]}>
          <h1>Show us some of your knowleage</h1>
          <p>
            {UploadStep === 0 &&
              "Upload your work. First show will be used as thumbnail"}
          </p>
        </div>
        <button onClick={nextPage}>continue</button>
      </div>
      {UploadStep === 0 && (
        <div className={styles["drag-drop"]}>
          <Dropzone />
        </div>
      )}
      {UploadStep === 1 && (
        <div>
          <DescribeVideo />
        </div>
      )}
    </div>
  );
};
export default UploadVideo;
