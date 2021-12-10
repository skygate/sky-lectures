import TextInput from "../../components/Inputs/TextInput";
import { useFormik } from "formik";
import styles from "./AddTags.module.scss";

const AddTag = () => {
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
    <div className={styles["last-step"]}>
      <h1 className={styles["last-step_title"]}>Last step</h1>
      <h2>Add some tags to help viewers find your content.</h2>
      <TextInput
        placeholder="Type your tag"
        name="videoDescription"
        value={formik.values.videoDescription}
        onChange={formik.handleChange}
      />
    </div>
  );
};
export default AddTag;
