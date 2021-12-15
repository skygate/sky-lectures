import styles from "./DescribeVideo.module.scss";
import TextInput from "../../components/Inputs/TextInputs/TextInput";
import { useFormik } from "formik";
import { useState } from "react";
import { ReactComponent as CloseBtn } from "../../assets/icons/close.svg";
import AddTags from "./AddTags";
import NextButton from "../../components/Nextbutton/NextButton";
import { UploadForm } from "../../types/UploadForm";

const DescribeVideo = (props: {
  setUploadForm: Function;
  uploadForm: UploadForm;
}) => {
  const [isVisible, setModalVisibility] = useState(false);

  const formik = useFormik({
    initialValues: {
      videoName: "",
      videoDescription: "",
    },
    onSubmit: (values) => {
      props.setUploadForm({
        ...props.uploadForm,
        videoName: values.videoName,
        videoDescription: values.videoDescription,
      });
    },
  });

  return (
    <div>
      <div
        className={
          isVisible
            ? `${styles.modal} ${styles.modal_opened}`
            : `${styles.modal} ${styles.modal_closed}`
        }
      >
        <div className={styles["modal_content"]}>
          <AddTags uploadForm={props.uploadForm} />
          <CloseBtn
            className={styles["modal_button-exit"]}
            onClick={() => setModalVisibility(!isVisible)}
          ></CloseBtn>
        </div>
      </div>

      <div className={styles["thumbnail"]}></div>

      <form
        onSubmit={(e) => {
          e.preventDefault();
          formik.handleSubmit(e);
        }}
      >
        <TextInput
          placeholder="Name your work"
          name="videoName"
          value={formik.values.videoName}
          onChange={formik.handleChange}
          containerStyles={styles.input_container}
        />
        <TextInput
          placeholder="Write something more about your work"
          name="videoDescription"
          value={formik.values.videoDescription}
          onChange={formik.handleChange}
          inputStyle={styles.input}
          containerStyles={styles.input_container}
        />
        <NextButton
          onClick={() => {
            setModalVisibility(true);
          }}
        />
      </form>
    </div>
  );
};
export default DescribeVideo;
