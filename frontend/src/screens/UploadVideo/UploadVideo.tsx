import Sidebar from "../../components/Sidebar/Sidebar";
import styles from "./UploadVideo.module.scss";
import { useState } from "react";
import DescribeVideo from "./DescribeVideo";
import { UploadForm } from "../../types/UploadForm";
import NextButton from "../../components/Nextbutton/NextButton";
import Dropzone from "../../components/Inputs/FileInputs/DragAndDropFileInput";
const UploadVideo = () => {
  const [UploadStep, setUploadStep] = useState(0);
  const [uploadForm, setUploadForm] = useState<UploadForm>({
    file: null,
    tags: "",
    videoName: "",
    videoDesciption: "",
  });
  function nextPage(): void {
    setUploadStep(UploadStep + 1);
  }

  return (
    <div className={styles["upload__content"]}>
      <Sidebar />
      <div className={styles["upload"]}>
        <div className={styles["upload__title"]}>
          Show us some of your knowleage
        </div>
        <div className={styles["upload__subtitle"]}>
          {UploadStep === 0 &&
            "Upload your work. First show will be used as thumbnail"}
          {UploadStep === 1 && <br />}
        </div>
      </div>
      {UploadStep === 0 && (
        <div className={styles["upload_dropzone"]}>
          <NextButton onClick={nextPage} />
          <Dropzone setUploadForm={setUploadForm} />
        </div>
      )}
      {UploadStep === 1 && (
        <DescribeVideo setUploadForm={setUploadForm} uploadForm={uploadForm} />
      )}
    </div>
  );
};
export default UploadVideo;
