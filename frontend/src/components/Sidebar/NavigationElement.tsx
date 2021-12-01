import { NavLink } from "react-router-dom";

import "./NavigationElement.modules.scss";

interface ElementProps {
  Icon: React.SVGProps<SVGElement>;
  path: string;
}

const NavigationElement = ({ Icon, path }: ElementProps) => {
  return (
    <li className="sidebar__navigation--element">
      <NavLink
        to={path}
        className={({ isActive }) => (isActive ? " active" : "")}
      >
        {Icon}
      </NavLink>
    </li>
  );
};

export default NavigationElement;
