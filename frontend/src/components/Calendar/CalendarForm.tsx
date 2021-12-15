import * as Yup from "yup";
import { Formik } from "formik";
import DatePicker from "react-datepicker";
import { setHours, setMinutes } from "date-fns";

import FilterButton from "./FilterButton";
import CustomButton from "./CustomButton";
import { ReactComponent as Arrow } from "../../assets/icons/arrow.svg";
import { ReactComponent as Cross } from "../../assets/icons/cross.svg";

import styles from "./CalendarForm.module.scss";
import "react-datepicker/dist/react-datepicker.css";
import "./DatePicker.modules.scss";

const PresentationSchema = Yup.object().shape({
  title: Yup.string()
    .min(2, "Too Short!")
    .max(30, "Too Long!")
    .required("Required"),
  notificationTime: Yup.number().required(),
});

interface Props {
  hideModal: () => void;
}

function CalendarForm({ hideModal }: Props) {
  return (
    <div className={styles.calendarForm}>
      <div className={styles.titleContainer}>
        <p className={styles.title}>Schedule Presentation</p>
        <button className={styles.close} onClick={hideModal}>
          <Cross />
        </button>
      </div>
      <Formik
        initialValues={{
          title: "",
          startDate: new Date(),
          endDate: new Date(),
          notificationTime: 0,
        }}
        validationSchema={PresentationSchema}
        onSubmit={(values, actions) => {
          setTimeout(() => {
            alert(JSON.stringify(values, null, 2));
            actions.setSubmitting(false);
          }, 1000);
        }}
      >
        {({
          errors,
          touched,
          handleSubmit,
          isSubmitting,
          values,
          setFieldValue,
        }) => {
          return (
            <form className={styles.form} onSubmit={handleSubmit}>
              <input
                className={styles.inputTitle}
                id="title"
                type="text"
                placeholder="Presentation’s title"
                onChange={(value) => {
                  console.log(value.target.value);
                  setFieldValue("title", value.target.value);
                }}
                value={values.title}
              />
              {errors.title && touched.title && (
                <span className={styles.errorTitle}>{errors.title}</span>
              )}
              <div className={styles.date}>
                <span className={styles.name}>When:</span>
                <DatePicker
                  name="date"
                  selected={values.startDate}
                  onChange={(date) => {
                    setFieldValue("startDate", date);
                    setFieldValue("endDate", date);
                  }}
                  wrapperClassName="dateInput"
                  calendarClassName="calendar"
                  dateFormat="dd.MM.yyyy"
                />
              </div>
              <div className={styles.time}>
                <span className={styles.name}>Time:</span>
                <div className={styles.timeContainer}>
                  <div>
                    <DatePicker
                      selected={values.startDate}
                      onChange={(date) => setFieldValue("startDate", date)}
                      showTimeSelect
                      showTimeSelectOnly
                      timeIntervals={15}
                      timeCaption="time"
                      dateFormat="HH:mm"
                      timeFormat="HH:mm"
                      minTime={setHours(setMinutes(new Date(), 0), 8)}
                      maxTime={setHours(setMinutes(new Date(), 0), 20)}
                      wrapperClassName="timeInput"
                      calendarClassName="startTime"
                    />
                  </div>
                  <div className={styles.arrow}>
                    <Arrow />
                  </div>
                  <div>
                    <DatePicker
                      selected={values.endDate}
                      onChange={(date) => setFieldValue("endDate", date)}
                      showTimeSelect
                      showTimeSelectOnly
                      timeIntervals={15}
                      timeCaption="time"
                      dateFormat="HH:mm"
                      timeFormat="HH:mm"
                      minTime={setHours(setMinutes(new Date(), 0), 8)}
                      maxTime={setHours(setMinutes(new Date(), 0), 20)}
                      wrapperClassName="timeInput"
                      calendarClassName="startTime"
                    />
                  </div>
                </div>
              </div>
              <div className={styles.notification}>
                <span className={styles.title}>
                  Send notification to your viewers before presentation?
                </span>
                <div className={styles.container}>
                  <FilterButton
                    handleClick={() => setFieldValue("notificationTime", 0)}
                    value={0}
                    currentValue={values.notificationTime}
                  >
                    none
                  </FilterButton>
                  <FilterButton
                    handleClick={() => setFieldValue("notificationTime", 15)}
                    value={15}
                    currentValue={values.notificationTime}
                  >
                    15 min
                  </FilterButton>
                  <FilterButton
                    handleClick={() => setFieldValue("notificationTime", 30)}
                    value={30}
                    currentValue={values.notificationTime}
                  >
                    30 min
                  </FilterButton>
                  <FilterButton
                    handleClick={() => setFieldValue("notificationTime", 45)}
                    value={45}
                    currentValue={values.notificationTime}
                  >
                    45 min
                  </FilterButton>
                  <FilterButton
                    handleClick={() => setFieldValue("notificationTime", 60)}
                    value={60}
                    currentValue={values.notificationTime}
                  >
                    1h
                  </FilterButton>
                  <FilterButton
                    handleClick={() => setFieldValue("notificationTime", 120)}
                    value={120}
                    currentValue={values.notificationTime}
                  >
                    2h
                  </FilterButton>
                </div>
              </div>
              <div className={styles.btnContainer}>
                <div className={styles.cancel}>
                  <CustomButton handleClick={hideModal} reverseColor={true}>
                    Cancel
                  </CustomButton>
                </div>
                <div>
                  <CustomButton type="submit">Schedule</CustomButton>
                </div>
              </div>
            </form>
          );
        }}
      </Formik>
    </div>
  );
}

export default CalendarForm;
