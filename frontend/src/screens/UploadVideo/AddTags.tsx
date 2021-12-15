import TextInput from "../../components/Inputs/TextInputs/TextInput";
import { useFormik } from "formik";
import styles from "./AddTags.module.scss";
import { UploadForm } from "../../types/UploadForm";

const AddTag = (props: { uploadForm: UploadForm }) => {
  var uploadForm = props.uploadForm;
  const formik = useFormik({
    initialValues: {
      tags: "",
    },

    onSubmit: async (values) => {
      uploadForm.tags = values.tags;
      console.log(uploadForm);
    },
  });
  return (
    <div className={styles["last_step"]}>
      <div className={styles["last_step_title"]}>Last step</div>
      <div className={styles["last_step_sub_title"]}>
        Add some tags to help viewers find your content.
      </div>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          formik.handleSubmit(e);
        }}
        className={styles["last_step_tag_form"]}
      >
        <TextInput
          placeholder="Type your tag"
          name="tags"
          value={formik.values.tags}
          onChange={formik.handleChange}
          inputStyle={styles.input}
          containerStyles={styles.input_container}
        />
        <div className={styles["last_step_tag_form_btn_container"]}>
          <button type="submit" className={styles["submit_btn"]}>
            Upload
          </button>
        </div>
      </form>
    </div>
  );
};
export default AddTag;
