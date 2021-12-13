import TextInput from "../../components/Inputs/TextInputs/TextInput";
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
      <div className={styles["last-step_title"]}>Last step</div>
      <div className={styles["last-step_sub_title"]}>
        Add some tags to help viewers find your content.
      </div>
      <form className={styles["last-step_tag_form"]}>
        <TextInput
          placeholder="Type your tag"
          name="videoDescription"
          value={formik.values.videoDescription}
          onChange={formik.handleChange}
          inputStyle={styles.input}
          containerStyles={styles.input_container}
        />
        <div className={styles["last-step_tag_form_btn_container"]}>
          <button className={styles["submit_btn"]}>Upload</button>
        </div>
      </form>
    </div>
  );
};
export default AddTag;
