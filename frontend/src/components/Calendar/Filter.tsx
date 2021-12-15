import { endOfWeek, format, startOfWeek } from "date-fns";

import UserDetails from "../UserDetails/UserDetails";
import { ReactComponent as Add } from "../../assets/icons/add.svg";
import { ReactComponent as LeftArrow } from "../../assets/icons/leftArrow.svg";
import { ReactComponent as RightArrow } from "../../assets/icons/rightArrow.svg";

import styles from "./Filter.module.scss";

interface Props {
  showModalHandle: () => void;
  changeWeekHandle: (btnType: string) => void;
  currentDate: Date;
}

function Filter({ showModalHandle, changeWeekHandle, currentDate }: Props) {
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
      <div className={styles.userContainer}>
        <button onClick={showModalHandle} className={styles.add}>
          <Add />
        </button>
        <UserDetails />
      </div>
    </div>
  );
}

export default Filter;
