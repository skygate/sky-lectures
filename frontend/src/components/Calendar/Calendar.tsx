import { useState } from "react";
import { subWeeks, addWeeks, startOfWeek, addDays } from "date-fns";

import Sidebar from "./Sidebar";
import Day from "./Day";
import Filter from "./Filter";
import Week from "./Week";
import CalendarForm from "./CalendarForm";
import FormModal from "../Modal/FormModal";

import Styles from "./Calendar.module.scss";

const presentation = [
  {
    id: "01",
    author: "Author",
    title: "presentation name",
    startTime: new Date("2021-12-10T10:40:00"),
    endTime: new Date("2021-12-10T10:55:00"),
  },
  {
    id: "02",
    author: "Author",
    title: "presentation name",
    startTime: new Date("2021-12-10T16:40:00"),
    endTime: new Date("2021-12-10T19:40:00"),
  },
];

function Calendar() {
  const [formState, setFormState] = useState({
    showForm: false,
    showModal: false,
  });
  const [currentDate, setCurrentDate] = useState(new Date());
  const startDate = startOfWeek(currentDate, { weekStartsOn: 1 });

  const days = [];

  for (let i = 0; i < 7; i++) {
    days.push(addDays(startDate, i));
  }

  function changeWeekHandle(btnType: string) {
    if (btnType === "prev") {
      setCurrentDate(subWeeks(currentDate, 1));
    }

    if (btnType === "next") {
      setCurrentDate(addWeeks(currentDate, 1));
    }
  }

  function showModalHandle() {
    setFormState({
      showForm: true,
      showModal: true,
    });
  }

  function hideModalHandle() {
    setFormState({
      showForm: false,
      showModal: false,
    });
  }

  return (
    <div className={Styles.calendar}>
      <Filter
        showModalHandle={showModalHandle}
        changeWeekHandle={changeWeekHandle}
        currentDate={currentDate}
      />
      <Week currentDate={currentDate} />
      <div className={Styles.container}>
        <Sidebar />
        {days.map((day, i) => (
          <Day key={i} presentations={presentation} date={day} />
        ))}
      </div>
      {formState.showForm && <CalendarForm hideModal={hideModalHandle} />}
      <FormModal
        handleClick={hideModalHandle}
        modalOpen={formState.showModal}
      ></FormModal>
    </div>
  );
}

export default Calendar;
