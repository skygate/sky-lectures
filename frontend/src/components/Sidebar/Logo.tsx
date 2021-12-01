import { Link } from "react-router-dom";

import { ReactComponent as LogoIcon } from "../../assets/icons/logo.svg";

import "./Logo.modules.scss";

function Logo() {
  return (
    <div className="sidebar__logo">
      <Link to="/" className="sidebar__logo--link">
        <LogoIcon />
      </Link>
    </div>
  );
}

export default Logo;
