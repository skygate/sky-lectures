import { startOfWeek, format, addDays } from "date-fns";

import styles from "./Week.module.scss";

interface Props {
  currentDate: Date;
}

function Week({ currentDate }: Props) {
  const days = [];
  let startDate = startOfWeek(currentDate, { weekStartsOn: 1 });

  for (let i = 0; i < 7; i++) {
    days.push(addDays(startDate, i));
  }

  return (
    <div className={styles.week}>
      <div></div>
      {days.map((day, i) => (
        <div className={styles.day} key={i}>
          <span className={styles.number}>{format(day, "dd")}</span>
          <span className={styles.name}>{format(day, "EEE")}</span>
        </div>
      ))}
    </div>
  );
}

export default Week;
