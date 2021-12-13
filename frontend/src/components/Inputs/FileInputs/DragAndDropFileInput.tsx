import { useDropzone } from "react-dropzone";
import { ReactComponent as VideoInput } from "../../../assets/icons/videoInput.svg";
import styles from "./DragAndDropFileInput.module.scss";
function Dropzone() {
  const { getInputProps, open, acceptedFiles } = useDropzone({
    // Disable click and keydown behavior
    noClick: true,
    noKeyboard: true,
  });
  interface File {
    path: string;
  }
  const files = acceptedFiles.map((file: any) => (
    <li key={file.path}>
      {file.path} - {file.size} bytes
    </li>
  ));

  return (
    <div className={styles["dropzone"]}>
      <div className={styles["dropzone_items"]}>
        <input {...getInputProps()} />
        <VideoInput className={styles["dropzone_img"]} />
        <div className={styles["dropzone_title"]}>Drag and drop file or</div>
        <button type="button" onClick={open} className={styles["dropzone_btn"]}>
          choose from computer
        </button>
        {files}
      </div>
    </div>
  );
}
export default Dropzone;
