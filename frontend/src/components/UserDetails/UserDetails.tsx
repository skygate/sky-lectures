import { ReactComponent as UserIcon } from "../../assets/icons/user.svg";

import styles from "./UserDetails.module.scss";

function UserDetails() {
  return (
    <div className={styles["userDetails"]}>
      <button className={styles["userDetails--button"]}>
        <UserIcon />
      </button>
      <p className={styles["userDetails--name"]}>User</p>
    </div>
  );
}

export default UserDetails;
