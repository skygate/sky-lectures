import { NavLink } from "react-router-dom";

import "./NavigationElement.modules.scss";

interface ElementProps {
  Icon: React.SVGProps<SVGElement>;
  path: string;
}

const NavigationElement = ({ Icon, path }: ElementProps) => {
  return (
    <li className="navigation__element">
      <NavLink
        to={path}
        className={({ isActive }) =>
          "navigation__element--link" + (isActive ? " active" : "")
        }
      >
        {Icon}
      </NavLink>
    </li>
  );
};

export default NavigationElement;
