import styles from "./DescribeVideo.module.scss";
import TextInput from "../../components/Inputs/TextInput";
import { useFormik } from "formik";

const DescribeVideo = () => {
  const formik = useFormik({
    initialValues: {
      videoName: "",
      videoDescription: "",
    },

    onSubmit: async (values) => {
      console.log(values);
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
          />
          <TextInput
            placeholder="Write something more about your work"
            name="videoDescription"
            value={formik.values.videoName}
            onChange={formik.handleChange}
          />
        </form>
      </div>
    </div>
  );
};
export default DescribeVideo;
