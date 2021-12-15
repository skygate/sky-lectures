import { NavLink } from "react-router-dom";

import styles from "./NavigationElement.module.scss";

interface ElementProps {
  Icon: React.SVGProps<SVGElement>;
  path: string;
}

const NavigationElement = ({ Icon, path }: ElementProps) => {
  return (
    <li className={styles["navigation__element"]}>
      <NavLink
        to={path}
        className={({ isActive }) =>
          styles["navigation__element--link"] + (isActive ? " active" : "")
        }
      >
        {Icon}
      </NavLink>
    </li>
  );
};

export default NavigationElement;
