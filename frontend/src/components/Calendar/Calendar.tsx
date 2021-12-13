import Sidebar from "./Sidebar";
import Day from "./Day";
import Filter from "./Filter";
import Week from "./Week";

import Styles from "./Calendar.module.scss";

function Calendar() {
  const week = [];

  for (let i = 0; i < 7; i++) {
    week.push(<Day key={i} />);
  }

  return (
    <div className={Styles.calendar}>
      <Filter />
      <Week />
      <div className={Styles.container}>
        <Sidebar />
        {week}
      </div>
    </div>
  );
}

export default Calendar;
