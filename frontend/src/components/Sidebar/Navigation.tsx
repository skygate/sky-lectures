import { ReactComponent as HomeIcon } from "../../assets/icons/home.svg";
import { ReactComponent as HeartIcon } from "../../assets/icons/heart.svg";
import { ReactComponent as UploadIcon } from "../../assets/icons/upload.svg";
import { ReactComponent as FileIcon } from "../../assets/icons/file.svg";
import { ReactComponent as ClockIcon } from "../../assets/icons/clock.svg";
import NavigationElement from "./NavigationElement";

import "./Navigation.modules.scss";

function Navigation() {
  return (
    <div className="sidebar__navigation">
      <ul>
        <NavigationElement Icon={<HomeIcon />} path="/" />
        <NavigationElement Icon={<HeartIcon />} path="/favourites" />
        <NavigationElement Icon={<UploadIcon />} path="/uploads" />
        <NavigationElement Icon={<FileIcon />} path="/schedule" />
        <NavigationElement Icon={<ClockIcon />} path="/history" />
      </ul>
    </div>
  );
}

export default Navigation;
