import { Link } from "react-router-dom";

import NavigationElement from "./NavigationElement";
import { ReactComponent as LogoIcon } from "../../assets/icons/logo.svg";
import { ReactComponent as HomeIcon } from "../../assets/icons/home.svg";
import { ReactComponent as HeartIcon } from "../../assets/icons/heart.svg";
import { ReactComponent as UploadIcon } from "../../assets/icons/upload.svg";
import { ReactComponent as FileIcon } from "../../assets/icons/file.svg";
import { ReactComponent as ClockIcon } from "../../assets/icons/clock.svg";
import { ReactComponent as QuitIcon } from "../../assets/icons/quit.svg";

import styles from "./Sidebar.module.scss";

function Sidebar() {
  return (
    <nav className={styles["sidebar"]}>
      <div className={styles["sidebar__logo"]}>
        <Link to="/" className={styles["sidebar__logo--link"]}>
          <LogoIcon />
        </Link>
      </div>
      <div className={styles["sidebar__navigation"]}>
        <ul className={styles["sidebar__navigation--list"]}>
          <NavigationElement Icon={<HomeIcon />} path="/" />
          <NavigationElement Icon={<HeartIcon />} path="/favorites" />
          <NavigationElement Icon={<UploadIcon />} path="/uploads" />
          <NavigationElement Icon={<FileIcon />} path="/schedule" />
          <NavigationElement Icon={<ClockIcon />} path="/history" />
        </ul>
      </div>
      <div className={styles["sidebar__footer"]}>
        <Link to="/signout" className={styles["sidebar__footer--link"]}>
          <QuitIcon />
        </Link>
      </div>
    </nav>
  );
}

export default Sidebar;
