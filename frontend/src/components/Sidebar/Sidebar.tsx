import { Link } from "react-router-dom";

import NavigationElement from "./NavigationElement";
import { ReactComponent as LogoIcon } from "../../assets/icons/logo.svg";
import { ReactComponent as HomeIcon } from "../../assets/icons/home.svg";
import { ReactComponent as HeartIcon } from "../../assets/icons/heart.svg";
import { ReactComponent as UploadIcon } from "../../assets/icons/upload.svg";
import { ReactComponent as FileIcon } from "../../assets/icons/file.svg";
import { ReactComponent as ClockIcon } from "../../assets/icons/clock.svg";
import { ReactComponent as QuitIcon } from "../../assets/icons/quit.svg";

import "./Sidebar.modules.scss";

function Sidebar() {
  return (
    <nav className="sidebar">
      <div className="sidebar__logo">
        <Link to="/" className="sidebar__logo--link">
          <LogoIcon />
        </Link>
      </div>
      <div className="sidebar__navigation">
        <ul className="sidebar__navigation--list">
          <NavigationElement Icon={<HomeIcon />} path="/" />
          <NavigationElement Icon={<HeartIcon />} path="/favourites" />
          <NavigationElement Icon={<UploadIcon />} path="/uploads" />
          <NavigationElement Icon={<FileIcon />} path="/schedule" />
          <NavigationElement Icon={<ClockIcon />} path="/history" />
        </ul>
      </div>
      <div className="sidebar__foter">
        <Link to="/signout" className="sidebar__footer--link">
          <QuitIcon />
        </Link>
      </div>
    </nav>
  );
}

export default Sidebar;
