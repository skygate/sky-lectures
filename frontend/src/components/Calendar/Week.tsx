import styles from "./Week.module.scss";

const DAY_OF_WEEK = ["mon", "tue", "wen", "thu", "fri", "sat", "sun"];

function Week() {
  return (
    <div className={styles.week}>
      <div></div>
      {DAY_OF_WEEK.map((item, i) => (
        <div className={styles.day} key={i}>
          {item}
        </div>
      ))}
    </div>
  );
}

export default Week;
