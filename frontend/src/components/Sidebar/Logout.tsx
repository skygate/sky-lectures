import { Link } from "react-router-dom";

import { ReactComponent as QuitIcon } from "../../assets/icons/quit.svg";

import "./Logout.modules.scss";

function Logout() {
  return (
    <div className="sidebar__logout">
      <Link to="/signout">
        <QuitIcon />
      </Link>
    </div>
  );
}

export default Logout;
