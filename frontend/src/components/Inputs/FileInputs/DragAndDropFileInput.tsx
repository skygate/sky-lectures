import { useDropzone } from "react-dropzone";
import { ReactComponent as VideoInput } from "../../../assets/icons/videoInput.svg";
import styles from "./DragAndDropFileInput.module.scss";
import { useCallback } from "react";
function Dropzone(props: { setUploadForm: Function }) {
  const onDrop = useCallback((acceptedFiles) => {
    props.setUploadForm({ file: acceptedFiles });
  }, []);
  const { getRootProps, getInputProps, open, acceptedFiles } = useDropzone({
    onDrop,
    noClick: true,
    noKeyboard: true,
    maxFiles: 1,
  });

  const files = acceptedFiles.map((file: File) => (
    <li key={file.name}>
      {file.name} - {file.size} bytes
    </li>
  ));

  return (
    <div className={styles["dropzone"]}>
      <div {...getRootProps()} className={styles["dropzone_items"]}>
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
