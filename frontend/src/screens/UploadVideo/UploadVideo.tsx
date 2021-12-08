import Sidebar from "../../components/Sidebar/Sidebar";
import styles from "./UploadVideo.module.scss";
import { useState } from "react";
import DescribeVideo from "./DescribeVideo";
const UploadVideo = () => {
  const [UploadStep, setUploadStep] = useState(0);
  return (
    <div>
      <Sidebar />
      <div className={styles["main-content"]}>
        <div className={styles["upload"]}>
          <div className={styles["upload-info"]}>
            <h1>Show us some of your knowleage</h1>
            <p>
              {UploadStep === 0 &&
                "Upload your work. First show will be used as thumbnail"}
            </p>
          </div>
          <button onClick={() => setUploadStep(UploadStep + 1)}>
            continue
          </button>
        </div>
        {UploadStep === 0 && <div className={styles["drag-drop"]}>dropbox</div>}
        {UploadStep === 1 && (
          <div>
            <DescribeVideo />
          </div>
        )}
      </div>
    </div>
  );
};
export default UploadVideo;
