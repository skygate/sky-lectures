import styles from "./Sidebar.module.scss";

function Sidebar() {
  const items = [];

  for (let i = 8; i < 21; i++) {
    items.push(
      <div className={styles.hour} key={i}>
        <span className={styles.textHour}>{i}:00</span>
      </div>
    );
  }

  return <div className={styles.sidebar}>{items}</div>;
}

export default Sidebar;
