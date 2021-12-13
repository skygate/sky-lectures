import { endOfWeek, format, startOfWeek } from "date-fns";

import { ReactComponent as LeftArrow } from "../../assets/icons/leftArrow.svg";
import { ReactComponent as RightArrow } from "../../assets/icons/rightArrow.svg";
import UserDetails from "../UserDetails/UserDetails";

import styles from "./Filter.module.scss";

interface Props {
  changeWeekHandle: (btnType: string) => void;
  currentDate: Date;
}

function Filter({ changeWeekHandle, currentDate }: Props) {
  const startDayFormat = "dd MMMM";
  const lastDayFormat = "dd MMMM yyyy";

  const startDay = startOfWeek(currentDate, { weekStartsOn: 1 });
  const lastDay = endOfWeek(currentDate, { weekStartsOn: 1 });

  return (
    <div className={styles.filter}>
      <span className={styles.name}>Schedule Presentation</span>
      <div className={styles.container}>
        <button className={styles.btn} onClick={() => changeWeekHandle("prev")}>
          <LeftArrow />
        </button>
        <span className={styles.week}>
          {format(startDay, startDayFormat)} - {format(lastDay, lastDayFormat)}{" "}
        </span>
        <button className={styles.btn} onClick={() => changeWeekHandle("next")}>
          <RightArrow />
        </button>
      </div>
      <UserDetails />
    </div>
  );
}

export default Filter;
