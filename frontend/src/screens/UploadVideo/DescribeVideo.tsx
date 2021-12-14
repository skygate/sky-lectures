import styles from "./DescribeVideo.module.scss";
import TextInput from "../../components/Inputs/TextInputs/TextInput";
import { useFormik } from "formik";

const DescribeVideo = (props: { setUploadForm: Function }) => {
  const formik = useFormik({
    initialValues: {
      videoName: "",
      videoDescription: "",
    },

    onSubmit: (values) => {
      props.setUploadForm({
        videoName: values.videoName,
        videoDescription: values.videoDescription,
      });
    },
  });

  return (
    <div className={styles["content"]}>
      <div className={styles["thumbnail"]}></div>
      <div>
        <form>
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
        </form>
      </div>
    </div>
  );
};
export default DescribeVideo;
